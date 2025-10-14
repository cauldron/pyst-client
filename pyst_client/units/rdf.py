import json
from functools import lru_cache
from io import BytesIO
from pathlib import Path
from typing import Any, Generator
from zipfile import ZipFile

import orjson
import requests
import skosify
import structlog
from bs4 import BeautifulSoup
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS

from pyst_client.units.errors import GraphFilterError, MissingDimensionVector
from pyst_client.units.utils import (
    DEFAULT_DATA_DIR,
    get_one_in_graph,
    streaming_download,
    to_untyped_literal,
)

VAEM = Namespace("http://www.linkedmodel.org/schema/vaem")
# TODO: Get version through file inspection
QUDTS = Namespace("http://qudt.org/schema/qudt/")
QUDTV = Namespace("http://qudt.org/vocab/")
QK = QUDTV.quantitykind

CS_MAPPING = {
    DCTERMS.description: SKOS.definition,
}

logger = structlog.get_logger("sentier_vocab")

RELATIONSHIPS = {
    SKOS.broaderTransitive,
    SKOS.narrowerTransitive,
    SKOS.broader,
    SKOS.narrower,
    SKOS.exactMatch,
    SKOS.closeMatch,
    SKOS.broadMatch,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
}
HEALTHY_RELATIONSHIPS = {
    SKOS.broader,
    SKOS.exactMatch,
    SKOS.closeMatch,
    SKOS.broadMatch,
    SKOS.narrowMatch,
    SKOS.relatedMatch,
}

vocab_data_dir = Path(__file__).parent / "data"
selected_fp = vocab_data_dir / "selected-quantity-kinds.json"
extra_concepts_data = vocab_data_dir / "extra-data.ttl"
qudt_patches_data = vocab_data_dir / "qudt-patches.ttl"


def clean(s: Any) -> str:
    return BeautifulSoup(str(s), "html.parser").get_text().strip()


class QUDT:
    def __init__(self, data_dir: Path = DEFAULT_DATA_DIR, default_lang: str = "en"):
        self.default_lang = default_lang
        self.selected_qk = {
            URIRef(k): v for k, v in json.load(open(selected_fp)).items()
        }
        self.zipped = ZipFile(open(self.get_latest_version(data_dir), "rb"))
        self.graph = Graph()
        # self.zipfile_prefix = self.get_zipfile_prefix()

        self.cs_uri = URIRef("https://vocab.sentier.dev/units/")
        concept_scheme = self.add_concept_scheme()

        mapping = self.add_quantity_kinds(concept_scheme)
        self.qk_uris = list(mapping.values())
        self.add_units(concept_scheme, mapping)

        # self.graph.parse(extra_concepts_data)
        # self.fill_missing_attributes()
        # self.skosify_checks()

    def add(self, triple: tuple) -> None:
        # Convenient place to put logging or debug checks
        self.graph.add(triple)

    def get_latest_version(self, data_dir: Path) -> Path:
        try:
            catalogue = json.load(open(data_dir / "qudt.json"))
        except (OSError,):
            catalogue = {}
        release = requests.get(
            "https://api.github.com/repos/qudt/qudt-public-repo/releases/latest"
        ).json()["assets"][0]["browser_download_url"]
        if catalogue.get("release") != release:
            fp = str(streaming_download(release))
            with open(data_dir / "qudt.json", "w") as f:
                json.dump({"release": release, "filepath": fp}, f, indent=2)
            return fp
        return catalogue["filepath"]

    def get_graph_for_file(self, path: str) -> Graph:
        for zipinfo in self.zipped.infolist():
            # if zipinfo.filename.startswith(self.zipfile_prefix + path):
            if zipinfo.filename == path:
                return Graph().parse(self.zipped.open(zipinfo.filename))
        raise KeyError

    def write_graph(self, filepath: Path = Path.cwd() / "qudt-sentier-dev.ttl") -> Path:
        self.graph.serialize(destination=filepath)
        return filepath

    def skosify_checks(self):
        # Can't use - create backwards related links to nodes not defined in our graph
        # skosify.infer.skos_related(self.graph)
        skosify.infer.skos_topConcept(self.graph)
        skosify.infer.skos_hierarchical(self.graph, narrower=False)
        # skosify.infer.skos_transitive(self.graph, narrower=True)
        # skosify.infer.rdfs_classes(self.graph)
        # skosify.infer.rdfs_properties(self.graph)

    def concept_scheme(self, as_bytes: bool = True) -> Graph:
        graph = Graph()

        for subj, verb, obj in self.graph.triples((self.cs_uri, None, None)):
            graph.add((subj, verb, obj))

        return graph

    def relationships(self, kind: URIRef) -> Graph:
        graph = Graph()
        concept_uris = self.concept_uris.union(set(self.qk_uris))

        for subj, verb, obj in self.graph.triples((None, kind, None)):
            if subj in concept_uris:
                graph.add((subj, verb, obj))

        return graph

    def concepts(self, sample: bool = False) -> Graph:
        graph = Graph()

        concept_uris = self.concept_uris.union(set(self.qk_uris))

        for subj, verb, obj in self.graph.triples((None, None, None)):
            if subj not in concept_uris:
                continue
            # Will be added later
            if verb in RELATIONSHIPS:
                continue
            else:
                graph.add((subj, verb, obj))

        # Remove alt labels if they are copies of pref labels
        for concept in concept_uris:
            pref_labels = {
                concept: o for s, v, o in graph.triples((concept, SKOS.prefLabel, None))
            }
            for s, v, o in graph.triples((concept, SKOS.altLabel, None)):
                if o == pref_labels[s]:
                    graph.remove((s, v, o))

        # Remove notation if they are copies of pref labels
        for concept in concept_uris:
            pref_labels = {
                concept: str(o) for s, v, o in graph.triples((concept, SKOS.prefLabel, None))
            }
            for s, v, o in graph.triples((concept, SKOS.notation, None)):
                if str(o) == pref_labels[s]:
                    graph.remove((s, v, o))

        # for s, v, o in graph.triples((URIRef("https://vocab.sentier.dev/units/unit/OHM"), SKOS.notation, None)):
        #     print(o)

        return graph

    def add_concept_scheme(self) -> URIRef:
        schema_graph = self.get_graph_for_file("schema/SCHEMA_QUDT.ttl")
        ontology, _, _ = get_one_in_graph(
            schema_graph, ((None, RDF.type, OWL.Ontology))
        )
        _, _, graph_metdata_node = get_one_in_graph(
            schema_graph, (ontology, VAEM["#hasGraphMetadata"], None)
        )
        _, _, title = get_one_in_graph(
            schema_graph, (graph_metdata_node, DCTERMS.title, None)
        )
        version = str(title).split("Version")[-1].strip()

        DIRECT_COPIES = (DCTERMS.created,)

        self.add((self.cs_uri, RDF.type, SKOS.ConceptScheme))
        self.add(
            (
                self.cs_uri,
                SKOS.prefLabel,
                self.as_language_aware_literal(
                    Literal(f"Units Concept Scheme based on QUDT version {version}")
                ),
            )
        )
        self.add(
            (
                self.cs_uri,
                DCTERMS.creator,
                URIRef("https://www.linkedin.com/in/ralphhodgson/"),
            )
        )
        self.add((self.cs_uri, OWL.versionInfo, Literal(version)))

        _, _, description = get_one_in_graph(
            schema_graph, (graph_metdata_node, DCTERMS.description, None)
        )
        description = clean(description)
        self.add(
            (
                self.cs_uri,
                SKOS.definition,
                self.as_language_aware_literal(Literal(description)),
            )
        )

        for s, p, o in schema_graph.triples((graph_metdata_node, None, None)):
            if p in DIRECT_COPIES:
                self.add((self.cs_uri, p, o))

        self.add(
            (
                self.cs_uri,
                URIRef("http://purl.org/ontology/bibo/status"),
                URIRef("http://purl.org/ontology/bibo/status/accepted"),
            )
        )

        return self.cs_uri

    def as_language_aware_literal(
        self, obj: Literal, en_title: bool = False
    ) -> Literal:
        if not obj.language:
            if en_title and self.default_lang.lower().startswith("en"):
                return Literal(str(obj).title(), lang=self.default_lang)
            else:
                return Literal(str(obj), lang=self.default_lang)
        else:
            if en_title and obj.language.lower().startswith("en"):
                return Literal(str(obj).title(), lang=obj.language)
            else:
                return obj

    def get_identifier(self, uri: URIRef) -> str:
        return uri.split("/")[-1]

    def deprecated(self, graph: Graph, key: URIRef) -> bool:
        return any(graph.triples((key, DCTERMS.isReplacedBy, None)))

    def check_that_deprecated_have_replaced_by(self, graph: Graph, kind: str) -> bool:
        # Note that it doesn't work the other way...
        replaced = {
            s
            for s, p, o in graph.triples((None, DCTERMS.isReplacedBy, None))
            if s.startswith(kind)
        }
        deprecated = {
            s
            for s, p, o in graph.triples((None, QUDTS.deprecated, None))
            if s.startswith(kind)
        }
        return deprecated.difference(replaced)

    def add_labels_handle_missing_language(
        self,
        graph: Graph,
        search_uri: URIRef,
        target_uri: URIRef,
        search_term: URIRef = RDFS.label,
        target_term: URIRef = SKOS.prefLabel,
    ) -> None:
        """Iterate over all `RDFS.label` triples for `uri`, and adds then as `SKOS.prefLabel`

        Handles labels without a language field by checking if the default language field is also
        provided as a separate label."""
        has_default_language = any(
            1
            for s, p, o in graph.triples((search_uri, search_term, None))
            if o.language == self.default_lang
        )
        for s, p, o in graph.triples((search_uri, search_term, None)):
            if not o.language and has_default_language:
                continue
            elif not o.language:
                self.add((target_uri, target_term, self.as_language_aware_literal(o)))
            else:
                self.add((target_uri, target_term, to_untyped_literal(o)))

    def add_quantity_kinds(self, cs: URIRef) -> dict[URIRef, URIRef]:
        qk_graph = self.get_graph_for_file(
            "vocab/quantitykinds/VOCAB_QUDT-QUANTITY-KINDS-ALL.ttl"
        )
        # No longer true as of version 3.1.6
        # assert not self.check_that_deprecated_have_replaced_by(qk_graph, QK)

        qk_mapping = {
            s: URIRef(
                "https://vocab.sentier.dev/units/quantity-kind/"
                + self.get_identifier(s)
            )
            for s, p, o in qk_graph
            if URIRef(s) in self.selected_qk
            and s.startswith(QK)
            and not any(qk_graph.triples((s, DCTERMS.isReplacedBy, None)))
            and not any(qk_graph.triples((s, QUDTS.deprecated, None)))
        }

        for key_uri, value_uri in qk_mapping.items():
            self.add((value_uri, RDF.type, SKOS.Concept))
            self.add((value_uri, SKOS.inScheme, cs))
            self.add((value_uri, SKOS.topConceptOf, cs))
            self.add((value_uri, SKOS.exactMatch, key_uri))
            try:
                    self.add(
                    (
                        value_uri,
                        QUDTS.hasDimensionVector,
                        get_one_in_graph(
                            qk_graph, (key_uri, QUDTS.hasDimensionVector, None)
                        )[2],
                    )
                )
            except GraphFilterError:
                logger.debug(f"No dimension vector given for quantity kind {value_uri}")
            for s, v, o in qk_graph.triples((key_uri, SKOS.broader, None)):
                if o in self.selected_qk:
                    self.add((qk_mapping[s], SKOS.broader, qk_mapping[o]))

            self.add_labels_handle_missing_language(
                graph=qk_graph,
                search_uri=key_uri,
                target_uri=value_uri,
            )
            self.add_labels_handle_missing_language(
                graph=qk_graph,
                search_uri=key_uri,
                target_uri=value_uri,
                search_term=DCTERMS.description,
                target_term=SKOS.definition,
            )
            self.add_labels_handle_missing_language(
                graph=qk_graph,
                search_uri=key_uri,
                target_uri=value_uri,
                search_term=RDFS.comment,
                target_term=SKOS.note,
            )

            unmodified_verb_mapping = {
                QUDTS.symbol: SKOS.notation,
                QUDTS.dbpediaMatch: SKOS.related,
                QUDTS.iec61360Code: SKOS.notation,
                QUDTS.informativeReference: QUDTS.informativeReference,
                QUDTS.isoNormativeReference: QUDTS.isoNormativeReference,
                QUDTS.latexDefinition: QUDTS.latexDefinition,
                QUDTS.latexSymbol: QUDTS.latexSymbol,
                QUDTS.siExactMatch: SKOS.exactMatch,

                # QUDTS.plainTextDescription: SKOS.note,

                RDFS.seeAlso: SKOS.related,
            }

            for s, v, o in qk_graph.triples((key_uri, None, None)):
                try:
                    self.add((value_uri, unmodified_verb_mapping[v], o))
                except KeyError:
                    pass

            self.add(
                (
                    value_uri,
                    URIRef("http://purl.org/ontology/bibo/status"),
                    URIRef("http://purl.org/ontology/bibo/status/accepted"),
                )
            )

        return qk_mapping

    def check_all_units_have_vector(self, graph: Graph) -> None:
        all_units = {
            s
            for s, p, o in graph.triples((None, None, None))
            if s.startswith(QUDTV.unit)
        }
        with_dimension_vector = {
            s
            for s, p, o in graph.triples((None, QUDTS.hasDimensionVector, None))
            if s.startswith(QUDTV.unit)
        }
        if all_units.difference(with_dimension_vector):
            raise MissingDimensionVector

    @lru_cache(maxsize=1024)
    def is_unitary(self, graph: Graph, uri: URIRef) -> bool:
        try:
            return (
                float(
                    get_one_in_graph(graph, ((uri, QUDTS.conversionMultiplier, None)))[
                        2
                    ]
                )
                == 1.0
            )
        except GraphFilterError:
            logger.trace("No conversion multiplier for {u}", u=uri)
            return False

    # def fill_missing_attributes(self) -> None:
    #     """Our custom concepts can be narrower than an existing QUDT unit. In these cases, we don't
    #     copy over all the additional data from the "parent" concept, but add it automatically.
    #     """
    #     all_units = {
    #         s
    #         for s, _, _ in self.graph.triples((None, RDF.type, SKOS.Concept))
    #         if s.startswith("https://vocab.sentier.dev/units/unit")
    #     }
    #     qk_mapping = {
    #         s: o
    #         for s, _, o in self.graph.triples((None, QUDTS.hasQuantityKind, None))
    #         if s in all_units
    #     }
    #     for uri in all_units.difference(set(qk_mapping)):
    #         possibles = [
    #             o
    #             for s, v, o in self.graph.triples((uri, SKOS.broader, None))
    #             if o.startswith("https://vocab.sentier.dev/units/unit")
    #         ]
    #         if not len(possibles) == 1:
    #             raise ValueError(f"Can't find broader match for concept {uri}")
    #         self.add((uri, QUDTS.hasQuantityKind, qk_mapping[possibles[0]]))

    def our_concept_uri(self, uri: URIRef) -> URIRef:
        return URIRef(
            "https://vocab.sentier.dev/units/unit" + str(uri).replace(QUDTV.unit, "")
        )

    def all_concept_uris(self, graph: Graph, only_these_qks: set) -> Generator:
        for s, p, o in graph.triples((None, QUDTS.hasQuantityKind, None)):
            if (
                o in self.selected_qk
                and not any(graph.triples((s, QUDTS.deprecated, None)))
                and any(graph.triples((s, QUDTS.hasDimensionVector, None)))
            ):
                yield s

    def add_units(self, cs: URIRef, qk_mapping: dict[URIRef, URIRef]) -> None:
        unit_graph = self.get_graph_for_file("vocab/unit/VOCAB_QUDT-UNITS-ALL.ttl")
        for triple in Graph().parse(qudt_patches_data):
            unit_graph.add(triple)
        # Not true as of 3.1.6
        # self.check_all_units_have_vector(unit_graph)

        unit_mapping = {
            s: self.our_concept_uri(s)
            for s in self.all_concept_uris(unit_graph, set(qk_mapping))
        }

        top_level = {
            key: vsd_uri
            for key, value in self.selected_qk.items()
            for qudt_uri, vsd_uri in unit_mapping.items()
            if self.get_identifier(qudt_uri) == value
        }

        for key_uri, value_uri in unit_mapping.items():
            self.add_unit(uri=value_uri, unit_graph=unit_graph, cs=cs, qudt_uri=key_uri)

            for _, _, quantity_kind in unit_graph.triples(
                (key_uri, QUDTS.hasQuantityKind, None)
            ):
                if quantity_kind not in top_level:
                    continue
                if value_uri in top_level.values():
                    self.add((value_uri, SKOS.broader, qk_mapping[quantity_kind]))
                    self.add(
                        (value_uri, QUDTS.hasQuantityKind, qk_mapping[quantity_kind])
                    )
                else:
                    self.add((value_uri, SKOS.broader, top_level[quantity_kind]))
                    self.add(
                        (value_uri, QUDTS.hasQuantityKind, qk_mapping[quantity_kind])
                    )
        self.concept_uris = set(unit_mapping.values())

    def add_unit(
        self, uri: URIRef, unit_graph: Graph, cs: URIRef, qudt_uri: URIRef
    ) -> None:
        self.add((uri, RDF.type, SKOS.Concept))
        self.add((uri, SKOS.inScheme, cs))
        self.add((uri, SKOS.exactMatch, qudt_uri))
        try:
            self.add(
                (
                    uri,
                    QUDTS.hasDimensionVector,
                    get_one_in_graph(
                        unit_graph, (qudt_uri, QUDTS.hasDimensionVector, None)
                    )[2],
                )
            )
        except GraphFilterError:
            logger.debug(f"No dimension vector given for unit {uri}")

        for s, v, o in unit_graph.triples((qudt_uri, RDFS.label, None)):
            self.add((uri, SKOS.prefLabel, self.as_language_aware_literal(o)))

        self.add_labels_handle_missing_language(
            graph=unit_graph,
            search_uri=qudt_uri,
            target_uri=uri,
            search_term=DCTERMS.description,
            target_term=SKOS.definition,
        )

        verb_mapping = {
            QUDTS.plainTextDescription: SKOS.note,
            QUDTS.conversionMultiplier: QUDTS.conversionMultiplier,
            QUDTS.conversionMultiplierSN: QUDTS.conversionMultiplierSN,
            QUDTS.symbol: SKOS.notation,
            QUDTS.dbpediaMatch: SKOS.related,
            QUDTS.iec61360Code: SKOS.notation,
            QUDTS.uneceCommonCode: SKOS.notation,
            QUDTS.ucumCode: SKOS.notation,
            QUDTS.uneceCommonCode: SKOS.notation,
            QUDTS.informativeReference: QUDTS.informativeReference,
            QUDTS.isoNormativeReference: QUDTS.isoNormativeReference,
            QUDTS.latexDefinition: QUDTS.latexDefinition,
            QUDTS.latexSymbol: QUDTS.latexSymbol,
            QUDTS.siExactMatch: SKOS.exactMatch,
            RDFS.comment: SKOS.note,
            QUDTS.plainTextDescription: SKOS.note,
            RDFS.seeAlso: SKOS.related,
            QUDTS.applicableSystem: QUDTS.applicableSystem,
        }
        own_type = {
            QUDTS.symbol,
            QUDTS.iec61360Code,
            QUDTS.uneceCommonCode,
            QUDTS.ucumCode,
            QUDTS.uneceCommonCode,
        }

        for s, v, o in unit_graph.triples((qudt_uri, None, None)):
            try:
                verb = verb_mapping[v]
                if v in own_type:
                    self.add((uri, verb, Literal(o, datatype=v)))
                else:
                    self.add((uri, verb, o))
            except KeyError:
                pass

        self.add(
            (
                uri,
                URIRef("http://purl.org/ontology/bibo/status"),
                URIRef("http://purl.org/ontology/bibo/status/accepted"),
            )
        )

    def expanded_separate_json_ld_graph(self, kind: URIRef, graph: Graph) -> bytes:
        """Take {a related (b, c)} and turn into {a related b}, {a related c}"""
        out = BytesIO()
        graph.serialize(out, format="json-ld", encoding="utf-8")
        out.seek(0)
        orig = orjson.loads(out.read())
        data = []
        for obj in orig:
            for child in obj[str(kind)]:
                data.append(orjson.dumps([{"@id": obj["@id"], str(kind): [child]}]))
        return data

    def expanded_json_ld_graph(
        self, graph: Graph, single_elements: bool = True
    ) -> bytes:
        out = BytesIO()
        graph.serialize(out, format="json-ld", encoding="utf-8")
        out.seek(0)
        if single_elements:
            # Transform from bytes with list to list of bytes (say that twice :)
            return [orjson.dumps(obj) for obj in orjson.loads(out.read())]
        else:
            return out.read()


# def add_quantity_kinds_to_graph(
#     input_ttl: Path,
#     qudt_ttl: Path,
# ) -> Path:
#     """
#     The `input_ttl` concept scheme was written by hand (!), but we can make it more useful by
#     positioning each input concept in the QUDT quantity kind hierarchy.
#     """
#     output_ttl = (
#         Path(__file__).parent
#         / "output"
#         / Path(str(input_ttl.stem) + ".supplemented" + str(input_ttl.suffix))
#     )

#     input_graph = Graph().parse(input_ttl)
#     qudt = Graph().parse(qudt_ttl)

#     qudt_qk_mapping = {
#         s: o
#         for s, v, o in qudt.triples((None, QUDTS.hasQuantityKind, None))
#         if o.startswith("https://vocab.sentier.dev/units/quantity-kind/")
#         and s.startswith("https://vocab.sentier.dev/units/unit/")
#     }
#     qudt_d_mapping = {
#         s: o
#         for s, v, o in qudt.triples((None, QUDTS.hasDimensionVector, None))
#         if o.startswith("http://qudt.org/vocab/dimensionvector/")
#         and s.startswith("https://vocab.sentier.dev/units/unit/")
#     }

#     for s, v, o in input_graph.triples((None, SKOS.exactMatch, None)):
#         if o.startswith("https://vocab.sentier.dev/units/unit/"):
#             input_graph.add((s, QUDTS.hasQuantityKind, qudt_qk_mapping[o]))
#             input_graph.add((s, QUDTS.hasDimensionVector, qudt_d_mapping[o]))

#     logger.info(f"Writing {output_ttl}")
#     input_graph.serialize(destination=output_ttl)
#     return output_ttl


# if __name__ == "__main__":
#     QUDT().write_graph()
#     add_quantity_kinds_to_graph(
#         Path(__file__).parent / "input" / "simapro.ttl",
#         Path(__file__).parent / "output" / "qudt-sentier-dev.ttl",
#     )

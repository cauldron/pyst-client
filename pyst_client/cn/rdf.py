from io import BytesIO
from pathlib import Path

import orjson
import skosify
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, SKOS

XKOS = Namespace("http://rdf-vocabulary.ddialliance.org/xkos#")

CS_TO_DROP = {
    DCTERMS.language,
    SKOS.hasTopConcept,
}
CS_MAPPING = {
    DCTERMS.description: SKOS.definition,
}
CONCEPT_TO_DROP = {
    SKOS.broaderTransitive,
    SKOS.narrowerTransitive,
    SKOS.broader,
    SKOS.narrower,
    SKOS.notation,
}
CORRESPONDENCE_MAPPING = {
    DCTERMS.description: SKOS.definition,
}


class CombinedNomenclature:
    def __init__(self, filepath: Path | BytesIO, year: int):
        # logger.info("Reading input RDF file {}", filepath.absolute())
        self.graph = Graph().parse(filepath, format="xml")
        self.year = year

        skosify.infer.skos_hierarchical(self.graph, narrower=True)
        skosify.infer.skos_transitive(self.graph, narrower=True)

    @property
    def cs_uri(self) -> URIRef:
        return URIRef(f"http://data.europa.eu/xsp/cn{self.year}/cn{self.year}")

    def concept_scheme(self, as_bytes: bool = True) -> Graph:
        graph = Graph()

        for subj, verb, obj in self.graph.triples((self.cs_uri, None, None)):
            if verb in CS_TO_DROP:
                continue
            elif verb in CS_MAPPING:
                graph.add((subj, CS_MAPPING[verb], obj))
            else:
                graph.add((subj, verb, obj))

        graph.add(
            (
                self.cs_uri,
                URIRef("http://purl.org/ontology/bibo/status"),
                URIRef("http://purl.org/ontology/bibo/status/accepted"),
            )
        )

        return graph

    def _sample_concept_uris(self) -> set[URIRef]:
        # Two smallest trees in CN; used to create sample instead of full dataset
        art = URIRef(f"http://data.europa.eu/xsp/cn{self.year}/970011000090")
        arms = URIRef(f"http://data.europa.eu/xsp/cn{self.year}/930011000090")
        concept_uris = {o for s, v, o in self.graph.triples((art, SKOS.narrowerTransitive, None))}
        concept_uris.update(
            {o for s, v, o in self.graph.triples((arms, SKOS.narrowerTransitive, None))}
        )
        concept_uris.update({art, arms})
        return concept_uris

    def _concept_uris(
        self,
    ) -> set[URIRef]:
        return {s for s, v, o in self.graph.triples((None, SKOS.inScheme, self.cs_uri))}

    def concepts(self, sample: bool = False) -> Graph:
        graph = Graph()

        if sample:
            concept_uris = self._sample_concept_uris()
        else:
            concept_uris = self._concept_uris(self.cs_uri)

        for subj, verb, obj in self.graph.triples((None, None, None)):
            if subj not in concept_uris:
                continue
            if verb in CONCEPT_TO_DROP:
                continue
            elif verb == DCTERMS.identifier:
                # This is a weird one - they give a short form as notation and the longer full form
                # as identifier. This doesn't seem correct so we change it.
                graph.add((subj, SKOS.notation, Literal(str(obj), datatype=RDF.PlainLiteral)))
            else:
                graph.add((subj, verb, obj))

        for concept in concept_uris:
            graph.add(
                (
                    concept,
                    URIRef("http://purl.org/ontology/bibo/status"),
                    URIRef("http://purl.org/ontology/bibo/status/accepted"),
                )
            )

        # Remove alt labels if they are copies of pref labels
        for concept in concept_uris:
            pref_labels = {concept: o for s, v, o in graph.triples((concept, SKOS.prefLabel, None))}
            for s, v, o in graph.triples((concept, SKOS.altLabel, None)):
                if o == pref_labels[s]:
                    graph.remove((s, v, o))
                    break

        return graph

    def relationships(self, kind: URIRef, sample: bool = False) -> Graph:
        graph = Graph()

        if sample:
            concept_uris = self._sample_concept_uris()
        else:
            concept_uris = self._concept_uris(self.cs_uri)

        for subj, verb, obj in self.graph.triples((None, kind, None)):
            if subj not in concept_uris:
                continue
            graph.add((subj, verb, obj))

        return graph

    def correspondences(self) -> list[URIRef]:
        return {s for s, v, o in self.graph.triples((None, RDF.type, XKOS.Correspondence))}

    def correspondence(self, uri: URIRef, sample: bool = False) -> Graph:
        graph = Graph()

        for s, v, o in self.graph.triples((uri, None, None)):
            if v in CORRESPONDENCE_MAPPING:
                graph.add((s, CORRESPONDENCE_MAPPING[v], o))
            elif v == XKOS.madeOf:
                continue
            else:
                graph.add((s, v, o))

        # Add missing required attributes
        for s, v, o in self.graph.triples((self.cs_uri, OWL.versionInfo, None)):
            graph.add((uri, OWL.versionInfo, o))
            break

        if not any(graph.triples((uri, DCTERMS.created, None))):
            for s, v, o in self.graph.triples((uri, DCTERMS.modified, None)):
                graph.add((uri, DCTERMS.created, o))
                break

        if not any(graph.triples((uri, DCTERMS.creator, None))):
            for s, v, o in self.graph.triples((self.cs_uri, DCTERMS.creator, None)):
                graph.add((uri, DCTERMS.creator, o))
                break

        graph.add(
            (
                uri,
                URIRef("http://purl.org/ontology/bibo/status"),
                URIRef("http://purl.org/ontology/bibo/status/accepted"),
            )
        )

        return graph

    def made_of(self, uri: URIRef, sample: bool = False) -> Graph:
        graph = Graph()

        for s, v, o in self.graph.triples((uri, XKOS.madeOf, None)):
            graph.add((s, v, o))

        return graph

    def associations(self, uri: URIRef, sample: bool = False) -> list[Graph]:
        graphs = {}

        association_uris_in_correspondence = {
            o for s, v, o in self.graph.triples((uri, XKOS.madeOf, None))
        }

        if sample:
            concept_uris = self._sample_concept_uris()
            selected_association_uris_in_correspondence = {
                s
                for s, v, o in self.graph.triples((None, XKOS.sourceConcept, None))
                if o in concept_uris and s in association_uris_in_correspondence
            }
            for s, v, o in self.graph.triples((None, None, None)):
                if s in selected_association_uris_in_correspondence:
                    if s not in graphs:
                        graphs[s] = Graph()
                    graphs[s].add((s, v, o))
        else:
            for s, v, o in self.graph.triples((None, None, None)):
                if s in association_uris_in_correspondence:
                    if s not in graphs:
                        graphs[s] = Graph()
                    graphs[s].add((s, v, o))

        return graphs

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

    def expanded_json_ld_graph(self, graph: Graph, single_elements: bool = True) -> bytes:
        out = BytesIO()
        graph.serialize(out, format="json-ld", encoding="utf-8")
        out.seek(0)
        if single_elements:
            # Transform from bytes with list to list of bytes (say that twice :)
            return [orjson.dumps(obj) for obj in orjson.loads(out.read())]
        else:
            return out.read()

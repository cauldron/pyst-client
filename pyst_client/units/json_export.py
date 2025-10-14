import orjson
from bs4 import BeautifulSoup

from pyst_client.units.rdf import QUDT, QUDTS, RDF, SKOS, URIRef

q = QUDT()

qk_data = {}
qk = {s for s, p, o in q.graph.triples((None, SKOS.topConceptOf, None))}

for qk_uri in qk:
    qk_data[qk_uri] = {"iri": qk_uri}
    for s, p, o in q.graph.triples((qk_uri, None, None)):
        if p == SKOS.prefLabel and (not o.language or o.language == q.default_lang):
            qk_data[qk_uri]["label"] = str(o)
        elif p == SKOS.definition:
            qk_data[qk_uri]["definition"] = (
                BeautifulSoup(str(o), "html.parser").get_text().strip()
            )
        elif p == QUDTS.hasDimensionVector:
            qk_data[qk_uri]["dimension_vector"] = str(o)
        elif p == SKOS.note:
            qk_data[qk_uri]["note"] = str(o)


units_data = {}
units = {s for s, p, o in q.graph.triples((None, RDF.type, SKOS.Concept))}

for unit_uri in units:
    units_data[unit_uri] = {"iri": unit_uri}
    for s, p, o in q.graph.triples((unit_uri, None, None)):
        if p == SKOS.prefLabel and (not o.language or o.language == q.default_lang):
            units_data[unit_uri]["label"] = str(o)
        elif p == SKOS.notation:
            units_data[unit_uri]["notation"] = str(o)
        elif p == QUDTS.hasQuantityKind:
            units_data[unit_uri]["quantity_kind_iri"] = str(o)
        elif p == SKOS.broader and o in units:
            units_data[unit_uri]["reference_unit_iri"] = str(o)
        elif p == SKOS.definition:
            units_data[unit_uri]["definition"] = (
                BeautifulSoup(str(o), "html.parser").get_text().strip()
            )
        elif p == QUDTS.conversionMultiplier:
            units_data[unit_uri]["conversion_multiplier"] = float(o)


with open("quantity-kinds.json", "wb") as f:
    f.write(orjson.dumps(list(qk_data.values()), option=orjson.OPT_INDENT_2))

with open("units.json", "wb") as f:
    f.write(orjson.dumps(list(units_data.values()), option=orjson.OPT_INDENT_2))

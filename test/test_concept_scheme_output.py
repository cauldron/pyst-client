# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyst_client.models.concept_scheme_output import ConceptSchemeOutput

class TestConceptSchemeOutput(unittest.TestCase):
    """ConceptSchemeOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConceptSchemeOutput:
        """Test ConceptSchemeOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConceptSchemeOutput`
        """
        model = ConceptSchemeOutput()
        if include_optional:
            return ConceptSchemeOutput(
                id = 'http://data.europa.eu/xsp/cn2024/010021000090',
                type = [http://www.w3.org/2004/02/skos/core#Concept],
                http___www_w3_org_2004_02_skos_corepref_label = [{@language=en, @value=CHAPTER 1 - LIVE ANIMALS}, {@language=pt, @value=CAPÍTULO 1 - ANIMAIS VIVOS}],
                http___purl_org_ontology_bibo_status = [{@id=http://purl.org/ontology/bibo/status/accepted}],
                http___www_w3_org_2004_02_skos_coredefinition = [{@language=en, @value=Includes all sorts of live animals, including things you probably never heard of before, like psittaciformes. Those are birds like parrots, by the way. Also includes silly names like hinnies and asses, but not those kinds of asses, get your mind out of the gutter. We are very serious people doing very serious work with our asses.}],
                http___www_w3_org_2004_02_skos_corenotation = [{@type=http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral, @value=01}],
                http___www_w3_org_2004_02_skos_corechange_note = [{http://purl.org/dc/terms/creator=[{@id=http://example.com/john.doe}], http://purl.org/dc/terms/issued=[{@type=http://www.w3.org/2001/XMLSchema#date, @value=1999-01-23}], http://www.w3.org/1999/02/22-rdf-syntax-ns#value=[{@language=en, @value=Moved from under 'fruits' to under 'vegetables'}]}],
                http___www_w3_org_2004_02_skos_corehistory_note = [{http://purl.org/dc/terms/creator=[{@id=http://example.com/jane.doe}], http://purl.org/dc/terms/issued=[{@type=http://www.w3.org/2001/XMLSchema#date, @value=1971-01-23}], http://www.w3.org/1999/02/22-rdf-syntax-ns#value=[{@language=en, @value=Previously thought we were talking about horseradish}]}],
                http___www_w3_org_2004_02_skos_coreeditorial_note = [{http://purl.org/dc/terms/creator=[{@id=http://example.com/jane.doe}], http://purl.org/dc/terms/issued=[{@type=http://www.w3.org/2001/XMLSchema#date, @value=2012-01-23}], http://www.w3.org/1999/02/22-rdf-syntax-ns#value=[{@language=en, @value=Check if this includes species outside Animalia}]}],
                http___purl_org_dc_terms_created = [{@type=http://www.w3.org/2001/XMLSchema#dateTime, @value=2023-10-11T13:59:56}],
                http___purl_org_dc_terms_creator = [{@id=http://publications.europa.eu/resource/authority/corporate-body/ESTAT}],
                http___www_w3_org_2002_07_owlversion_info = [{@value=2024}]
            )
        else:
            return ConceptSchemeOutput(
                id = 'http://data.europa.eu/xsp/cn2024/010021000090',
                type = [http://www.w3.org/2004/02/skos/core#Concept],
                http___www_w3_org_2004_02_skos_corepref_label = [{@language=en, @value=CHAPTER 1 - LIVE ANIMALS}, {@language=pt, @value=CAPÍTULO 1 - ANIMAIS VIVOS}],
                http___purl_org_ontology_bibo_status = [{@id=http://purl.org/ontology/bibo/status/accepted}],
                http___purl_org_dc_terms_created = [{@type=http://www.w3.org/2001/XMLSchema#dateTime, @value=2023-10-11T13:59:56}],
                http___purl_org_dc_terms_creator = [{@id=http://publications.europa.eu/resource/authority/corporate-body/ESTAT}],
                http___www_w3_org_2002_07_owlversion_info = [{@value=2024}],
        )
        """

    def testConceptSchemeOutput(self):
        """Test ConceptSchemeOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

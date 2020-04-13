################################################################################
#
#  Copyright (C) 2020 Aclima, Inc
#  This file is part of aclima-schema - https://github.com/Aclima/aclima-schema
#
#  SPDX-License-Identifier: MIT
#  See DOCS/LICENSING.md for more information.
#
################################################################################

from sosa.ontology.ontology_factory import OntologyFactory
from sosa.feature import FeatureOfInterest
from sosa.feature import Property

import unittest


class OntologyFactoryTest(unittest.TestCase):
    def test_get_instance(self) -> None:
        factory = OntologyFactory._get_instance()

        self.assertTrue(factory)

    def test_get_feature_of_interest(self) -> None:
        feature = OntologyFactory.get_feature_of_interest('http://aclima.io/schema/1.0/NitricOxide')

        self.assertTrue(isinstance(feature, FeatureOfInterest))
        # TODO: Load from test repo file
        #self.assertEqual('http://www.w3.org/ns/sosa/FeatureOfInterest', feature.type_iri)
        #self.assertEqual('Nitric oxide', feature.label)
        #self.assertEqual('Nitrogen oxide or nitrogen monoxide', feature.description)
        #self.assertEqual('NO', feature.abbreviation)

    def test_get_property(self) -> None:
        prop = OntologyFactory.get_property('http://aclima.io/schema/1.0/RawAverage')

        self.assertTrue(isinstance(prop, Property))
        # TODO: Load from test repo file
        #self.assertEqual('http://www.w3.org/ns/sosa/FeatureOfInterest', modality.type_iri)
        #self.assertEqual('Nitric oxide', modality.label)
        #self.assertEqual('Nitrogen oxide or nitrogen monoxide', modality.description)
        #self.assertEqual('NO', modality.abbreviation)


if __name__ == '__main__':
    unittest.main()

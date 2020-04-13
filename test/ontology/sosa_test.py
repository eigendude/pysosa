################################################################################
#
#  Copyright (C) 2019-2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from sosa.ontology.sosa import SOSA

import unittest


class SOSATest(unittest.TestCase):
    def test_namespace(self):
        self.assertEqual(SOSA.namespace, 'http://www.w3.org/ns/sosa/')

    def test_axioms(self):
        self.assertEqual(SOSA.OBSERVABLE_PROPERTY, 'http://www.w3.org/ns/sosa/ObservableProperty')
        self.assertEqual(SOSA.OBSERVATION, 'http://www.w3.org/ns/sosa/Observation')
        self.assertEqual(SOSA.SENSOR, 'http://www.w3.org/ns/sosa/Sensor')
        self.assertEqual(SOSA.ACTUATABLE_PROPERTY, 'http://www.w3.org/ns/sosa/ActuatableProperty')
        self.assertEqual(SOSA.ACTUATION, 'http://www.w3.org/ns/sosa/Actuation')
        self.assertEqual(SOSA.ACTUATOR, 'http://www.w3.org/ns/sosa/Actuator')
        self.assertEqual(SOSA.SAMPLE, 'http://www.w3.org/ns/sosa/Sample')
        self.assertEqual(SOSA.SAMPLING, 'http://www.w3.org/ns/sosa/Sampling')
        self.assertEqual(SOSA.SAMPLER, 'http://www.w3.org/ns/sosa/Sampler')
        self.assertEqual(SOSA.FEATURE_OF_INTEREST, 'http://www.w3.org/ns/sosa/FeatureOfInterest')
        self.assertEqual(SOSA.RESULT, 'http://www.w3.org/ns/sosa/Result')
        self.assertEqual(SOSA.PROCEDURE, 'http://www.w3.org/ns/sosa/Procedure')
        self.assertEqual(SOSA.PLATFORM, 'http://www.w3.org/ns/sosa/Platform')


if __name__ == '__main__':
    unittest.main()

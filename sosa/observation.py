################################################################################
#
#  Copyright (C) 2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

"""
Axiomatization of the core classes and properties that are specifically related
to modeling Observations.

This module introduces the following classes:

  * ObservableProperty
  * Observation
  * Sensor

Reference:

    https://www.w3.org/TR/vocab-ssn/#Observations

"""

from sosa.ontology.sosa import SOSA

import dataclasses


@dataclasses.dataclass
class ObservableProperty:
    """
    A property being observed.
    """

    resource_iri: str
    """
    The Internationalized Resource Identifier (IRI) for the object.
    """

    type_iri: str = dataclasses.field(default_factory=str)
    """
    The IRI for the object's Resource Description Framework (RDF) type.
    """

    label: str = dataclasses.field(default_factory=str)
    """
    A human-readable name for the resource in US English.
    """

    description: str = dataclasses.field(default_factory=str)
    """
    Additional information describing the resource in US English.
    """


@dataclasses.dataclass
class Observation:
    """
    An observation that occurred.
    """

    resource_iri: str
    """
    The Internationalized Resource Identifier (IRI) for the object.
    """

    type_iri: str = dataclasses.field(default_factory=str)
    """
    The IRI for the object's Resource Description Framework (RDF) type.
    """

    label: str = dataclasses.field(default_factory=str)
    """
    A human-readable name for the resource in US English.
    """

    description: str = dataclasses.field(default_factory=str)
    """
    Additional information describing the resource in US English.
    """


@dataclasses.dataclass
class Sensor:
    """
    A device performing an observation.
    """

    resource_iri: str
    """
    The Internationalized Resource Identifier (IRI) for the object.
    """

    type_iri: str = dataclasses.field(default_factory=str)
    """
    The IRI for the object's Resource Description Framework (RDF) type.
    """

    label: str = dataclasses.field(default_factory=str)
    """
    A human-readable name for the resource in US English.
    """

    description: str = dataclasses.field(default_factory=str)
    """
    Additional information describing the resource in US English.
    """

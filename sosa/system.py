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
to modeling systems and their deployment.

This module introduces the following classes:

  * Platform
  * System
  * Deployment

Reference:

    https://www.w3.org/TR/vocab-ssn/#Systems-and-their-Deployment

"""

from sosa.ontology.sosa import SOSA
from sosa.ontology.ssn import SSN

import dataclasses


@dataclasses.dataclass
class Platform:
    """
    A Platform is an entity that hosts other entities, particularly Sensors,
    Actuators, Samplers, and other Platforms.
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
class System:
    """
    A system is a unit of abstraction for pieces of infrastructure that
    implement Procedures.
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
class Deployment:
    """
    A deployment of one or more Systems for a particular purpose.
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

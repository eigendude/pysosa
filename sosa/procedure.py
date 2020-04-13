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
to modeling Procedures.

This module introduces the following classes:

  * Procedure
  * Input
  * Output

Reference:

    https://www.w3.org/TR/vocab-ssn/#Procedures

"""

from sosa.ontology.sosa import SOSA
from sosa.ontology.ssn import SSN

import dataclasses


@dataclasses.dataclass
class Procedure:
    """
    A workflow, protocol, plan, algorithm, or computational method specifying
    how to make an Observation, create a Sample, or make a change to the state
    of the world via an Actuator
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
class Input:
    """
    Any information that is provided to a Procedure for its use.
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
class Output:
    """
    Any information that is reported from a Procedure.
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

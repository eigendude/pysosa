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
Axiomatization of Features of Interest and their Properties.

This module introduces the following classes:

  * FeatureOfInterest
  * Property

Reference:

    https://www.w3.org/TR/vocab-ssn/#Features-of-Interest-and-Properties

"""

import dataclasses
from qudt.unit import Unit
from qudt.units.dimensionless import DimensionlessUnit


def create_unitless() -> Unit:
    """
    Helper function to create a unitless Unit object
    """
    return DimensionlessUnit.UNITLESS


@dataclasses.dataclass
class FeatureOfInterest:
    """
    A Feature of Interest being observed or actuated.
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

    abbreviation: str = dataclasses.field(default_factory=str)
    """
    A short abbreviation for the resource, used to shorten the string
    representation of the resource.
    """

    def __repr__(self) -> str:
        """
        Return a short string representation of the resource suitable for
        display.
        """
        return self.abbreviation if self.abbreviation else self.label


@dataclasses.dataclass
class Property:
    """
    A Property belonging to a Feature of Interest.
    """

    resource_iri: str
    """
    The Internationalized Resource Identifier (IRI) for the object.
    """

    type_iri: str = dataclasses.field(default_factory=str)
    """
    The IRI for the object's Resource Description Framework (RDF) type.

    The IRI will indicate if this is an Observable Property, Actuatable
    Property, or their superclass, a general Property.
    """

    label: str = dataclasses.field(default_factory=str)
    """
    A human-readable name for the resource in US English.
    """

    description: str = dataclasses.field(default_factory=str)
    """
    Additional information describing the resource in US English.
    """

    unit: Unit = dataclasses.field(default_factory=create_unitless)
    """
    The unit used to express an observation or actuation of the Property.
    """

    def __repr__(self) -> str:
        """
        Return a short string representation of the resource suitable for
        display.
        """
        return self.label

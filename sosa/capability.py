################################################################################
#
#  Copyright (C) 2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from sosa.ontology.ssn import SSN

import dataclasses


@dataclasses.dataclass
class Condition:
    """
    Used to specify ranges for qualities that act as Conditions on a System's
    operation.
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
class SystemCapability:
    """
    Describes normal measurement, actuation, sampling properties such as
    accuracy, range, precision, etc. of a System under some specified
    Conditions such as a temperature range.
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
class SystemProperty:
    """
    An identifiable and observable characteristic that represents the
    System's ability to operate its primary purpose.
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
class MeasurementRange:
    """
    The set of values that the Sensor can return as the Result of an
    Observation under the defined Conditions with the defined system
    properties.
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
class ActuationRange:
    """
    The range of Property values that can be the Result of an Actuation
    under the defined Conditions.
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
class Accuracy:
    """
    The closeness of agreement between the Result of an Observation
    (Actuation) and the true value of the observed ObservableProperty
    (ActuatableProperty) under the defined Conditions.
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
class DetectionLimit:
    """
    An observed value for which the probability of falsely claiming the
    absence of a component in a material is beta, given a probability alpha
    of falsely claiming its presence.
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
class Drift:
    """
    Drift can mean:

        * As a Sensor Property:

            A continuous or incremental change in the reported values of
            Observations over time for an unchanging Property under the
            defined Conditions

        * As an Actuator Property:

            A continuous or incremental change in the true value of the
            acted on ActuatableProperty over time for an unchanging command
            under the defined Conditions

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
class Frequency:
    """
    The smallest possible time between one Observation, Actuation, or
    Sampling and the next, under the defined Conditions.
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
class Latency:
    """
    The time between a command for an Observation (Actuation) and the
    Sensor (Actuator) providing a Result (Actuation), under the defined
    Conditions.
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
class Precision:
    """
    Precision can mean:

        * As a sensor capability:

            The closeness of agreement between replicate Observations on an
            unchanged or similar quality value, under the defined Conditions.

        * As an actuator capability:

            The closeness of agreement between replicate Actuations for an
            unchanged or similar command, under the defined Conditions.

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
class Resolution:
    """
    Resolution can mean:

        * As a Sensor Property:

            The smallest difference in the value of a ObservableProperty
            being observed that would result in perceptably different
            values of Observation Results, under the defined Conditions.

        * As an Actuator Property:

            The smallest difference in the value of an Actuation command
            that would result in a value change of the ActuatableProperty
            being acted on, under the defined Conditions.

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
class ResponseTime:
    """
    Response time can mean:

        * As a Sensor Property:

            The time between a (step) change in the value of an observed
            ObservableProperty and a Sensor (possibly with specified error)
            'settling' on an observed value, under the defined Conditions.

        * As an Actuator Property:

            The time between a (step) change in the command of an Actuator
            and the 'settling' of the value of the acted on
            ActuatableProperty, under the defined Conditions.

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
class Selectivity:
    """
    Selectivity can mean:

        * As a Sensor Property:

            Selectivity is a Property of a Sensor whereby it provides
            observed values for one or more ObservableProperties such that
            the Result for each ObservableProperty are independent of other
            Properties in the FeatureOfInterest being investigated, under
            the defined Conditions.

        As an Actuator Property:

            Selectivity is a Property of an Actuator whereby it acts on one
            or more ActuatableProperties such as the Results for each
            ActuatableProperty are independent of other Properties in the
            FeatureOfInterest being acted on, under the defined Conditions.

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
class Sensitivity:
    """
    Sensitivity can mean:

        * As a Sensor Property:

            Sensitivity is the quotient of the change in a Result of
            Observations and the corresponding change in a value of an
            ObservableProperty being observed, under the defined Conditions.

        * As an Actuator Property:

            Sensitivity is the quotient of the change in a command of
            Actuation and the corresponding change in a value of an
            ActuatableProperty being acted on, under the defined Conditions.

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
class OperatingRange:
    """
    Describes normal OperatingProperties of a System under some specified
    Conditions.
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
class OperatingProperty:
    """
    An identifiable characteristic that represents how the System operates
    under the specified Conditions.
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
class MaintenanceSchedule:
    """
    Schedule of maintenance for a System in the specified Conditions.
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
class OperatingPowerRange:
    """
    Power range in which System is expected to operate in the specified
    Conditions.
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
class SurvivalRange:
    """
    Describes SurvivalProperties of a System under some specified
    Conditions.
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
class SurvivalProperty:
    """
    An identifiable characteristic that represents the extent of the
    System's useful life under the specified Conditions.
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
class SystemLifetime:
    """
    Total useful life of a System in the specified Conditions.
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
class BatteryLifetime:
    """
    Total useful life of a System's battery in the specified Conditions.
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

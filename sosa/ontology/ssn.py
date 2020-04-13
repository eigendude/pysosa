################################################################################
#
#  Copyright (C) 2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  This file is derived from the Semantic Sensor Network Ontology
#  Copyright (C) Open Geospatial Consortium (OGC)
#  Copyright (C) World Wide Web Consortium (W3C)
#
#  SPDX-License-Identifier: BSD-3-Clause AND W3C-20150513
#  See the file LICENSE for more information.
#
################################################################################

from qudt.ontology.ontology_utils import OntologyUtils


OntologyUtils.register_namespace('ssn', 'http://www.w3.org/ns/ssn/')
OntologyUtils.register_namespace('ssn-system', 'http://www.w3.org/ns/ssn/systems/')


class SSN:
    """
    The Semantic Sensor Network (SSN) ontology

    SSN is a web ontology published by the W3C for describing sensors and their
    observations, the involved procedures, the studied features of interest
    the samples used to do so, and the observed properties, as well as
    actuators.

    SSN follows a horizontal and vertical modularization architecture by
    including a lightweight but self-contained core ontology called SOSA
    (Sensor, Observation, Sample, and Actuator) for its elementary classes and
    properties.

    Reference:

        https://www.w3.org/TR/vocab-ssn/

    """

    namespace = OntologyUtils.get_namespace('ssn')

    ############################################################################
    # Axiomatization modules
    #
    # Feature classes:
    #
    #     * Property
    #
    # Procedure classes and properties:
    #
    #     * Input
    #     * Output
    #     * implements
    #     * isImplementedBy
    #     * hasInput
    #     * hasOutput
    #
    # System classes and properties:
    #
    #     * System
    #     * Deployment
    #     * hosts
    #     * isHostedBy
    #     * hasSubSystem
    #     * deployedSystem
    #     * hasDeployment
    #     * deployedOnPlatform
    #     * inDeployment
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Axiomatization
    #
    ############################################################################

    ############################################################################
    #
    # Feature module
    #
    ############################################################################

    PROPERTY = OntologyUtils.get_iri('ssn', 'Property')
    """
    A quality of an entity. An aspect of an entity that is intrinsic to and
    cannot exist without the entity.

    This is the super-class of ObservableProperty and ActuatableProperty.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNProperty

    """

    ############################################################################
    #
    # Procedure module
    #
    ############################################################################

    INPUT = OntologyUtils.get_iri('ssn', 'Input')
    """
    Any information that is provided to a Procedure for its use.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNInput

    """

    OUTPUT = OntologyUtils.get_iri('ssn', 'Output')
    """
    Any information that is reported from a Procedure.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNOutput

    """

    IMPLEMENTS = OntologyUtils.get_iri('ssn', 'implements')
    """
    Relation between an entity that implements a Procedure in some executable
    way and the Procedure (an algorithm, procedure or method).

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNimplements

    """

    IS_IMPLEMENTED_BY = OntologyUtils.get_iri('ssn', 'isImplementedBy')
    """
    Relation between a Procedure (an algorithm, procedure or method) and an
    entity that implements that Procedure in some executable way.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNimplementedBy

    """

    HAS_INPUT = OntologyUtils.get_iri('ssn', 'hasInput')
    """
    Relation between a Procedure and an Input to it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNhasInput

    """

    HAS_OUTPUT = OntologyUtils.get_iri('ssn', 'hasOutput')
    """
    Relation between a Procedure and an Output of it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNhasOutput

    """

    ############################################################################
    #
    # System module
    #
    ############################################################################

    SYSTEM = OntologyUtils.get_iri('ssn', 'System')
    """
    A system is a unit of abstraction for pieces of infrastructure that
    implement Procedures.

    A System may have components, its subsystems, which are other Systems.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSystem

    """

    DEPLOYMENT = OntologyUtils.get_iri('ssn', 'Deployment')
    """
    Describes the Deployment of one or more Systems for a particular purpose.

    Deployment may be done on a Platform.

    Examples:

        * Temperature Sensor deployed on a wall
        * A whole network of Sensors deployed for an Observation campaign

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNDeployment

    """

    HAS_SUBSYSTEM = OntologyUtils.get_iri('ssn', 'hasSubSystem')
    """
    Relation between a System and its component parts.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNhasSubSystem

    """

    DEPLOYED_SYSTEM = OntologyUtils.get_iri('ssn', 'deployedSystem')
    """
    Relation between a Deployment and a deployed System.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNdeployedSystem

    """

    HAS_DEPLOYMENT = OntologyUtils.get_iri('ssn', 'hasDeployment')
    """
    Relation between a System and a Deployment, recording that the System is
    deployed in that Deployment.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNhasDeployment

    """

    DEPLOYED_ON_PLATFORM = OntologyUtils.get_iri('ssn', 'deployedOnPlatform')
    """
    Relation between a Deployment and the Platform on which the Systems are
    deployed.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNdeployedOnPlatform

    """

    IN_DEPLOYMENT = OntologyUtils.get_iri('ssn', 'inDeployment')
    """
    Relation between a Platform and a Deployment, meaning that the
    deployedSystems of the Deployment are hosted on the Platform.

    Examples:

        * A relation between a buoy and a Deployment of several Sensors

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNinDeployment
    """

    ############################################################################
    # Horizontal segmentation modularization
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#HorizontalSegmentation
    #
    ############################################################################

    ############################################################################
    #
    # Capabilities of systems
    #
    ############################################################################

    CONDITION = OntologyUtils.get_iri('ssn-system', 'Condition')
    """
    Used to specify ranges for qualities that act as Conditions on a System's
    operation.

    Examples:

        * Wind speed of 10-60m/s may be used as the Condition on a
          SystemProperty to state that a Sensor has a particular Accuracy
          under that Condition

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMCondition

    """

    SYSTEM_CAPABILITY = OntologyUtils.get_iri('ssn-system', 'SystemCapability')
    """
    Describes normal measurement, actuation, sampling properties such as
    accuracy, range, precision, etc. of a System under some specified
    Conditions such as a temperature range.

    The capabilities specified here are those that affect the primary
    purpose of the System, while those in OperatingRange represent the
    system's normal operating environment, including Conditions that don't
    affect the Observations or the Actuations.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSystemCapability

    """

    SYSTEM_PROPERTY = OntologyUtils.get_iri('ssn-system', 'SystemProperty')
    """
    An identifiable and observable characteristic that represents the
    System's ability to operate its primary purpose:

        * A Sensor making Observations
        * An Actuator making Actuations
        * A Sampler that is Sampling

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSystemProperty

    """

    MEASUREMENT_RANGE = OntologyUtils.get_iri('ssn-system', 'MeasurementRange')
    """
    The set of values that the Sensor can return as the Result of an
    Observation under the defined Conditions with the defined system
    properties.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMMeasurementRange

    """

    ACTUATION_RANGE = OntologyUtils.get_iri('ssn-system', 'ActuationRange')
    """
    The range of Property values that can be the Result of an Actuation
    under the defined Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMActuationRange

    """

    ACCURACY = OntologyUtils.get_iri('ssn-system', 'Accuracy')
    """
    The closeness of agreement between the Result of an Observation
    (Actuation) and the true value of the observed ObservableProperty
    (ActuatableProperty) under the defined Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMAccuracy

    """

    DETECTION_LIMIT = OntologyUtils.get_iri('ssn-system', 'DetectionLimit')
    """
    An observed value for which the probability of falsely claiming the
    absence of a component in a material is beta, given a probability alpha
    of falsely claiming its presence.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMDetectionLimit

    """

    DRIFT = OntologyUtils.get_iri('ssn-system', 'Drift')
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

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMDrift

    """

    FREQUENCY = OntologyUtils.get_iri('ssn-system', 'Frequency')
    """
    The smallest possible time between one Observation, Actuation, or
    Sampling and the next, under the defined Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMFrequency

    """

    LATENCY = OntologyUtils.get_iri('ssn-system', 'Latency')
    """
    The time between a command for an Observation (Actuation) and the
    Sensor (Actuator) providing a Result (Actuation), under the defined
    Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMLatency

    """

    PRECISION = OntologyUtils.get_iri('ssn-system', 'Precision')
    """
    Precision can mean:

        * As a sensor capability:

            The closeness of agreement between replicate Observations on an
            unchanged or similar quality value, under the defined Conditions.

        * As an actuator capability:

            The closeness of agreement between replicate Actuations for an
            unchanged or similar command, under the defined Conditions.

    Examples:

        * A measure of a Sensor's ability to consistently reproduce an
          Observation
        * A measure of an Actuator's ability to consistently reproduce an
          Actuations

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMPrecision

    """

    RESOLUTION = OntologyUtils.get_iri('ssn-system', 'Resolution')
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

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMResolution

    """

    RESPONSE_TIME = OntologyUtils.get_iri('ssn-system', 'ResponseTime')
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

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMResponseTime

    """

    SELECTIVITY = OntologyUtils.get_iri('ssn-system', 'Selectivity')
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

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSelectivity

    """

    SENSITIVITY = OntologyUtils.get_iri('ssn-system', 'Sensitivity')
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

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSensitivity

    """

    OPERATING_RANGE = OntologyUtils.get_iri('ssn-system', 'OperatingRange')
    """
    Describes normal OperatingProperties of a System under some specified
    Conditions.

    In the absence of OperatingProperties, it simply describes the
    Conditions in which a System is expected to operate.

    The System continues to operate as defined using SystemCapability. If,
    however, the OperatingProperty is violated, the System is operating
    'out of operating range' and SystemCapability specifications may no
    longer hold.

    Examples:

        * The power requirements or maintenance schedule of a System under
          a specified temperature range.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMOperatingRange

    """

    OPERATING_PROPERTY = OntologyUtils.get_iri('ssn-system', 'OperatingProperty')
    """
    An identifiable characteristic that represents how the System operates
    under the specified Conditions.

    Examples:

        * Power ranges
        * Power sources
        * Standard configurations
        * Attachments

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMOperatingProperty

    """

    MAINTENANCE_SCHEDULE = OntologyUtils.get_iri('ssn-system', 'MaintenanceSchedule')
    """
    Schedule of maintenance for a System in the specified Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMMaintenanceSchedule

    """

    OPERATING_POWER_RANGE = OntologyUtils.get_iri('ssn-system', 'OperatingPowerRange')
    """
    Power range in which System is expected to operate in the specified
    Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMOperatingPowerRange

    """

    SURVIVAL_RANGE = OntologyUtils.get_iri('ssn-system', 'SurvivalRange')
    """
    Describes SurvivalProperties of a System under some specified
    Conditions.

    In the absence of SurvivalProperties, simply describes the Conditions a
    System can be exposed to without damage.

    The System continues to operate as defined using SystemCapability. If,
    however, the SurvivalRange is violated, the System is 'damaged' and
    SystemCapability specifications may no longer hold.

    Examples:

        * The lifetime of a System under a specified temperature range
        * The temperature range a System can withstand before being
          considered damaged

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSurvivalRange

    """

    SURVIVAL_PROPERTY = OntologyUtils.get_iri('ssn-system', 'SurvivalProperty')
    """
    An identifiable characteristic that represents the extent of the
    System's useful life under the specified Conditions.

    Examples:

        * Total battery life or number of recharges
        * The number of Observations that can be made before the sensing
          capability is depleted

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSurvivalProperty

    """

    SYSTEM_LIFETIME = OntologyUtils.get_iri('ssn-system', 'SystemLifetime')
    """
    Total useful life of a System in the specified Conditions.

    Examples:

        * Total life since manufacture
        * Time in use
        * Number of operations

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMSystemLifetime

    """

    BATTERY_LIFETIME = OntologyUtils.get_iri('ssn-system', 'BatteryLifetime')
    """
    Total useful life of a System's battery in the specified Conditions.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SSNSYSTEMBatteryLifetime

    """

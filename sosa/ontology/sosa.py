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


OntologyUtils.register_namespace('sosa', 'http://www.w3.org/ns/sosa/')


class SOSA:
    """
    The Sensor, Observation, Sample, and Actuator (SOSA) ontology

    SOSA is a web ontology published by the W3C for describing sensors and
    their observations, the involved procedures, the studied features
    interest, the samples used to do so, and the observed properties, as well
    as actuators.

    SOSA is a lightweight but self-contained core ontology included in the
    Semantic Sensor Network (SSN) ontology.

    SOSA is composed of modules that are horizontally layered and may depend on
    each other, i.e., they may rely on the directional import of another
    horizontal module.

    The SOSA ontology is being extended by the W3C for some ease-of-life
    changes to how data is grouped, such as observation collections, chained
    samples. Extension entities are marked with a [*extension] tag.

    Reference:

        https://www.w3.org/TR/vocab-ssn/

    """

    namespace = OntologyUtils.get_namespace('sosa')

    ############################################################################
    #
    # Observation module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling Observations.
    #
    # This module introduces the following classes:
    #
    #     * ObservableProperty
    #     * Observation
    #     * ObservationCollection [*extension]
    #     * Sensor
    #
    # This module introduces the following relationships:
    #
    #     * observedProperty
    #     * phenomenonTime
    #     * observes
    #     * isObservedBy
    #     * madeObservation
    #     * madeBySensor
    #     * hasMember [*extension]
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Observations
    #
    ############################################################################

    OBSERVABLE_PROPERTY = OntologyUtils.get_iri('sosa', 'ObservableProperty')
    """
    An observable quality (property, characteristic) of a FeatureOfInterest.

    Examples:

        * The height of a tree
        * The depth of a water body
        * The temperature of a surface

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAObservableProperty

    """

    OBSERVATION = OntologyUtils.get_iri('sosa', 'Observation')
    """
    An observation is the act of carrying out a Procedure to estimate or
    calculate a value of a property of a FeatureOfInterest.

    A link to a Sensor describes what made the Observation and how. A link to
    an ObservableProperty describes what the result is an estimate of. A link
    to a FeatureOfInterest details what that property was associated with.

    Examples:

        * Estimating the intensity of an Earthquake using the Mercalli
          intensity scale
        * Measuring the energy released by said earthquake

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAObservation

    """

    OBSERVATION_COLLECTION = OntologyUtils.get_iri('sosa', 'ObservationCollection')
    """
    Collection of one or more observations, whose members share a common value
    for one or more property.

    ObservationCollection accommodates multiple observations of which may hold
    one or more of the essential properties of an atomic observation, except
    for the result. Where present, the value of the property(s) of the
    collection are shared by all member observations.

    Examples:

        * A stream of data in which only the time changes between consecutive
          results for the same property on a single feature of interest, using
          the same sensor.

        * A sensor network generates a set of results, over the same time
          interval, for the same property(s) over a suit of features-of-
          interest.

    Reference:

        https://www.w3.org/TR/vocab-ssn-ext/#sosa:ObservationCollection

    """

    SENSOR = OntologyUtils.get_iri('sosa', 'Sensor')
    """
    A sensor is a Device, agent (including humans), or software (simulation)
    involved in, or implementing, a Procedure.

    Sensors respond to a Stimulus, e.g., a change in the environment, or Input
    data composed from the Results of prior Observations.

    Sensors generate a Result. Sensors can be hosted by Platforms.

    Examples:

        * Accelerometers
        * Barometers
        * Human eyes

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSASesnor

    """

    OBSERVED_PROPERTY = OntologyUtils.get_iri('sosa', 'observedProperty')
    """
    A relation linking an Observation to the property that was observed.

    The ObservableProperty should be a property of the FeatureOfInterest
    (linked by hasFeatureOfInterest) of this Observation.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAobservedProperty

    """

    PHENOMENON_TIME = OntologyUtils.get_iri('sosa', 'phenomenonTime')
    """
    The time that the Result of an Observation, Actuation, or Sampling applies
    to the FeatureOfInterest.

    Not necessarily the same as the resultTime. May be an interval or an
    instant, or some other compound temporal entity.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAphenomenonTime

    """

    OBSERVES = OntologyUtils.get_iri('sosa', 'observes')
    """
    Relation between a Sensor and an ObservableProperty that it is capable of
    sensing.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAobserves

    """

    IS_OBSERVED_BY = OntologyUtils.get_iri('sosa', 'isObservedBy')
    """
    Relation between an ObservableProperty and the Sensor able to observe it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisObservedBy

    """

    MADE_OBSERVATION = OntologyUtils.get_iri('sosa', 'madeObservation')
    """
    Relation between a Sensor and an Observation made by the Sensor.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeObservation

    """

    MADE_BY_SENSOR = OntologyUtils.get_iri('sosa', 'madeBySensor')
    """
    Relation between an Observation and the Sensor which made the Observations.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeBySensor
    """

    HAS_MEMBER = OntologyUtils.get_iri('sosa', 'hasMember')
    """
    Link to a member of a collection of observations that share the same value
    for one or more of the characteristic properties.

    Any appearance of sosa:hasMember in a dataset entails that the subject of
    the statement is a sosa:ObservationCollection and the object of the
    statement is a sosa:Observation or sosa:ObservationCollection.

    Reference:

        https://www.w3.org/TR/vocab-ssn-ext/#sosa:hasMember

    """

    ############################################################################
    #
    # Actuation module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling Actuations.
    #
    # This module introduces the following classes:
    #
    #     * ActuatableProperty
    #     * Actuation
    #     * Actuator
    #
    # This module introduces the following relationships:
    #
    #     * actsOnProperty
    #     * isActedOnBy
    #     * madeActuation
    #     * madeByActuator
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Actuations
    #
    ############################################################################

    ACTUATABLE_PROPERTY = OntologyUtils.get_iri('sosa', 'ActuatableProperty')
    """
    An actuatable quality (property, characteristic) of a FeatureOfInterest.

    Examples:

        * The ability of the window to be opened and closed is its
          ActuatableProperty

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAActuatableProperty

    """

    ACTUATION = OntologyUtils.get_iri('sosa', 'Actuation')
    """
    An Actuation carries out a Procedure to change the state of the world using
    an Actuator.

    Examples:

        * The activity of automatically closing a window if the temperature in
          a room drops below 20 degree Celsius

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAActuation

    """

    ACTUATOR = OntologyUtils.get_iri('sosa', 'Actuator')
    """
    A device that is used by, or implements, a Procedure that changes the state
    of the world.

    Examples:

        * A window actuator for automatic window control

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAActuator

    """

    ACTS_ON_PROPERTY = OntologyUtils.get_iri('sosa', 'actsOnProperty')
    """
    Relation between an Actuation and the property of a FeatureOfInterest it is
    acting upon.

    Examples:

        * In the Actuation of automatically closing a window if the temperature
          in a room drops below 20 degrees Celsius, the property is the state
          of the window as it changes from being open to being closed.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAactsOnProperty

    """

    IS_ACTED_ON_BY = OntologyUtils.get_iri('sosa', 'isActedOnBy')
    """
    Relation between an ActuatableProperty of a FeatureOfInterest and 
    Actuation changing its state.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisActedOnBy

    """

    MADE_ACTUATION = OntologyUtils.get_iri('sosa', 'madeActuation')
    """
    Relation between an Actuator and the Actuation made by the Actuator.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeActuation

    """

    MADE_BY_ACTUATOR = OntologyUtils.get_iri('sosa', 'madeByActuator')
    """
    Relation linking an Actuation to the Actuator that made that Actuation.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeByActuator

    """

    ############################################################################
    #
    # Sample module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling Sampling.
    #
    # This module introduces the following classes:
    #
    #     * Sample
    #     * Sampling
    #     * Sampler
    #
    # This module introduces the following relationships:
    #
    #     * hasSample
    #     * isSampleOf
    #     * madeSampling
    #     * madeBySampler
    #     * hasOriginalSample [*extension]
    #     * hasSampledFeature [*extension]
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Actuations
    #
    ############################################################################

    SAMPLE = OntologyUtils.get_iri('sosa', 'Sample')
    """
    Feature which is intended to be representative of a FeatureOfInterest on
    which Observations may be made.

    Examples:

        * A statistical sample is often designed to be characteristic of an
          entire population, so that Observations can be made regarding the
          sample that provide a good estimate of the properties of the
          population

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSASample

    """

    SAMPLING = OntologyUtils.get_iri('sosa', 'Sampling')
    """
    An act of Sampling carries out a Procedure to create or transform one or
    more Samples.

    Examples:

        * Crushing a rock sample in a ball mill
        * Digging a pit through a soil sequence
        * Dividing a field site into quadrants
        * Drawing blood from a patient
        * Drilling an observation well
        * Establishing a station for environmental monitoring
        * Registering an image of the landscape
        * Sieving a powder to separate the subset finer than 100-mesh
        * Selecting a subset of a population
        * Splitting a piece of drill-core to create two new samples
        * Taking a diamond-drill core from a rock outcrop

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSASampling

    """

    SAMPLER = OntologyUtils.get_iri('sosa', 'Sampler')
    """
    A device that is used by, or implements, a Procedure to create or transform
    one or more samples.

    Sometimes the distinction between the Sampler and the Sensor is
    evident, as they are packaged as a unit. A Sampler need not be a physical
    device.

    Examples:

        * Ball mill
        * Diamond drill
        * Hammer
        * Hypodermic syringe and needle
        * Image sensor
        * Soil auger

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSASampler

    """

    HAS_SAMPLE = OntologyUtils.get_iri('sosa', 'hasSample')
    """
    Relation between a FeatureOfInterest and the Sample used to represent it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhasSample

    """

    IS_SAMPLE_OF = OntologyUtils.get_iri('sosa', 'isSampleOf')
    """
    Relation from a Sample to the FeatureOfInterest that it is intended to be
    representative of.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisSampleOf

    """

    MADE_SAMPLING = OntologyUtils.get_iri('sosa', 'madeSampling')
    """
    Relation between a Sampler (sampling device or entity) and the Sampling act
    it performed.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeSampling

    """

    MADE_BY_SAMPLER = OntologyUtils.get_iri('sosa', 'madeBySampler')
    """
    Relation linking an act of Sampling to the Sampler (sampling device or
    entity) that made it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAmadeBySampler

    """

    HAS_ORIGINAL_SAMPLE = OntologyUtils.get_iri('sosa', 'hasOriginalSample')
    """
    Link to the original sample that is related to the context sample through a
    chain of isSampleOf relations.

    The class sosa:Sample has a maximum of 1 original sample. This constraint
    says that no more than one original-sample is expected for each individual
    sample.

    Reference:

        https://www.w3.org/TR/vocab-ssn-ext/#sosa:hasOriginalSample

    TODO: Capitalization error in definition at reference

    """

    HAS_SAMPLED_FEATURE = OntologyUtils.get_iri('sosa', 'hasSampledFeature')
    """
    Link to the ultimate feature of interest of the context sample - i.e. the
    end of a chain of isSampleOf relations.

    The class sosa:Sample can have more than 1 original sample. More than one
    sampled feature may apply when a single sample proxies for different
    ultimate features when used in multiple investigations.

    Reference:

        https://www.w3.org/TR/vocab-ssn-ext/#sosa:hasSampledFeature

    """
    ############################################################################
    #
    # Features of Interest
    #
    # Axiomatization of Features of Interest.
    #
    # This module introduces the following classes:
    #
    #     * FeatureOfInterest
    #
    # This module introduces the following relationships:
    #
    #     * hasFeatureOfInterest
    #     * isFeatureOfInterestOf
    #     * hasUltimateFeatureOfInterest [*extension]
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Features-of-Interest-and-Properties
    #
    ############################################################################

    FEATURE_OF_INTEREST = OntologyUtils.get_iri('sosa', 'FeatureOfInterest')
    """
    A FeatureOfInterest appears across three modules:

        * The thing whose property is being estimated or calculated in the
          course of an Observation
        * The thing whose property is being manipulated by an Actuator
        * The thing which is being sampled or transformed in an act of Sampling

    Examples:

        * When measuring the height of a tree, the tree is the
          FeatureOfInterest
        * A window is a FeatureOfInterest for an automatic window control
          Actuator

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAFeatureOfInterest

    """

    HAS_FEATURE_OF_INTEREST = OntologyUtils.get_iri('sosa', 'hasFeatureOfInterest')
    """
    A relation between:

        * An Observation and the entity whose quality was observed
        * An Actuation and the entity whose property was modified
        * An act of Sampling and the entity that was sampled

    Examples:

        * In an Observation of the weight of a person, the FeatureOfInterest
          is the person and the property is its weight.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhasFeatureOfInterest

    """

    IS_FEATURE_OF_INTEREST_OF = OntologyUtils.get_iri('sosa', 'isFeatureOfInterestOf')
    """
    A relation between a FeatureOfInterest and an Observation about it or an
    Actuation acting on it, or an act of Sampling that sampled it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisFeatureOfInterestOf

    """

    HAS_ULTIMATE_FEATURE_OF_INTEREST = OntologyUtils.get_iri('sosa', 'hasUltimateFeatureOfInterest')
    """
    Link to the ultimate feature of interest of an observation or act of
    sampling.

    This is useful when the proximate feature of interest is a sample of the
    ultimate feature of interest, directly or transitively.

    An Observation can have more than 1 ultimate feature of interest for each
    individual observation.

    Reference:

        https://www.w3.org/TR/vocab-ssn-ext/#sosa:hasUltimateFeatureOfInterest

    TODO: Fix typo of trasntitively at reference link

    """

    ############################################################################
    #
    # Result module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling Results.
    #
    # This module introduces the following classes:
    #
    #     * Result
    #
    # This module introduces the following relationships:
    #
    #     * hasResult
    #     * isResultOf
    #     * hasSimpleResult
    #     * resultTime
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Results
    #
    ############################################################################

    RESULT = OntologyUtils.get_iri('sosa', 'Result')
    """
    The Result of an Observation, Actuation, or act of Sampling.

    To store an observation's simple result value one can use the
    hasSimpleResult property.

    Examples:

        * The value 20 as the height of a certain tree together with the unit,
          e.g., Meter.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAResult

    """

    HAS_RESULT = OntologyUtils.get_iri('sosa', 'hasResult')
    """
    Relation linking an Observation and a Sensor or Actuator and a Result,
    which contains a value representing the value associated with the observed
    Property.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhasResult

    """

    IS_RESULT_OF = OntologyUtils.get_iri('sosa', 'isResultOf')
    """
    Relation linking a Result to the Observation or Actuation that created or
    caused it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisResultOf

    """

    HAS_SIMPLE_RESULT = OntologyUtils.get_iri('sosa', 'hasSimpleResult')
    """
    The simple value of an Observation or Actuation.

    Examples:

        * The values 23 or true

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhasSimpleResult

    """

    RESULT_TIME = OntologyUtils.get_iri('sosa', 'resultTime')
    """
    The result time is the instant of time when the Observation, Actuation or
    Sampling activity was completed.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhasSimpleResult

    """

    ############################################################################
    #
    # Procedure module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling Procedures.
    #
    # This module introduces the following classes:
    #
    #     * Procedure
    #
    # This module introduces the following relationships
    #
    #     * usedProcedure
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Procedures
    #
    ############################################################################

    PROCEDURE = OntologyUtils.get_iri('sosa', 'Procedure')
    """
    A workflow, protocol, plan, algorithm, or computational method specifying
    how to make an Observation, create a Sample, or make a change to the state
    of the world via an Actuator

    A Procedure is re-usable, and might be involved in many Observations,
    Samplings, or Actuations. It explains the steps to be carried out to
    arrive at reproducible Results.

    Note: Many Observations may be created via the same Procedure, the same way
    as many tables are assembled using the same instructions (as information
    objects, not their concrete realization).

    Examples:

        * The standard height for anemometers above ground when measuring wind
          speed, typically 10m for meteorological measures and 2m in
          Agrometeorology
        * The Sensor placement of said anemometers

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAProcedure

    """

    USED_PROCEDURE = OntologyUtils.get_iri('sosa', 'usedProcedure')
    """
    A relation to link to a re-usable Procedure used in making an Observation,
    an Actuation, or a Sample, typically through a Sensor, Actuator or Sampler.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAusedProcedure

    """

    ############################################################################
    #
    # System module
    #
    # Axiomatization of the core classes and properties that are specifically
    # related to modeling systems and their deployment.
    #
    # This module introduces the following classes:
    #
    #     * Platform
    #
    # This module introduces the following relationships:
    #
    #     * hosts
    #     * isHostedBy
    #
    # Reference:
    #
    #     https://www.w3.org/TR/vocab-ssn/#Systems-and-their-Deployment
    #
    ############################################################################

    PLATFORM = OntologyUtils.get_iri('sosa', 'Platform')
    """
    A Platform is an entity that hosts other entities, particularly Sensors,
    Actuators, Samplers, and other Platforms.

    Examples:

        * Post
        * Buoy
        * Vehicle
        * Ship
        * Aircraft
        * Satellite
        * Cell-phone
        * Human or animal for biological Sensors or Actuators

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAPlatform

    """

    HOSTS = OntologyUtils.get_iri('sosa', 'hosts')
    """
    Relation between a Platform and a Sensor, Actuator, Sampler, or Platform,
    hosted or mounted on it.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAhosts

    """

    IS_HOSTED_BY = OntologyUtils.get_iri('sosa', 'isHostedBy')
    """
    Relation between a Sensor, or Actuator, Sampler, or Platform, and the
    Platform that it is mounted on or hosted by.

    Reference:

        https://www.w3.org/TR/vocab-ssn/#SOSAisHostedBy

    """

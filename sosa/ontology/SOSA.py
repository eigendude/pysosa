################################################################################
#
#  Copyright (C) 2019 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#################################################################################

#
# Classes in the SOSA specification.
#

from sosa.ontology.OntologyUtils import OntologyUtils


OntologyUtils.register_namespace('sosa', 'http://sosa.org/schema/sosa#')


class ActuatableProperty(object):
    """
    A property or characteristic of the hardware being actuated.

    Example:

    A window actuator acts by changing the state between a frame and a
    window. The ability of the window to be opened and closed is its
    ActuatableProperty.
    """
    iri = OntologyUtils.get_iri('sosa', 'ActuatableProperty')


class Actuation(object):
    """
    An Actuation carries out a Procedure to change the state of the world.

    Example:

    The activity of automatically closing a window if the temperature in a
    room drops below 20 degree Celsius. The activity is the Actuation and
    the device that closes the window is the Actuator. The Procedure is the
    rule, plan, or specification that defines the conditions that triggers
    the Actuation, here a drop in temperature.
    """
    iri = OntologyUtils.get_iri('sosa', 'Actuation')


class Actuator(object):
    """
    A device that is used by, or implements, a Procedure that changes the
    state of the world.

    Example:

    A window actuator for automatic window control, i.e., opening or closing
    the window.
    """
    iri = OntologyUtils.get_iri('sosa', 'Actuator')


class FeatureOfInterest(object):
    """
    The thing whose property is being estimated or calculated.

    Example:

    When measuring the height of a tree, the height is the ObservedProperty,
    20m may be the Result of the Observation, and the tree is the
    FeatureOfInterest. A window is a FeatureOfInterest for an automatic window
    control Actuator.
    """
    iri = OntologyUtils.get_iri('sosa', 'FeatureOfInterest')


class ObservableProperty(object):
    """
    An observable quality of a FeatureOfInterest.

    Example:

    The height of a tree, the depth of a water body, or the temperature of a
    surface are examples of observable properties, while the value of a
    classic car is not (directly) observable but asserted.
    """
    iri = OntologyUtils.get_iri('sosa', 'ObservableProperty')


class Observation(object):
    """
    Activity of carrying out a Procedure to estimate or calculate a value of
    a property of a FeatureOfInterest.

    Example:

    The activity of estimating the intensity of an Earthquake using the
    Mercalli intensity scale is an Observation as is measuring the moment
    magnitude, i.e., the energy released by said earthquake.
    """
    iri = OntologyUtils.get_iri('sosa', 'Observation')


class Platform(object):
    """
    A Platform is an entity that hosts other entities, particularly Sensors,
    Actuators and other Platforms.

    Example:

    A post, buoy, vehicle, ship, aircraft, satellite, cell-phone, human or
    animal may act as platforms for (technical or biological) sensors or
    actuators.
    """
    iri = OntologyUtils.get_iri('sosa', 'Platform')


class Procedure:
    """
    A workflow, protocol, plan, algorithm, or computational method specifying
    how to make an Observation, create a Sample, or make a change to the state
    of the world (via an Actuator).

    Example:

    The measured wind speed differs depending on the height of the sensor above
    the surface, e.g., due to friction.

    Consequently, procedures for measuring wind speed define a standard height
    for anemometers above ground, typically 10m for meteorological measures and
    2m in Agrometeorology.

    Note:

    Many observations may be created via the same Procedure, the same way as
    many tables are assembled using the same instructions (as information
    objects, not their concrete realization).
    """
    iri = OntologyUtils.get_iri('sosa', 'Procedure')


class Result(object):
    """
    The Result of an Observation, Actuation, or act of Sampling.

    Example:

    The value 20 as the height of a certain tree together with the unit,
    e.g., Meter.
    """
    iri = OntologyUtils.get_iri('sosa', 'Result')


class Sample(object):
    """
    Feature on which Observations may be made, which is intended to be
    representative of a FeatureOfInterest that is not fully accessible.

    Physical samples are sometimes known as 'specimens'.

    Example:

    In the context of the observation model, it connotes the 'world in the
    vicinity of the station', so the observed properties relate to the physical
    medium at the station, and not to any physical artifact such as a mooring,
    buoy, benchmark, monument, well, etc.

    A statistical sample is often designed to be characteristic of an entire
    population, so that observations can be made regarding the sample that
    provide a good estimate of the properties of the population.
    """
    iri = OntologyUtils.get_iri('sosa', 'Sample')


class Sampler(object):
    """
    A device that is used by, or implements, a Sampling Procedure to create or
    transform one or more samples.

    Example:

    A ball mill, diamond drill, hammer, hypodermic syringe and needle, image
    sensor or a soil auger can all act as sampling devices (i.e., be Samplers).
    """
    iri = OntologyUtils.get_iri('sosa', 'Sampler')


class Sampling(object):
    """
    An act of Sampling carries out a sampling Procedure to create or transform
    one or more samples.

    Examples:

      * Crushing a rock sample in a ball mill.
      * Digging a pit through a soil sequence.
      * Dividing a field site into quadrants.
      * Drawing blood from a patient.
      * Drilling an observation well.
      * Establishing a station for environmental monitoring.
      * Registering an image of the landscape.
      * Sieving a powder to separate the subset finer than 100-mesh.
      * Selecting a subset of a population.
      * Splitting a piece of drill-core to create two new samples.
      * Taking a diamond-drill core from a rock outcrop.
    """
    iri = OntologyUtils.get_iri('sosa', 'Sampling')


class Sensor(object):
    """
    Device, agent (including humans), or software (simulation) involved in, or
    implementing, a Procedure. Sensors respond to a stimulus, e.g., a change
    in the environment, or input data composed from the results of prior
    Observations, and generate a Result. Sensors can be mounted on Platforms.

    Example:

    Accelerometers, gyroscopes, barometers, magnetometers, and so forth are
    sensors that are typically mounted on a modern smart phone (which acts as
    Platform).

    Other examples of sensors include the human eyes.
    """
    iri = OntologyUtils.get_iri('sosa', 'Sensor')

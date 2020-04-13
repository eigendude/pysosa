################################################################################
#
#  Copyright (C) 2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from qudt.ontology.ontology_utils import OntologyUtils


OntologyUtils.register_namespace('schema', 'http://schema.org/')


class SCHEMA:
    """
    Schema.org is a collaborative, community activity with a mission to create,
    maintain, and promote schemas for structured data on the Internet, on web
    pages, in email messages, and beyond.

    Reference:

        https://schema.org/

    """

    namespace = OntologyUtils.get_namespace('schema')

    DESCRIPTION = OntologyUtils.get_iri('schema', 'description')
    """
    A description of the item.

    Reference:

        https://schema.org/description

    """

    MANUFACTURER = OntologyUtils.get_iri('schema', 'manufacturer')
    """
    The manufacturer of the product.

    Reference:

        https://schema.org/manufacturer

    """

    MODEL = OntologyUtils.get_iri('schema', 'model')
    """
    The model of the product.

    Reference:

        https://schema.org/model

    """

    SERIAL_NUMBER = OntologyUtils.get_iri('schema', 'serialNumber')
    """
    The serial number or any alphanumeric identifier of a particular product.

    Reference:

        https://schema.org/serialNumber

    """

    PROVIDER = OntologyUtils.get_iri('schema', 'provider')
    """
    The service provider, service operator, or service performer; the goods
    producer. Another party (a seller) may offer those services or goods on
    behalf of the provider.

    A provider may also serve as the seller.
    """

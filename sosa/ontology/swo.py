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


OntologyUtils.register_namespace('obo', 'http://purl.obolibrary.org/obo/')


class SWO:
    """
    The Software Ontology (SWO) is a resource for describing software tools,
    their types, tasks, versions, provenance and associated data.

    It contains detailed information on licensing and formats as well as
    software applications themselves, mainly (but not limited) to the
    bioinformatics community.

    Reference:

        http://www.ontobee.org/ontology/SWO

    """

    namespace = OntologyUtils.get_namespace('obo')

    VERSION_NUMBER = OntologyUtils.get_iri('obo', 'IAO_0000129')
    """
    A version number is an information content entity which is a sequence of
    characters borne by part of each of a class of manufactured products or its
    packaging and indicates its order within a set of other products having the
    same name.

    Reference:

        http://www.ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000129

    """

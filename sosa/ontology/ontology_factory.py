################################################################################
#
#  Copyright (C) 2020 Garrett Brown
#  This file is part of pysosa - https://github.com/eigendude/pysosa
#
#  SPDX-License-Identifier: BSD-3-Clause
#  See the file LICENSE for more information.
#
################################################################################

from sosa.feature import FeatureOfInterest
from sosa.feature import Property

import os
from qudt.ontology.ontology_reader import OntologyReader
from qudt.ontology.unit_factory import UnitFactory
from qudt.ontology.qudt import QUDT
from qudt.ontology.rdf import RDF
from qudt.ontology.rdfs import RDFS
import rdflib
from sosa.ontology.schema import SCHEMA
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple


# Type definitions
Statement = Tuple[str, str, rdflib.term.Identifier]
Predicate = Callable[[str, str, rdflib.term.Identifier], bool]


class OntologyFactory(object):
    """
    A factory for creating instances of classes defined by the ontology.
    """

    _instance: Optional['OntologyFactory'] = None

    def __init__(self):
        """
        Create an instance of the ontology factory and load the RDF triplet
        repositories.
        """
        # Get the path to this package
        package_path = os.path.dirname(os.path.realpath(__file__))

        # RDF triplet repositories
        self._feature_repos: List[rdflib.Graph] = list()
        self._property_repos: List[rdflib.Graph] = list()

    @classmethod
    def _get_instance(cls) -> 'OntologyFactory':
        """
        Get the singleton used to store repository contents.

        :return: The singleton instance of type OntologyFactory
        """
        if cls._instance is None:
            cls._instance = OntologyFactory()

        return cls._instance

    @classmethod
    def load_feature_repo(cls, repo_file: str) -> int:
        """
        Loads the specified RDF triplet repo using rdflib expressing Features
        of Interest.

        If the repo's file does not exist, this function has no effect and
        returns 0.

        :param repo_file: The path to the RDF triplet repo
        :return: The number of triplets loaded, or 0 if the file doesn't exist
        """
        return cls._load_repo(repo_file, cls._get_instance()._feature_repos)

    @classmethod
    def load_property_repo(cls, repo_file: str) -> int:
        """
        Loads the specified RDF triplet repo using rdflib expressing Observable
        and Actuatable Properties.

        If the repo's file does not exist, this function has no effect and
        returns 0.

        :param repo_file: The path to the RDF triplet repo
        :return: The number of triplets loaded, or 0 if the file doesn't exist
        """
        return cls._load_repo(repo_file, cls._get_instance()._property_repos)

    @classmethod
    def get_feature_of_interest(cls, resource_iri: str) -> FeatureOfInterest:
        """
        Get a Feature of Interest instance by its resource IRI.

        :param resource_iri: The features's resource IRI
        :return: The feature
        """
        return cls._get_instance()._get_feature_of_interest(resource_iri)

    @classmethod
    def get_property(cls, resource_iri: str) -> Property:
        """
        Get a Property instance by its resource IRI.

        :param resource_iri: The property's resource IRI
        :return: The property
        """
        return cls._get_instance()._get_property(resource_iri)

    def _get_feature_of_interest(self, resource_iri: str) -> FeatureOfInterest:
        """
        Internal implementation of get_feature_of_interest().
        """
        feature = FeatureOfInterest(
            resource_iri=resource_iri,
        )

        statements: List[Statement] = self._get_statements(
            self._feature_repos,
            lambda subj, pred, obj: str(subj) == resource_iri,
        )

        for (subject, predicate, obj) in statements:
            if predicate == RDF.TYPE:
                feature.type_iri = str(obj)
            if predicate == RDFS.LABEL:
                feature.label = str(obj)
            elif predicate == SCHEMA.DESCRIPTION:
                feature.description = str(obj)
            elif predicate == QUDT.ABBREVIATION:
                feature.abbreviation = str(obj)

        return feature

    def _get_property(self, resource_iri: str) -> Property:
        """
        Internal implementation of get_property().
        """
        prop = Property(
            resource_iri=resource_iri,
        )

        statements: List[Statement] = self._get_statements(
            self._property_repos,
            lambda subj, pred, obj: str(subj) == resource_iri,
        )

        for (subject, predicate, obj) in statements:
            if predicate == RDF.TYPE:
                prop.type_iri = str(obj)
            if predicate == RDFS.LABEL:
                prop.label = str(obj)
            elif predicate == SCHEMA.DESCRIPTION:
                prop.description = str(obj)
            elif predicate == QUDT.UNIT:
                prop.unit = UnitFactory.get_unit(str(obj))

        return prop

    @staticmethod
    def _load_repo(repo_file: str, destination_list: List[rdflib.Graph]) -> int:
        """
        Helper function to load RDF triplet repos into a destination list.
        """
        repo = OntologyReader.read(repo_file)

        if repo:
            destination_list.append(repo)

        return len(repo)

    @staticmethod
    def _get_statements(
            repos: List[rdflib.Graph],
            triplet_test: Predicate
    ) -> List[Statement]:
        """
        Get the statements of the given repos that satisfy the provided lambda.

        :param repo: The ontology repository
        :param triplet_test: The lambda to invoke per statement
        :return: The matching statements
        """
        statements: List[Statement] = list()

        for repo in repos:
            for (subject, predicate, obj) in repo:
                if triplet_test(subject, predicate, obj):
                    statements.append((str(subject), str(predicate), obj))

        return statements

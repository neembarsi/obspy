#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Domain definitions for the the download helpers.

Subclass if you need more complex custom domains.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2014
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
from abc import ABCMeta, abstractmethod


class Domain:
    """
    Abstract base class defining a domain. Subclass to define a custom domain.

    Each subclass has to implement the
    :meth:`~obspy.fdsn.download_helpers.Domain.get_query_parameters` method and
    optionally the
    :meth:`~obspy.fdsn.download_helpers.Domain.in_in_domain` method.

    The :meth:`~obspy.fdsn.download_helpers.Domain.get_query_parameters` method
    must return the query parameters to download as much data as required. The
    :meth:`~obspy.fdsn.download_helpers.Domain.in_in_domain` can later be
    used to refine the domain after the data has been downloaded.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_query_parameters(self):
        """
        Return the domain specific query parameters for the
        :meth:`~obspy.fdsn.client.Client.get_stations' method. Possibilities
        are ``minlatitude``, ``maxlatitude``, ``minlongitude``, and
        ``maxlongitude`` for rectangular queries or ``latitude``,
        ``longitude``, ``minradius``, and ``maxradius`` for circular queries.
        """
        pass

    def is_in_domain(self, latitude, longitude):
        """
        Returns True/False depending on the point being in the domain.
        """
        raise NotImplementedError


class RectangularDomain(Domain):
    def __init__(self, min_latitude, max_latitude, min_longitude,
                 max_longitude):
        self.min_latitude = min_latitude
        self.max_latitude = max_latitude
        self.min_longitude = min_longitude
        self.max_longitude = max_longitude

    def get_query_parameters(self):
        return {
            "min_latitude": self.min_latitude,
            "max_latitude": self.max_latitude,
            "min_longitude": self.min_longitude,
            "max_longitude": self.max_longitude}


class CircularDomain(Domain):
    def __init__(self, latitude, longitude, min_radius, max_radius):
        self.latitude = latitude
        self.longitude = longitude
        self.min_radius = min_radius
        self.max_radius = max_radius

    def get_query_parameters(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "min_radius": self.min_radius,
            "max_radius": self.max_radius}


class GlobalDomain(Domain):
    def get_query_parameters(self):
        return {}


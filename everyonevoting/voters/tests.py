from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import GeoDistrict, Affiliation, Voter

# TODO: Test GeoDistricts

class ModelsTest(TestCase):

    def test_geodistrict(self):
        base_geodistrict = GeoDistrict.objects.create()
        self.assertEquals("Global", base_geodistrict.name)

        east_geodistrict = GeoDistrict.objects.create(name="Eastern",
                                                      parent=base_geodistrict)
        west_geodistrict = GeoDistrict.objects.create(name="Western",
                                                      parent=base_geodistrict)

        self.assertEqual(east_geodistrict.name, "Eastern")
        self.assertEqual(west_geodistrict.name, "Western")

        self.assertEqual(GeoDistrict.objects.count(), 3)
        self.assertQuerysetEqual(base_geodistrict.geodistrict_set.all(),
                                 [repr(east_geodistrict), repr(west_geodistrict)],
                                 ordered=False)


    def test_affiliation(self):
        pass

    def test_voter(self):
        pass

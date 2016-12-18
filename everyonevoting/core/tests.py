from datetime import datetime
from freezegun import freeze_time

from django.http import HttpRequest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.db import connection
from django.core.management.color import no_style
from django.db.models.base import ModelBase

from .models import BaseModel, Organization, UserProfile

# TODO: Test user account and profile creation
# TODO: Test organization model creation


class ModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins. To use, subclass and specify
    the mixin class variable. A model using the mixin will be made
    available in self.model.
    """

    def setUp(self):
        # Create a dummy model which extends the mixin
        self.model = ModelBase('__TestModel__'+self.mixin.__name__, (self.mixin,),
            { '__module__': self.mixin.__module__ })

        # Create the schema for our test model
        self._style = no_style()
        sql, _ = connection.creation.sql_create_model(self.model, self._style)

        self._cursor = connection.cursor()
        for statement in sql:
            self._cursor.execute(statement)

    def tearDown(self):
        # Delete the schema for the test model
        sql = connection.creation.sql_destroy_model(self.model, (), self._style)
        for statement in sql:
            self._cursor.execute(statement)


class BaseModelTestCase(ModelMixinTestCase):

    def setUp(self):
        self.mixin = BaseModel

    def test_model(self):
        print(self.model.created_on)



class OrganizationTest(TestCase):

    def setUp(self):
        # First we create a new user
        self.user = User.objects.create_user('sjohnson', 'sjohnson@masa.org',
                                        'sarahpassword')
        self.user.first_name = "Sarah"
        self.user.last_name = "Johnson"
        self.user.save()

        # Create test client
        self.client = Client()

    @freeze_time("2016-12-14")
    def test_object_creation(self):
        """Test base object creation and modification time."""

        # Test time created
        obj = Organization.objects.create(
            name='Test',
            responsible_officer=self.user
        )
        self.assertEqual(obj.created_on, timezone.now(), 'A message...')

        # Test object ownership
        #self.assertEqual(obj.responsible_officer, self.user)

        # Test time modified
        obj.name = 'Test Again'
        obj.save()
        self.assertEqual(obj.updated_on, timezone.now(), 'Another message')


class NewUserTest(TestCase):
    """This test will check the functionality of user accounts, including
    core django.contrib.auth objects and custom UserProfile functionality."""

    def setUp(self):
        # First we create a new user
        self.user = User.objects.create_user('sjohnson', 'sjohnson@masa.org',
                                        'sarahpassword')
        self.user.first_name = "Sarah"
        self.user.last_name = "Johnson"
        self.user.save()

        # Create test client
        self.client = Client()

    def tearDown(self):
        pass

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        #self.assertEqual(len(response.context['customers']), 5)

    def test_user_login(self):
        # Then we retrieve and authenticate the new user
        user = authenticate(username='sjohnson', password='sarahpassword')
        print(user.first_name)
        print(user.last_login)
        response = self.client.get('/')
        # login(self.client.request, user)
        print("YES, "+str(user.is_authenticated()))
        #print(dir(response.context))


    def test_user_email_verification(self):
        # Email verification
        pass

    def test_user_profile(self):
        pass

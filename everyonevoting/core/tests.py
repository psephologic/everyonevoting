from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Organization, UserProfile
from .views import IndexView

# TODO: Test user account and profile creation
# TODO: Test organization model creation


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, IndexView)

    def test_index_page_returns_correct_html(self):
        request = HttpRequest()
        response = IndexView.as_view()(request)
        self.assertTemplateUsed('core/index.html')
        # self.assertEqual(response.content.decode(), expected_html)


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
        print(dir(response.context))


    def test_user_email_verification(self):
        # Email verification
        pass

    def test_user_profile(self):
        pass


class OrganizationTest(TestCase):

    def test_organization_creation(self):
        organization = Organization()

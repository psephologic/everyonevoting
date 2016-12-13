from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_site(self):

        # Dr. Sarah Johnson has been charged with coordinating the annual
        # election for her organization. She has found Everyone Voting through a
        # web search and checks it out.
        self.browser.get(self.live_server_url)
        self.assertIn('Everyone Voting', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Everyone Voting', header_text)

        print("Done")

        # The home page’s goal is to get organizations up and running quickly for their
        # election needs, and so features a simple form for getting started. Sarah
        # enters the name of her organization, “Mid-Atlantic Sociology Association”
        # (MASA), the date of the election, and presses the “Continue” button.

        # The system does a quick search to see if the organization already exists in
        # the database, and deems it new. The next form is a registration page, where
        # Sarah enters her contact information needed to create her account.

        # A verification email is issued, and once confirmed, Sarah (now an
        # administrator) is taken to the next form, where she sets up the organization’s
        # account. Contact information is entered and saved.

        # The next form is used to define the governing structure of the organization,
        # including the elected positions, their terms, and current incumbent information.

        # The following form provides tools to import the member list into a registry.

        # The organization represents a large body of members in NY, NJ, and PA.
        # Elections are held for President, Vice-President, Secretary, Treasurer, and
        # members of the Executive Committee.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
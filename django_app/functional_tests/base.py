from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from superlists.settings import TEST


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        if TEST:
            cls.server_url = 'http://tdd1.django-test.com'
            cls.live_server_url = cls.server_url
            super().setUpClass()
            return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

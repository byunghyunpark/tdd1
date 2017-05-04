from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 효시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 바로 작업을 추가하기로 한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '신규 작업 추가'
        )

        # '공잣깃털 사기'라고 텍스트 상자에 입력한다.
        inputbox.send_keys('공잣깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에 '1: 공작깃털 사기' 아이템이 추가된다.
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: 공잣깃털 사기')

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 다시 '공잣깃털을 이용해서 그물 만들기' 라고 입력한다

        # 에디스는 매우 체계적인 사람이다
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        # 페이지는 다시 객신되고 두 개 아이템이 목록에 보인다
        self.check_for_row_in_list_table('1: 공잣깃털 사기')
        self.check_for_row_in_list_table('2: 공잣깃털을 이용해서 그물 만들기')

        # 에디스는 사이트가 입력한 목록을 저장하고 있느지 궁금하다
        # 사이트는 그녀를 위한 특정 URL을 생성해준다
        # 이때 URL에 대한 설명도 함께 제공된다
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

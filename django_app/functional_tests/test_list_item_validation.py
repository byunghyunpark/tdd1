from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # 에디스는 메인 페이지에 접속해서 빈 아이템을 실수로 등록하려고 한다
        # 에러 메시지가 표시된다

        # 다른 아이템을 입력하고 이번에는 정상 처리된다

        # 그녀는 고의적으로 다시 빈 아이템을 등록한다

        # 리스트 페이지에 다시 에러 메시지가 표시된다
        self.fail('write me!')

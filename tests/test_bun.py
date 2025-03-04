from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('Classic bun', 200)

        assert bun.get_name() == 'Classic bun'

    def test_get_price(self):
        bun = Bun('Classic bun', 200)

        assert bun.get_price() == 200


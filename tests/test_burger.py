import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from unittest.mock import Mock


class TestBurger:

    @pytest.mark.parametrize('name, price',
                             [
                                 ['Classic bun', 200],
                                 ['Cheese bun', 100.58],
                                 ['Herb bun', 10000000000000]
                             ])
    def test_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients.index(ingredient) == 1 and burger.ingredients.index(ingredient2) == 0

    def test_get_price(self):
        burger = Burger()
        bun = Bun('Classic bun', 200)
        ingredient = Ingredient('SAUCE', 'Classic sauce', 100)
        ingredient2 = Ingredient('SAUCE', 'Chilli sauce', 50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        price = bun.get_price() * 2 + ingredient.get_price() + ingredient2.get_price()

        assert burger.get_price() == price

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun('Classic bun', 200)
        ingredient = Ingredient('SAUCE', 'Classic sauce', 100)
        ingredient2 = Ingredient('SAUCE', 'Chilli sauce', 50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        receipt = ('(==== Classic bun ====)\n= sauce Classic sauce =\n= sauce Chilli sauce =\n(==== Classic bun '
                   '====)\n\nPrice: 550')

        assert burger.get_receipt() == receipt




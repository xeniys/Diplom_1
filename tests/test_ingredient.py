from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient('SAUCE', 'Classic sauce', 100.50)

        assert ingredient.get_price() == 100.50

    def test_get_name(self):
        ingredient = Ingredient('SAUCE', 'Classic sauce', 100.50)

        assert ingredient.get_name() == 'Classic sauce'

    def test_get_type(self):
        ingredient = Ingredient('SAUCE', 'Classic sauce', 100.50)

        assert ingredient.get_type() == 'SAUCE'

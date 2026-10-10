import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_sauce_creation(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert sauce.get_name() == "Hot Sauce"
        assert sauce.get_price() == 50

    def test_filling_creation(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_type() == INGREDIENT_TYPE_FILLING
        assert filling.get_name() == "Cutlet"
        assert filling.get_price() == 70
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_ingredient_creation_with_sauce_type(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_creation_with_sauce_name_and_price(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_name() == "Hot Sauce"
        assert sauce.get_price() == 50

    def test_ingredient_creation_with_filling_type(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_ingredient_creation_with_filling_name_and_price(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_name() == "Cutlet"
        assert filling.get_price() == 70
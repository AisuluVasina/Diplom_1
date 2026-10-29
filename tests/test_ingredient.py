import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_get_type_returns_sauce(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name_returns_sauce_name(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_name() == "Hot Sauce"

    def test_get_price_returns_sauce_price(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50)
        assert sauce.get_price() == 50

    def test_get_type_returns_filling(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_name_returns_filling_name(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_name() == "Cutlet"

    def test_get_price_returns_filling_price(self):
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Cutlet", 70)
        assert filling.get_price() == 70
import pytest
from praktikum.database import Database

class TestDatabase:

    @pytest.mark.parametrize("index, expected_name, expected_price", [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300),
    ])
    def test_available_buns(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("index, exp_type, exp_name, exp_price", [
        (0, "SAUCE", "hot sauce", 100),
        (3, "FILLING", "cutlet", 100),
        (5, "FILLING", "sausage", 300),
    ])
    def test_available_ingredients(self, index, exp_type, exp_name, exp_price):
        db = Database()
        ing = db.available_ingredients()[index]
        assert ing.get_type() == exp_type
        assert ing.get_name() == exp_name
        assert ing.get_price() == exp_price
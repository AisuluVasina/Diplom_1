import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    """Создает мок-объект булочки с заданными параметрами."""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "Mock Bun"
    mock.get_price.return_value = 100.0
    return mock

@pytest.fixture
def mock_sauce():
    """Создает мок-объект соуса."""
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = "Mock Sauce"
    mock.get_price.return_value = 50.0
    return mock

@pytest.fixture
def mock_filling():
    """Создает мок-объект начинки."""
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = "Mock Filling"
    mock.get_price.return_value = 70.0
    return mock

@pytest.fixture
def burger_with_components(mock_bun, mock_sauce, mock_filling):
    """Создает полностью собранный бургер для комплексных тестов."""
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger
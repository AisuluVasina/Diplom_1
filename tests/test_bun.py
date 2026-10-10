import pytest
from praktikum.bun import Bun

class TestBun:
    def test_get_name(self):
        # Создаём мок-объект
        bun = Bun("Test Bun", 100)
        assert bun.get_name() == "Test Bun"

    def test_get_price(self):
        bun = Bun("Another Bun", 150)
        assert bun.get_price() == 150

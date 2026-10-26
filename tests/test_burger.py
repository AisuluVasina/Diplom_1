import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun  
from praktikum.ingredient import Ingredient 

class TestBurger:

    @pytest.mark.parametrize("price_value", [100.0, 0.0, 999.99])
    def test_set_buns_assigns_correct_bun(self, price_value):
        """
        ПРОВЕРКА: Метод set_buns корректно присваивает объект булочки.
        Что проверяем: 
          - что burger.bun становится равным переданной булочке (то же самое object reference);
          - что цена булочки внутри бургера совпадает с заданной.
        """
        burger = Burger()
        test_bun = Bun("Test Bun", price_value)
        
        burger.set_buns(test_bun)
        
        assert burger.bun == test_bun
        assert burger.bun.get_price() == price_value

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "Hot Sauce", 50.0),
        ("FILLING", "Beef Cutlet", 100.0),
        ("SAUCE", "Chili Sauce", 75.5)
    ])
    def test_add_ingredient_appends_to_list(self, ingredient_type, name, price):
        """
        ПРОВЕРКА: Метод add_ingredient добавляет ингредиент в конец списка.
        Что проверяем:
          - длина списка ingredients становится равна 1 после добавления;
          - первый элемент списка — это именно тот объект ингредиента, который мы передали.
        """
        burger = Burger()
        ingredient = Ingredient(ingredient_type, name, price)
        
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_deletes_by_index(self):
        """
        ПРОВЕРКА: Метод remove_ingredient удаляет элемент по индексу.
        Что проверяем:
          - после удаления первого элемента длина списка становится 1;
          - оставшийся элемент — это второй добавленный ингредиент (ing2).
        """
        burger = Burger()
        ing1 = Ingredient("SAUCE", "Sauce 1", 10)
        ing2 = Ingredient("FILLING", "Filling 1", 20)
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        # Удаляем первый элемент (индекс 0)
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2

    def test_remove_ingredient_raises_index_error(self):
        """
        ПРОВЕРКА: Граничный случай — удаление несуществующего индекса вызывает ошибку.
        Что проверяем:
          - при попытке удалить элемент из пустого списка метод выбрасывает IndexError.
        """
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_swaps_positions_correctly(self):
        """
        ПРОВЕРКА: Метод move_ingredient корректно перемещает элемент в списке.
        Что проверяем:
          - после перемещения ing2 с индекса 1 на индекс 0 порядок списка становится [ing2, ing1, ing3].
        """
        burger = Burger()
        ing1 = Ingredient("SAUCE", "Sauce A", 10)
        ing2 = Ingredient("FILLING", "Filling B", 20)
        ing3 = Ingredient("SAUCE", "Sauce C", 30)
        
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        # Сейчас список: [ing1, ing2, ing3]
        
        # Перемещаем ing2 (индекс 1) на позицию 0
        burger.move_ingredient(1, 0)
        
        # Ожидаемый порядок: [ing2, ing1, ing3]
        assert burger.ingredients == [ing2, ing1, ing3]

    @pytest.mark.parametrize("bun_price, sauce_price, filling_price, expected_total", [
        (100.0, 50.0, 70.0, 320.0),  # 100*2 + 50 + 70
        (0.0, 0.0, 0.0, 0.0),        # Все нули
        (50.5, 10.1, 20.2, 131.3)    # Дробные числа
    ])
    def test_get_price_calculates_correctly(self, bun_price, sauce_price, filling_price, expected_total):
        """
        ПРОВЕРКА: Метод get_price считает сумму по формуле: (цена булочки * 2) + сумма ингредиентов.
        Что проверяем:
          - результат get_price() совпадает с ожидаемой суммой с небольшой погрешностью (для float).
        Зачем: протестировать математику на разных наборах данных, включая нулевые и дробные значения.
        """
        burger = Burger()
        bun = Bun("Test Bun", bun_price)
        sauce = Ingredient("SAUCE", "Test Sauce", sauce_price)
        filling = Ingredient("FILLING", "Test Filling", filling_price)
        
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        calculated_price = burger.get_price()
        
        # Используем округления
        assert abs(calculated_price - expected_total) < 0.01

    def test_get_receipt_format_and_content(self, mock_bun, mock_sauce, mock_filling):
        """
        ПРОВЕРКА: Метод get_receipt возвращает строку в правильном формате.
        Что проверяем:
          - в чеке есть строка с названием булочки;
          - есть строки с ингредиентами (в нижнем регистре, как формирует метод);
          - итоговая цена отображается корректно.
        """
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        receipt = burger.get_receipt()
        
        # Проверяем структуру строки
        assert "(==== Mock Bun ====" in receipt
        # Ищем в нижнем регистре, потому что метод get_receipt сам приводит текст к нижнему регистру
        assert "= sauce mock sauce =" in receipt.lower()
        assert "= filling mock filling =" in receipt.lower()
        assert f"Price: {burger.get_price()}" in receipt

    def test_get_receipt_empty_burger_handling(self):
        """
        ПРОВЕРКА: Поведение get_receipt для бургера без булочки.
        """
        burger = Burger()

        with pytest.raises(AttributeError):
             burger.get_receipt()

    def test_move_ingredient_out_of_bounds(self):
        """
        ПРОВЕРКА: Граничный случай — перемещение элемента за пределы списка вызывает ошибку.
        Что проверяем:
          - попытка переместить элемент с несуществующим индексом (5) вызывает IndexError.
        """
        burger = Burger()
        burger.add_ingredient(Ingredient("SAUCE", "Test", 10))
        
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)
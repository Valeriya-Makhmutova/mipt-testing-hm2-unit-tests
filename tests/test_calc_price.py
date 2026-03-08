import pytest
from src.calc_price import calc_price

# позитивные тесты:

# работа функции без скидки
def test_calc_price_without_discount():
    result = calc_price(1000.0, 0.0, 2)
    assert result == 2000.0
    assert type(result) is float

#работа фнкции со скидкой
def test_calc_price_with_discount():
    result = calc_price(1000.0, 25.0, 2)
    assert result == 1500.0
    assert type(result) is float


# негативные тесты:

# с нулевым количеством билетов
def test_calc_price_with_zero_count():
    with pytest.raises(ValueError):
        calc_price(1000.0, 25.0, 0)

# с некорректной скидкой
def test_calc_price_too_large_discount():
     with pytest.raises(ValueError):
        calc_price(1000.0, 125.0, 2)


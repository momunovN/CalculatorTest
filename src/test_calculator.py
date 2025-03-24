

import pytest
from calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(2, 3) == 5
    assert calc.sum(0, 5) == 5
    assert calc.sum(5, 0) == 5
    assert calc.sum(-1, -1) == -2
    assert calc.sum(-1, 1) == 0
def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(5, 0) == 5
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(-1, 1) == -2
def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(5, 0) == 1
    assert calc.multiply(0, 5) == 1
    assert calc.multiply(-2, -3) == 6
    assert calc.multiply(-2, 3) == -6
def test_divide():

    assert calc.divide(6, 3) == 2
    assert calc.divide(5, 1) == 5
    assert calc.divide(0, 5) == 0
    assert calc.divide(-6, -3) == 2
    assert calc.divide(6, -3) == -2

def test_divide_by_zero():

    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        calc.divide(10, 0)
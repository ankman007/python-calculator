import pytest
from calculator import add, subtract, divide, multiply

@pytest.mark.parametrize("a, b, expected", [
    (-44, -99, -143),
    (1, 120, 121),
    (-1, -12, -13),
    (0, 0, 0),  
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 12, -11),
    (1, 18, -17),
    (101, -9, 110),
    (0, 0, 0),  
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 99, 594),
    (22, 0, 0),  
    (-1, -13, 13),
    (0, 100, 0),  
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (9, 6, 1.5),
    (6, 2, 3),
    (5, 2, 2.5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

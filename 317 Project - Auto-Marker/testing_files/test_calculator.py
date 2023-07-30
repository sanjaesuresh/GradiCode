from src.calculator import Calculator
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
def test_add2():
    calc = Calculator()
    assert calc.add(0, 0) == 0
def test_add3():
    calc = Calculator()
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 1) == 1

def test_subtract2():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    
def test_subtract3():
    calc = Calculator()
    assert calc.subtract(5, 5) == 0
    
def test_subtract4():
    calc = Calculator()
    assert calc.subtract(-1, 1) == -2

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    
def test_multiply2():
    calc = Calculator()
    assert calc.multiply(0, 5) == 0
    
def test_multiply3():
    calc = Calculator()
    assert calc.multiply(-1, 8) == -8

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    
def test_divide2():
    calc = Calculator()
    assert calc.divide(7, 2) == 3.5
    with pytest.raises(ValueError):
        calc.divide(1, 0)
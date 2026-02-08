import pytest
from calculator import Calculator

class TestCalculator:
    
    def setup_method(self):
        print("\nSetting up for a test...")
        self.calc = Calculator()
        
    def test_add(self):
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 10) == -5
        assert self.calc.subtract(0, 0) == 0

    def test_multiply(self):
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0

    def test_divide(self):
        assert self.calc.divide(20, 4) == 5
        assert self.calc.divide(-10, 2) == -5
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
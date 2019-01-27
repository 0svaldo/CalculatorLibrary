"""
Unidad de pruebas para la libreria de calculos
"""


import calculator


class TestCalculator:


    def test_addition(self):
        assert 4 == calculator.add(2,2)


    def test_substraction(self):
        assert 1 == calculator.substract(4,3)


    def test_times(self):
        assert 6 == calculator.times(2,3)

   
    def test_divide(self):
        assert 3 == calculator.times(6,2)

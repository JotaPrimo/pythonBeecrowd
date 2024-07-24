import unittest

from solucoes import AreaOfCircle

class AreaCircleTest(unittest.TestCase):
    def test_deve_retornar_true_equals_doze(self):
        # cenario
        resultado_esperado = "A=12.5664"

        r = 2.00

        # acao
        resutado_obtido = AreaOfCircle.calculate(r)

        # assertion
        self.assertEqual(resultado_esperado, resutado_obtido)

    def test_deve_ser_igual(self):
        # cenario
        resultado_esperado = "A=31819.3103"

        r = 100.64

        # acao
        resutado_obtido = AreaOfCircle.calculate(r)

        # assertion
        self.assertEqual(resultado_esperado, resutado_obtido)


    def test_calculate_area_circle_deve_retornar_false(self):
        # cenario
        resultado_esperado = "A=12.5664"
        r = 150.00

        # acao
        resutado_obtido = AreaOfCircle.calculate(r)

        # assertion
        self.assertNotEqual(resultado_esperado, resutado_obtido)


if __name__ == '__main__':
    unittest.main()

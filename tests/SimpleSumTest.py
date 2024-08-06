import unittest

from solucoes.SimpleSum import SimpleSum


class SimpleSumTestCase(unittest.TestCase):
    def test_soma_deve_retornar_40(self):
        # cenario
        a = 30
        b = 10
        resultado_esperado = "SOMA = 40"

        # ação
        resultado_obtido = SimpleSum(a, b).calculate()

        # assertion
        self.assertEqual(resultado_esperado, resultado_obtido, "Resultados iguais, teste ok")

    def test_soma_deve_retornar_menos_20(self):
        # cenario
        a = -30
        b = 10
        resultado_esperado = "SOMA = -20"

        # ação
        resultado_obtido = SimpleSum(a, b).calculate()

        # assertion
        self.assertEqual(resultado_esperado, resultado_obtido, "Resultados iguais")

    def test_soma_deve_retornar_0(self):

        # cenario
        a = 0
        b = 0
        resultado_esperado = "SOMA = 0"

        # acao
        resultado_obtido = SimpleSum(a, b).calculate()

        # assertion
        self.assertEqual(resultado_esperado, resultado_obtido, "Resultados iguais")

    def test_soma_diferente_de_0_quando_a_1_b_0(self):

        # cenario
        a = 1
        b = 0
        resultado_esperado = "SOMA = 0"

        # acao
        resultado_obtido = SimpleSum(a, b).calculate()

        # assertion
        self.assertNotEqual("SOMA = 0", resultado_obtido, "Resultados Diferentes")
        self.assertNotEqual(resultado_esperado, resultado_obtido, "Resultados iguais")


if __name__ == '__main__':
    unittest.main()

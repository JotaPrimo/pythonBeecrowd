import unittest

from solucoes.SimpleProduct import SimpleProduct


class SimpleProductTest(unittest.TestCase):
    def test_produto_deve_ser_igual_27(self):
        # Cenário
        first_value = 3
        second_value = 9
        resultado_esperado = "PROD = 27"

        # Ação
        resultado_obtido = SimpleProduct(first_value, second_value).calculate_product()

        # Asserção
        self.assertEqual(resultado_obtido, resultado_esperado)

    def test_produto_deve_ser_igual_300_negativo(self):
        # Cenário
        first_value = -30
        second_value = 10
        resultado_esperado = "PROD = -300"

        # Ação
        resultado_obtido = SimpleProduct(first_value, second_value).calculate_product()

        # asserssão
        self.assertEqual(resultado_obtido, resultado_esperado)

    def test_produto_deve_ser_igual_0(self):
        # cenário
        first_value = 0
        second_value = 9
        resultado_esperado = "PROD = 0"

        # ação
        resultado_obtido = SimpleProduct(first_value, second_value).calculate_product()

        # assertion
        self.assertEqual(resultado_obtido, resultado_esperado)


if __name__ == '__main__':
    unittest.main()

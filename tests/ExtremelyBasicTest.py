import unittest

from solucoes import ExtremelyBasic


class ExtremelyBasicTestCase(unittest.TestCase):
    def test_deve_retornar_true_quando_valores_forem_iguais(self):
        # cenario
        A = 10
        B = 9

        #ação
        resposta = ExtremelyBasic.somar_dois_valores(A, B)

        #asserção
        self.assertEqual(resposta, "X = 19")

    def test_deve_ser_igual(self):
        # CENARIO
        A = -10
        B = 4

        #ACAO
        resposta = ExtremelyBasic.somar_dois_valores(A, B)

        # assertion
        self.assertEqual(resposta, "X = -6")

    def test_deve_ser_igual2(self):
        # cenario
        A = 15
        B = -7

        "acao"
        resultant = ExtremelyBasic.somar_dois_valores(A, B)

        #assertion
        self.assertEqual(resultant, "X = 8")

    def test_nao_deve_ser_igual(self):
        # cenario
        A = 15
        B = -7

        #acao
        resultado = ExtremelyBasic.somar_dois_valores(A, B)

        #assertion
        self.assertNotEqual(resultado, "X = 7")


if __name__ == '__main__':
    unittest.main()

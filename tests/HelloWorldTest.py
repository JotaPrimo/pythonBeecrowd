import unittest

from solucoes import HelloWorld


class TestHelloWOrldCase(unittest.TestCase):

    # metodos de teste
    def test_hello_world(self):
        self.assertEqual(HelloWorld.hello_world(), "Hello World!")

    def test_deve_retornar_true_quando_frase_for_diferente(self):
        self.assertNotEqual(HelloWorld.hello_world(), "Hello Worlds!")


# Executa os testes
if __name__ == '__main__':
    unittest.main()

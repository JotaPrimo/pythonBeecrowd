class SimpleSum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        resultado = self.a + self.b
        return f"SOMA = {resultado}"

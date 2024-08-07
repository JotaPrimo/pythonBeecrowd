class Difference:
    def __init__(self, a: int, b: int, c: int, d: int):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def calculate(self) -> str:
        prod_ab = self._a * self._b
        prod_bc = self._c * self._d
        diferenca = prod_ab - prod_bc
        return f"DIFERENCA = {diferenca}"

import pytest

from solucoes.Difference import Difference


class TestDifference:

    @pytest.mark.parametrize("a, b, c, d, resultado_esperado", [
        (5, 6, 7, 8, "DIFERENCA = -26"),
        (0, 0, 7, 8, "DIFERENCA = -56"),
        (5, 6, -7, 8, "DIFERENCA = 86"),
    ])
    def test_calculate(self, a: int, b: int, c: int, d: int, resultado_esperado: str):
        resultado_obtido = Difference(a, b, c, d).calculate()
        assert resultado_obtido == resultado_esperado


import pytest

from solucoes.salary import Salary


class TestSalary:
    @pytest.mark.parametrize("numero_funcionario, horas_trabalhadas, valor_hora, resultado_esperado", [
        (25, 100, 5.50, "NUMBER = 25\n SALARY = U$ 550.00\n"),
        (1, 200, 20.50, "NUMBER = 1\n SALARY = U$ 4100.00\n"),
        (6, 145, 15.55, "NUMBER = 6\n SALARY = U$ 2254.75\n"),
    ])
    def test_salary(self, numero_funcionario, horas_trabalhadas, valor_hora, resultado_esperado):
        resultado_obtido = Salary(numero_funcionario, horas_trabalhadas, valor_hora).get_infos_salario()
        assert resultado_obtido == resultado_esperado

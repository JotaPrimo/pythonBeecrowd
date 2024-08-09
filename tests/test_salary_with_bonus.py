import pytest

from solucoes.salary_with_bonus import SalaryWithBonus


class TestSalaryWithBonus:
    @pytest.mark.parametrize("seller_name, salary, total_sales, resultado_esperado", [
        ('JOAO', '500.00', '1230.30', 'TOTAL = R$ 684.54'),
        ('PEDRO', '700.00', '0.00', 'TOTAL = R$ 700.00'),
        ('MANGOJATA', '1700.00', '1230.50', 'TOTAL = R$ 1884.58')
    ])
    def test_calculate_bonus(self, seller_name: str, salary: str, total_sales: str, resultado_esperado: str):
        salary_with_bonus = SalaryWithBonus(seller_name, salary, total_sales)
        salary_with_bonus.add_bonus_in_salary()

        resultado_obtido = f"TOTAL = R$ {salary_with_bonus.salary}"

        assert resultado_obtido == resultado_esperado

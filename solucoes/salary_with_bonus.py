from solucoes.utils.number_utils import NumberUtils
from decimal import Decimal, getcontext


class SalaryWithBonus:
    PERCENTUAL: Decimal = 15

    def __init__(self, seller_name: str, salary: str, total_sales: str):
        self._seller_name = seller_name
        self._salary = SalaryWithBonus.converte_value_for_decimal(salary)
        self._total_sales = SalaryWithBonus.converte_value_for_decimal(total_sales)

    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value

    @property
    def salary(self) -> Decimal:
        return self._salary

    @salary.setter
    def salary(self, value: Decimal):
        self._salary = value

    @property
    def total_sales(self) -> Decimal:
        return self._total_sales

    @total_sales.setter
    def total_sales(self, value: Decimal):
        self._total_sales = value

    @classmethod
    def converte_value_for_decimal(cls, value) -> Decimal:
        getcontext().prec = 10
        return Decimal(value)

    def calculate_bonus(self) -> Decimal:
        percent = Decimal((self.PERCENTUAL / 100))
        bonus = Decimal(self.total_sales * percent)
        return NumberUtils.truncate_to_two_decimal_places(bonus)

    def add_bonus_in_salary(self):
        bonus = self.calculate_bonus()
        self.salary += bonus

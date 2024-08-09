import math

from decimal import Decimal, getcontext


class NumberUtils:

    TWO_PLACES = 28

    @staticmethod
    def format_number_one_decimal_place(number: float) -> str:
        return f"{number:.1}"

    @staticmethod
    def format_number_four_decimal_places(number: float) -> str:
        return f"{number:.4f}"

    @staticmethod
    def format_number_five_decimal_places(number: float) -> str:
        return f"{number:.5f}"

    @staticmethod
    def truncate_to_two_decimal_places(value: Decimal) -> Decimal:
        getcontext().prec = NumberUtils.TWO_PLACES
        valor_decimal = Decimal(value)
        return valor_decimal.quantize(Decimal('0.01'))



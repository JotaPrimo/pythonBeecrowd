class NumberUtils:

    @staticmethod
    def format_number_one_decimal_place(number: float) -> str:
        return f"{number:.1}"

    @staticmethod
    def format_number_four_decimal_places(number: float) -> str:
        return f"{number:.4f}"

    @staticmethod
    def format_number_five_decimal_places(number: float) -> str:
        return f"{number:.5f}"



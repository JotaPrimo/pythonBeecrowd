from solucoes.utils.number_utils import NumberUtils


class AverageOne:
    WEIGHT_FIRST_GRADE = 3.5
    WEIGHT_SECOND_GRADE = 7.5
    TOTAL_WEIGHT_GRADE = 11

    def __init__(self, first_grade, second_grade):
        self.first_grade = first_grade
        self.second_grade = second_grade

    def calculate_average(self) -> str:
        grade_one = self.first_grade * self.WEIGHT_FIRST_GRADE
        grade_second = self.second_grade * self.WEIGHT_SECOND_GRADE
        final_average = (grade_one + grade_second) / self.TOTAL_WEIGHT_GRADE

        return NumberUtils.format_number_five_decimal_places(final_average)

    def process(self) -> str:
        # print(self.calculate_average())
        return f"MEDIA = {self.calculate_average()}"

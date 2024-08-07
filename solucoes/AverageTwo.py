
class AverageTwo:
    WEIGHT_GRADE_A = 2
    WEIGHT_GRADE_B = 3
    WEIGHT_GRADE_C = 5
    WEIGHT_ALL_GRADE = 10

    def __init__(self, grade_a, grade_b, grade_c):
        self.grade_a = grade_a
        self.grade_b = grade_b
        self.grade_c = grade_c

    def weight_grade_a(self):
        return self.grade_a * self.WEIGHT_GRADE_A

    def weight_grade_b(self):
        return self.grade_b * self.WEIGHT_GRADE_B

    def weight_grade_c(self):
        return self.grade_c * self.WEIGHT_GRADE_C

    def calculate(self) -> str:
        weight_grades = self.weight_grade_a() + self.weight_grade_b() + self.weight_grade_c()
        average = weight_grades / self.WEIGHT_ALL_GRADE
        return f'MEDIA = {average:.1f}'

import pytest

from solucoes.AverageTwo import AverageTwo


@pytest.mark.parametrize("grade_a, grade_b, grade_c, expected_result", [
    (5.0, 6.0, 7.0, "MEDIA = 6.3"),
    (5.0, 10.0, 10.0, "MEDIA = 9.0"),
    (10.0, 10.0, 5.0, "MEDIA = 7.5"),
])
def test_calculate_average_grade(grade_a, grade_b, grade_c, expected_result):
    average = AverageTwo(grade_a, grade_b, grade_c).calculate()

    # assert
    assert average == expected_result


@pytest.mark.parametrize("grade_a, grade_b, grade_c, expected_result", [
    (6.0, 6.0, 7.0, "MEDIA = 6.3"),
    (7.0, 10.0, 10.0, "MEDIA = 9.0"),
    (9.0, 10.0, 5.0, "MEDIA = 7.5"),
])
def test_calculate_average_grade(grade_a, grade_b, grade_c, expected_result):
    average = AverageTwo(grade_a, grade_b, grade_c).calculate()
    assert average != expected_result

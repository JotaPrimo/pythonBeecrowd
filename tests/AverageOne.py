import pytest

from solucoes.AverageOne import AverageOne


@pytest.mark.parametrize("first_grade, second_grade, expected_result", [
    (5.0, 7.1, "MEDIA = 6.43182"),
    (0.0, 7.1, "MEDIA = 4.84091"),
    (10.0, 10.0, "MEDIA = 10.00000"),
])
def test_calculate_average_grade(first_grade, second_grade, expected_result):
    # Ação
    result_returned = AverageOne(first_grade, second_grade).process()

    # Assertions
    assert result_returned == expected_result


@pytest.mark.parametrize("first_grade, second_grade, expected_result", [
    (5.0, 7.1, "MEDIA = 5.43182"),
    (0.0, 7.1, "MEDIA = 6.84091"),
    (10.0, 10.0, "MEDIA = 10.01000"),
])
def test_calculate_average_grade_should_return_incorrect_value(first_grade, second_grade, expected_result):
    result_returned = AverageOne(first_grade, second_grade).process()
    assert result_returned != expected_result

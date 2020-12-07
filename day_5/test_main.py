import pytest

from day_5 import main


@pytest.mark.parametrize("pass_number, result_row, result_column",
                         [("FBFBBFFRLR", 44, 5),
                          ("BFFFBBFRRR", 70, 7),
                          ("FFFBBBFRRR", 14, 7),
                          ("BBFFBBFRLL", 102, 4)])
def test_get_row_column(pass_number, result_row, result_column):
    returned_row, returned_column = main.get_row_column(pass_number)
    assert returned_row == result_row
    assert returned_column == result_column

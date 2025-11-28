from speed_calc import calculate_speed
import pytest

def test_calculate_speed_normal():
    assert calculate_speed(100, 2) == 50

def test_calculate_speed_fraction():
    assert calculate_speed(50, 0.5) == 100

def test_calculate_speed_zero_time():
    with pytest.raises(ZeroDivisionError):
        calculate_speed(10, 0)
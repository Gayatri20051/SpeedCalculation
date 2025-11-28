import pytest
from speed import calculate_speed   # rename "speed.py" to your actual filename

def test_normal_speed():
    assert calculate_speed(100, 10) == 10

def test_decimal_speed():
    assert calculate_speed(45.5, 5.5) == pytest.approx(8.2727, rel=1e-3)

def test_zero_time():
    assert calculate_speed(50, 0) == "Error: Time cannot be zero"

def test_negative_distance():
    assert calculate_speed(-100, 10) == -10

def test_negative_time():
    assert calculate_speed(100, -5) == -20
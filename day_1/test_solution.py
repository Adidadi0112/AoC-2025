import pytest
from .safe_dial import SafeDial

def test_input():
    return ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

def test_object():
    safe = SafeDial()
    assert safe.current_number == 50 and len(safe.dial) == 100

def test_rotation_in_bounds_right():
    safe = SafeDial()
    safe.rotate(5)
    assert safe.current_number == 55

def test_rotation_in_bounds_left():
    safe = SafeDial()
    safe.rotate(-10)
    assert safe.current_number == 40

def test_rotation_out_of_bounds_right():
    safe = SafeDial()
    safe.rotate(56)
    assert safe.current_number == 6

def test_rotation_out_of_bounds_left():
    safe = SafeDial()
    safe.rotate(-68)
    assert safe.current_number == 82

def test_input_sequence():
    safe = SafeDial()
    sequence = safe.parse(test_input())
    for number in sequence:
        safe.rotate(number)
    assert safe.zeros_sum == 3
    
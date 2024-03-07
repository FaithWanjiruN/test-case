import pytest
from roman import roman_to_integer, main

def test_single_character():
    assert roman_to_integer("I") == 1
    assert roman_to_integer("V") == 5
    assert roman_to_integer("X") == 10

def test_multiple_characters():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("IV") == 4
    assert roman_to_integer("XLIX") == 49

def test_invalid_characters():
    with pytest.raises(ValueError):
        roman_to_integer("IIII")
    with pytest.raises(ValueError):
        roman_to_integer("VV")
    with pytest.raises(ValueError):
        roman_to_integer("LL")

def test_start_with_I():
    assert roman_to_integer("I") == 1
    assert roman_to_integer("II") == 2
    assert roman_to_integer("III") == 3

def test_largest_possible_numeral():
    assert roman_to_integer("MMMCMXCIX") == 3999

if __name__ == "__main__":
    print(roman_to_integer("MCMXCIV"))  # Output: 1994
    test_single_character()
    test_multiple_characters()
    test_invalid_characters()
    test_start_with_I()  # Add the new test case
    test_largest_possible_numeral()  # Add the new test case
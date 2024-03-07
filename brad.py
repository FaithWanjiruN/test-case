import pytest
roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman_num):
    """
    Converts a Roman numeral string to an integer.

    Args:
        roman_num: The Roman numeral string to convert.

    Returns:
        The integer equivalent of the Roman numeral.
    """

    result = 0
    prev = 0

    for char in roman_num:
        current = roman_numerals[char]

        # Check for invalid subtractions
        if prev > current and prev not in [10, 100, 1000]:
            raise ValueError("Invalid Roman numeral: cannot subtract large value from smaller one")

        if prev < current:
            # Handle subtractions only for specific cases (I, X, C)
            if prev not in [1, 10, 100]:
                raise ValueError("Invalid Roman numeral: invalid subtraction without specific values")
            result += current - prev
        else:
            result += current

        prev = current
        return result


# Asserting tests

def test_empty_string():
    assert roman_to_int("") == 0


def test_single_character():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10


def test_multiple_characters():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("XLIX") == 49


def test_complex_cases():
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MDXL") == 1540


def test_invalid_characters():
    with pytest.raises(ValueError):
        roman_to_int("IIII")
    with pytest.raises(ValueError):
        roman_to_int("VV")
    with pytest.raises(ValueError):
        roman_to_int("LL")


def test_start_with_I():
    assert roman_to_int("I") == 1
    assert roman_to_int("II") == 2
    assert roman_to_int("III") == 3
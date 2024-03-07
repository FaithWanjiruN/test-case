#test cases
import pytest
from roman import roman_to_integer, main

#Single letters
def test_single_letters():
    assert roman_to_integer("II") == 2
    assert roman_to_integer("V") == 5
    assert roman_to_integer("XI") == 11

#Many letters
def test_many_letters():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("V") == 5
    assert roman_to_integer("LXXVIII") == 78

#Subtractive notation(SN)
def test_subtractive_notation():
    assert roman_to_integer("IV") == 4

#With and without SN
def test_specific_numeral_XIV():
    assert roman_to_integer("XIV") == 14

#Repetition
def test_repeated_letters():
    assert roman_to_integer("II") == 2

#Invalid letters
def test_invalid_letters():
    with pytest.raises(ValueError):
        roman_to_integer("III")
    with pytest.raises(ValueError):
        roman_to_integer("VV")
    with pytest.raises(ValueError):
        roman_to_integer("LL")

#First number is I
def test_start_with_I():
    assert roman_to_integer("I") == 1
    assert roman_to_integer("II") == 2
    assert roman_to_integer("III") == 3

#Invalid and valid letter
def test_invalid_and_valid_letters():
    with pytest.raises(ValueError):
        roman_to_integer("XIZ")  

    assert roman_to_integer("XII") == 12  

#Null input
def test_null_input():
    assert roman_to_integer("") == 0


if __name__ == "__main__":
    test_single_letters()
    test_many_letters()
    test_subtractive_notation()
    test_specific_numeral_XIV()
    test_repeated_letters()
    test_invalid_letters()
    test_start_with_I()  
    test_invalid_and_valid_letters() 
    test_null_input()
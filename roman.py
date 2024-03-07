def roman_to_integer(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0
    
    for numeral in reversed(roman):
        try:
            current_value = roman_numerals[numeral]
        except KeyError:
            # Invalid Roman numeral, return None
            return None
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result



def main():
    while True:
        roman_input = input("Enter a Roman numeral: ").upper()
        
        try:
            result = roman_to_integer(roman_input)
            print(f"The integer equivalent of {roman_input} is: {result}")
            break  # Break out of the loop if input is valid
        except KeyError:
            print("Invalid Roman numeral input. Please provide a valid Roman numeral. Try again.")
        if not roman_input:
            print("Empty input. Please provide a valid Roman numeral.")
            continue  # Continue the loop to prompt for input again

if __name__ == "__main__":
    main()

def test_single_letter_roman():
    assert roman_to_integer('I') == 1
    assert roman_to_integer('V') == 5
    assert roman_to_integer('X') == 10
    assert roman_to_integer('L') == 50
    assert roman_to_integer('C') == 100
    assert roman_to_integer('D') == 500
    assert roman_to_integer('M') == 1000

def test_invalid_input():
    # Assuming your script handles input validation, you can test it with invalid inputs
    assert roman_to_integer('AB') is None
    assert roman_to_integer('XYZ') is None
    assert roman_to_integer('IVX') is None
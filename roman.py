def roman_to_integer(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0
    
    for numeral in reversed(roman):
        current_value = roman_numerals[numeral]
        
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

if __name__ == "__main__":
    main()

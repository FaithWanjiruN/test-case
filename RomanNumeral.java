import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class RomanNumeral {

    private static Map<Character, Integer> map;

    static {
        map = new HashMap<Character, Integer>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
    }

    public int romanToInt(String s) {
        int convertedNumber = 0;
        for (int i = 0; i < s.length(); i++) {
            int currentNumber = map.get(s.charAt(i));
            int next = i + 1 < s.length() ? map.get(s.charAt(i + 1)) : 0;
            if (currentNumber >= next) {
                convertedNumber += currentNumber;
            } else {
                convertedNumber -= currentNumber;
            }
        }
        return convertedNumber;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        boolean validInput = false;
        String userInput = "";

        while (!validInput) {
            System.out.print("Enter a single Roman letter: ");
            userInput = scanner.nextLine().toUpperCase();

            if (userInput.length() == 1 && map.containsKey(userInput.charAt(0))) {
                validInput = true;
            } else {
                System.out.println("Invalid input. Please enter a single Roman letter.");
            }
        }

        RomanNumeral romanNumeral = new RomanNumeral();
        int result = romanNumeral.romanToInt(userInput);if (validInput) {
            
        }
        System.out.println("Converted integer: " + result);
        scanner.close();
    }
}
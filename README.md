String Calculator

Overview

This module implements a string calculator function `add` that takes a string of numbers separated by delimiters and returns their sum. The function supports:
- Comma (`,`) and newline (`\n`) as default delimiters.
- Custom single-character and multi-character delimiters.
- Error handling for negative numbers.

Additionally, a test suite using `unittest` is provided to validate the function's correctness.
Function: add(numbers: str) -> int
Parameters
- `numbers` (str): A string containing numbers separated by default or custom delimiters.
Returns
- `int`: The sum of all numbers in the input string. If the input is empty, returns `0`.
Functionality
1. If the input string is empty, return `0`.
2. Support custom delimiters by checking for the `//` prefix:
   - Single-character custom delimiters (e.g., `//;\n1;2`).
   - Multi-character custom delimiters (e.g., `//[***]\n1***2***3`).
3. Split the numbers using the determined delimiter(s) and newlines.
4. Convert extracted numbers to integers while handling whitespace.
5. If negative numbers are present, raise a `ValueError` with the list of negative numbers.
6. Return the sum of the valid numbers.
Example Usage
add("1,2,3")  # Returns 6
add("1\n2,3")  # Returns 6
add("//;\n1;2")  # Returns 3
add("//[***]\n1***2***3")  # Returns 6
Exception Handling
If the input contains negative numbers, a `ValueError` is raised:
add("1,-2,3,-4")  # Raises ValueError: negative numbers not allowed -2,-4
Unit Tests
The module includes a test suite (`TestStringCalculator`) using `unittest`.
Test Cases
1. **Empty String**: Returns `0`.
2. **Single Number**: Returns the number itself.
3. **Two Numbers**: Returns the sum of two numbers.
4. **Multiple Numbers**: Returns the sum of all numbers.
5. **Newline as Delimiter**: Handles `\n` as a separator.
6. **Custom Delimiters**: Supports both single-character and multi-character delimiters.
7. **Negative Numbers**: Raises an exception listing all negative numbers.
8. **Multiple Negative Numbers**: Ensures multiple negatives are reported correctly.
9. **Custom Delimiter with Newline**: Handles a custom delimiter and newline together.
10. **Custom Delimiter with Special Characters**: Supports delimiters containing special characters.

if __name__ == "__main__":
    unittest.main(exit=False)
Summary
- Implements a string calculator that supports multiple delimiters and error handling.
- Provides a robust set of unit tests to validate the functionality.
- Ensures proper exception handling for negative numbers.

Test cases : All test cases passed Successfull"

0/python.exe c:/Users/shivam.taneja/Desktop/string_td/string_calculator/string_tdd.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK

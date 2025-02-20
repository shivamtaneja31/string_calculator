import re
import unittest

def add(numbers: str) -> int:
    """
    Adds numbers provided in a string, supporting custom delimiters and handling negatives.

    Args:
        numbers (str): A string of numbers separated by delimiters (default: comma or newline).
                       Custom delimiters can be specified using the format: `//[delimiter]\\n[numbers]`.

    Returns:
        int: The sum of the numbers.

    Raises:
        ValueError: If any negative numbers are present, an exception is raised with the list of negatives.
    """
    if not numbers:
        return 0

    delimiter = ','  # Default delimiter

    # Handle custom delimiters
    if numbers.startswith("//"):
        if numbers.startswith("//["):
            # Extract multi-character or special-character delimiter
            match = re.match(r"//\[(.+)\]\n(.*)", numbers)
            if match:
                delimiter, numbers = match.groups()
                delimiter = re.escape(delimiter)  # Escape special characters
        else:
            # Extract single-character delimiter
            match = re.match(r"//(.+)\n(.*)", numbers)
            if match:
                delimiter, numbers = match.groups()
                delimiter = re.escape(delimiter)  # Escape special characters

    # Split using delimiter or newline
    numbers = re.split(fr"{delimiter}|\n", numbers)

    # Process numbers and handle negatives
    num_list = []
    negatives = []
    for num in numbers:
        num = num.strip()
        if num:
            value = int(num)
            if value < 0:
                negatives.append(value)
            num_list.append(value)

    # Raise exception if negatives are found
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(num_list)

class TestStringCalculator(unittest.TestCase):
    """
    Test cases for the `add` function in the String Calculator.
    """

    def test_empty_string(self):
        """Test that an empty string returns 0."""
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        """Test that a single number returns the number itself."""
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        """Test that two numbers separated by a comma are summed correctly."""
        self.assertEqual(add("1,5"), 6)
    
    def test_multiple_numbers(self):
        """Test that multiple numbers separated by commas are summed correctly."""
        self.assertEqual(add("1,2,3,4"), 10)
    
    def test_newline_as_delimiter(self):
        """Test that numbers separated by newlines are summed correctly."""
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        """Test that a custom delimiter (;) is handled correctly."""
        self.assertEqual(add("//;\n1;2"), 3)
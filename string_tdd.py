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
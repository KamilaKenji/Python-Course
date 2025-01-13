def first_repeated_number(numbers):
    """Find the first repeated number in the list."""
    seen = set()  # To track numbers we've seen
    for num in numbers:
        if num in seen:
            return num  # Return the first repeated number
        seen.add(num)
    return None  # Return None if no repeated number is found


# Test the function
sample = [2, 1, 3, 4, 2]
print(first_repeated_number(sample))  # Output: 2


def roman_to_integer(roman):
    """Convert a Roman numeral string to an integer."""
    # Mapping of Roman numerals to values
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for i in range(len(roman)):
        # Check if the current symbol is smaller than the next one (subtraction rule)
        if i < len(roman) - 1 and values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]]
        else:
            total += values[roman[i]]

    return total


# Test the function
sample = "XIX"
print(roman_to_integer(sample))  # Output: 19


def find_smallest_number(numbers):
    """Find the smallest number in the list."""
    smallest = numbers[0]  # Assume the first number is the smallest
    for number in numbers:
        if number < smallest:  # Update if a smaller number is found
            smallest = number
    return smallest


# Test the function
sample = [3, 4, -1, 10, 12]
print(find_smallest_number(sample))  # Output: -1

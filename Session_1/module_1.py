from typing import List


def find_pair_with_target_sum(numbers):
    checked_numbers = []  # List to store numbers we've checked so far

    for number in numbers:
        complement = target - number  # Calculate complement
        if complement in checked_numbers:  # Check if complement is already in checked numbers
            return [complement, number]  # Return the pair
        checked_numbers.append(number)  # Add current number to the checked list

    return []  # Return empty list if no pair is found

# Test the function
sample = [3, 4, -1, 10, 12]
target = 2
print(find_pair_with_target_sum(sample))  # Output: [3, -1]



def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
        num //= 10  # Remove the last digit
    return reversed_num

# Test the function
sample = 130
print(reverse_number(sample))  # Output: 31



def first_repeated_number(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Compare each number with the rest
            if numbers[i] == numbers[j]:
                return numbers[i]  # Return the first repeated number
    return -1  # Return -1 if no duplicates are found

# Test the function
sample = [2, 1, 3, 4, 2]
print(first_repeated_number(sample))  # Output: 2


def roman_to_integer(roman):
    # Mapping of Roman numerals to values
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
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
    smallest = numbers[0]  # Assume the first number is the smallest
    for number in numbers:
        if number < smallest:  # Update if a smaller number is found
            smallest = number
    return smallest

# Test the function
sample = [3, 4, -1, 10, 12]
print(find_smallest_number(sample))  # Output: -1


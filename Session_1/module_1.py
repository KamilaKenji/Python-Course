def task_1(numbers, target):
    """
    Find a pair of numbers in the list that add up to the target sum.

    Args:
        numbers (list[int]): List of integers.
        target (int): Target sum.

    Returns:
        list[int]: A list containing the pair of numbers that sum to the target.
    """
    complements = {}
    for num in numbers:
        if num in complements:
            return [complements[num], num]
        complements[target - num] = num
    return []


def task_2(num):
    """
    Reverse an integer without using string operations.

    Args:
        num (int): The integer to reverse.

    Returns:
        int: The reversed integer.
    """
    is_negative = num < 0
    num = abs(num)
    result = 0

    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num //= 10

    return -result if is_negative else result


def task_3(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return -1


def task_4(roman):
    """
    Convert a Roman numeral string to an integer.

    Args:
        roman (str): Roman numeral string.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for i in range(len(roman)):
        if i < len(roman) - 1 and values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]]
        else:
            total += values[roman[i]]

    return total


def task_5(numbers):
    """
    Find the smallest number in the list without using the min() function.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        int: The smallest number in the list.
    """
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

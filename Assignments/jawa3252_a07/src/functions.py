"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-10"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(number):
    """
    -------------------------------------------------------
    takes an integer greater than 0 as a parameter
    and returns a list of the factors that make up that
    number excepting the number itself.
    Use: list_factors(integer)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        factors list of the factors that make up that number
        excepting the number itself (list of int)
    ------------------------------------------------------
    """

    factors = []

    if (number == 1):
        factors.append(1)

    elif (number > 0):
        for i in range (1, number, 1):
            if number % i == 0:
                factors.append(i)

    else:
        factors.append("Invalid number")

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    number_list = []
    user_input = 1

    while (user_input != 0):

        user_input = int(input("Enter a positive number:"))

        if (user_input > 0):
            number_list.append(user_input)

    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    index_list = []

    for i in range (0, len(numbers), 1):
        if (target_number == numbers[i]):
            index_list.append(i)

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for x in range(0, len(subtrahend), 1):
        for y in range(len(minuend) - 1, -1, -1):
            if (subtrahend[x] == minuend[y]):
                minuend.remove(subtrahend[x])

    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    in_order = True
    index = 0
    current = numbers[0]

    for i in range(0, len(numbers)):

        if (current > numbers[i]):
            in_order = False
            index = i

            break

        else:
            in_order = True
            index = -1
            current = numbers[i]

    return in_order, index

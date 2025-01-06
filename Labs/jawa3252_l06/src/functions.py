"""
-------------------------------------------------------
function, lab 6
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-23"
-------------------------------------------------------
"""
WEEKS = 6


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, finish + 1, increment):
        total += i

    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    if height > 0:
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            chars = char * (2 * i + 1)
            print(f"{spaces}{chars}")
    return None


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, width + 1):
        print(char * i)

    for i in range(width - 1, 0, -1):
        print(char * i)

    return None


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """

    final_value = 0
    print(f"Year{'Value $':>14s}")
    print(f"{'-':-^18s}")

    for i in range(0, years, 1):
        formatted_value = "{:,.2f}".format(value)
        print(f"{i:2d}{formatted_value:>16s}")
        value *= (1 + rate / 100)

    formatted_value2 = "{:,.2f}".format(value)
    print(f"{years:2d}{formatted_value2:>16s}")
    final_value = value

    return final_value


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6-week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total_hours = 0.0

    for week in range(1, WEEKS + 1):
        print(f"Week {week}")
        for ia in range(1, ia_count + 1):
            hours = float(input(f"  Marking hours for IA {ia}: "))
            total_hours += hours

    return total_hours

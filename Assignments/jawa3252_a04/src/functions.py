"""
-------------------------------------------------------
Assignment 4, Functions
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-12"
-------------------------------------------------------
"""
# Imports

# Constants


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    day = ""

    if day_num == 1:
        day = "Sunday"

    elif day_num == 2:
        day = "Monday"

    elif day_num == 3:
        day = "Tuesday"

    elif day_num == 4:
        day = "Wednesday"

    elif day_num == 5:
        day = "Thursday"

    elif day_num == 6:
        day = "Friday"

    elif day_num == 7:
        day = "Saturday"

    else:
        day = "Error"

    return day


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    pollution_level = ""

    if 0 <= air_quality_index <= 50:
        pollution_level = "Good"

    elif 51 <= air_quality_index <= 100:
        pollution_level = "Moderate"

    elif 101 <= air_quality_index <= 150:
        pollution_level = "Unhealthy"

    elif 151 <= air_quality_index <= 200:
        pollution_level = "Unhealthy"

    elif 201 < air_quality_index <= 300:
        pollution_level = "Very Unhealthy"

    elif 301 <= air_quality_index:
        pollution_level = "Hazardous"

    else:
        pollution_level = "Error"

    return pollution_level


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    average = 0.0
    if val1 > val2:
        if val2 > val3:
            average = val1 + val2

        else:
            average = val1 + val3

    elif val2 > val3:
        if val3 > val1:
            average = val2 + val3

        else:
            average = val1 + val2

    elif val3 > val1:
        if val1 > val2:
            average = val1 + val3

        else:
            average = val3 + val2

    average /= 2

    return average


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    rgb_colour = ""

    if (rgb_colour1 == "red") & (rgb_colour2 == "red"):
        rgb_colour = "red"

    elif (rgb_colour1 == "blue") & (rgb_colour2 == "blue"):
        rgb_colour = "blue"

    elif (rgb_colour1 == "green") & (rgb_colour2 == "green"):
        rgb_colour = "green"

    elif ((rgb_colour1 == "red") & (rgb_colour2 == "blue")) | ((rgb_colour1 == "blue") & (rgb_colour2 == "red")):
        rgb_colour = "fuchsia"

    elif ((rgb_colour1 == "red") & (rgb_colour2 == "green")) | ((rgb_colour1 == "green") & (rgb_colour2 == "red")):
        rgb_colour = "yellow"

    elif ((rgb_colour1 == "blue") & (rgb_colour2 == "green")) | ((rgb_colour1 == "green") & (rgb_colour2 == "blue")):
        rgb_colour = "aqua"

    else:
        rgb_colour = "Error"

    return rgb_colour


def hoo_rah(number):
    """
    -------------------------------------------------------
    Returns a string based on the input number:
        "Hoo" if the number is evenly divisible by 2
        "Rah" if the number is evenly divisible by 7
        "Hoo Rah" if the number is evenly divisible by both 2 and 7
        "Zip" if the number is none of the above.
    Returns "Error" if the input number is not an integer.
    Use: result = hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number - an integer to determine divisibility (int)
    Returns:
        result - a string indicating divisibility or "Error" (str)
    ------------------------------------------------------
    """
    if number % 2 == 0 and number % 7 == 0:
        result = "Hoo Rah"
    elif number % 2 == 0:
        result = "Hoo"
    elif number % 7 == 0:
        result = "Rah"
    else:
        result = "Zip"

    return result

"""
-------------------------------------------------------
Functions, Lab 5
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-09"
-------------------------------------------------------
"""
# Imports

# Constants
GRAVITY = 9.8
INFANTAGE = 3
SENIORAGE = 65
STUDENTAGELOW = 10
STUDENTAGEHIGH = 18
ADULTAGELOW = 18
ADULTAGEHIGH = 65
INFANT = 0.00
SENIOR = 4.00
STUDENTSCHOOL = 1.00
STUDENT = 3.00
ADULT = 5
KID = 2


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    message = ""
    weight = mass * GRAVITY

    if weight > 1000:
        message = "heavy"

    elif 10 < weight < 1000:
        message = "average"

    else:
        message = "light"

    return weight, message


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
                 False otherwise (boolean)
    ------------------------------------------------------
    """
    result = ""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False

    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    category = ""
    if speed > 117:
        category = "Hurricane"

    elif 89 < speed <= 117:
        category = "Whole Gale"

    elif 62 < speed <= 88:
        category = "Gale Winds"

    elif 39 < speed <= 61:
        category = "Strong Wind"

    elif speed < 0:
        category = "Unknown"

    else:
        category = "Breeze"

    return category


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    location = ""

    if x == 0 and y < 0:
        location = "Y-Axis"

    elif x == 0 and y > 0:
        location = "Y-Axis"

    elif y == 0 and x > 0:
        location = "X-Axis"

    elif y == 0 and x < 0:
        location = "X-Axis"

    elif y > 0 and x > 0:
        location = "Quadrant 1"

    elif y < 0 and x > 0:
        location = "Quadrant 4"

    elif y < 0 and x < 0:
        location = "Quadrant 3"

    elif y > 0 and x < 0:
        location = "Quadrant 2"

    else:
        location = "Origin"

    return location


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """

    age = int(input("How old are you? "))
    price = 0.0

    if age < INFANTAGE:
        price = INFANT

    elif age >= SENIORAGE:
        price = SENIOR

    elif STUDENTAGELOW <= age < STUDENTAGEHIGH:
        student = input("Are you a student? (enter 'Y' for yes, 'N' for no.): ")
        if student == "Y":
            price = STUDENTSCHOOL
        else:
            price = STUDENT

    elif ADULTAGELOW <= age < ADULTAGEHIGH:
        price = ADULT

    else:
        price = KID

    return price


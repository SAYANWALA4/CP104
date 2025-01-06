"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-30"
-------------------------------------------------------
"""
# Imports
from random import randint

# Constants
TAX = 3.625 / 100
OVERTIME_RATE = 1.5
OVERTIME = 40


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0

    while(high != number):
        count += 1
        user_guess = int(input("Guess:"))

        if (user_guess > number):
            print("Too high, try again.")

        elif (user_guess < number):
            print("Too low, try again")

        elif(user_guess == number):
            print("Congratulations - good guess!")
            high = number

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    current = 0
    previous = 1
    power = 0
    while (previous != current):

        current = 2 ** power

        if (current >= target and target >= previous):
            previous = current

        elif(current > target and previous > target):
            power -= 2

        else:
            previous = current
            current += 1

        power += 1

    return current


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    minimum = 0.0
    maximum = 0.0
    total = 0.0
    count = 0

    first_value = float(input("First positive value: "))
    if first_value < 0:
        print("The first number must be a positive number.")
        minimum = maximum = total = average = None
    else:
        minimum = maximum = first_value
        total += first_value
        count += 1

        while True:
            user_input = float(input("Next positive value: "))

            if user_input < 0:
                break

            if user_input < minimum:
                minimum = user_input

            if user_input > maximum:
                maximum = user_input

            total += user_input
            count += 1

        average = total / count if count > 0 else 0.0

    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the total expenses and determines whether the user is in "Surplus", "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
    available - money currently available (float >= 0)
    Returns:
    expenses - total monthly expenses (float)
    balance - remaining balance (float)
    status - One of (str): "Surplus" if user budget is in surplus, "Deficit" if user budget is in deficit, "Balanced" if user budget is balanced.
    ------------------------------------------------------
    """

    expenses = 0.0
    while True:
        expense_input = input("Enter an expense (0 to quit): ")
        try:
            expense = float(expense_input)
            if expense == 0:
                break
            expenses += expense
        except ValueError:
            expense_input = None

    balance = available - expenses
    status = "Surplus" if balance >= 0 else "Deficit" if balance < 0 else "Balanced"

    return (expenses, balance, status)


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    finish = False
    total = 0.0
    employees = 0
    net_pay = 0

    while not finish:
        employee_id = int(input("Employee ID: "))

        if employee_id == 0:
            finish = True
        else:
            hourly_wage_rate = float(input("Hourly wage rate: "))
            hours_worked = float(input("Hours worked: "))

            if hours_worked <= OVERTIME:
                gross_pay = hours_worked * hourly_wage_rate
            else:
                gross_pay = (OVERTIME * hourly_wage_rate) + ((hours_worked - OVERTIME) * hourly_wage_rate * OVERTIME_RATE)

            net_pay = gross_pay - gross_pay * (TAX)
            total += net_pay
            employees += 1

            print(f"Net payment for employee {employee_id}: ${net_pay:.2f}")

    average = total / employees if employees > 0 else 0.0

    return total, average

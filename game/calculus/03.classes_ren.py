renpy = None
store = None


"""renpy
init python:
"""

# CLASSES



# FUNCTIONS
def calc_get_operation(calc_level):
    num1 = renpy.random.randint(1, calc_level)
    num2 = renpy.random.randint(1, calc_level)
    operator = renpy.random.choice(["+", "−", "×", "/"])
    operation = f"{num1} {operator} {num2}"
    if operator == "+":
        result = num1 + num2
    elif operator == "−":
        result = num1 - num2
    elif operator == "×":
        result = num1 * num2
    elif operator == "/":
        result = num1 // num2
    return operation, result


def calc_add_xp(amount):
    global xp, calc_level
    xp += amount
    calc_level = int((xp / 4) ** 0.5) + 1


def calc_get_streak_bonus(streak):
    """
    Get bonus if streak is a perfect square.
    Bonus will be the square root of the streak.
    """
    if (streak ** 0.5).is_integer():
        return int(streak ** 0.5)
    return 0


renpy = None
store = None


"""renpy
init python:
"""

# CLASSES



# FUNCTIONS
def get_operation(level):
    num1 = renpy.random.randint(1, level)
    num2 = renpy.random.randint(1, level)
    operator = renpy.random.choice(["+", "-", "*", "/"])
    operation = f"{num1} {operator} {num2}"
    result = int(eval(operation))
    return operation, result


def add_xp(amount):
    global xp, level
    xp += amount
    level = int((xp / 4) ** 0.5) + 1

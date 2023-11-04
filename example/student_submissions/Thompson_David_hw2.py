def findMax(numbers):
        if not numbers:
                return None
        else:
                return max(numbers)

def calculate_hypotenuse(a, b):
        c = (a**2 + b**2) ** 0.5
        return c

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


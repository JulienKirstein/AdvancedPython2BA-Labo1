# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

from math import *


def fact(n):
    """Computes the factorial of a natural number.

    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    try:
        if n > 0:
            x = 1
            for i in range(2, n + 1):
                x *= i
            return x
        else:
            raise ValueError
    except ValueError:
        print("Entier négatif")


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.

    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta = b * b - 4 * a * c

    if delta == 0:
        return (0, 0)

    if delta < 0:
        return ("None", "None")

    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return (x1, x2)


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds

    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <== 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    x = lower
    som = 0
    while x <= upper:
        som += eval(function) * 0.01
        x += 0.01

    return som


if __name__ == '__main__':
    print(fact(-1))
    print(roots(1, 6, 5))
print(integrate('x ** 2 - 1', -1, 1))
#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hp
#
# Created:     15-04-2024
# Copyright:   (c) hp 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def newtons_interpolation(x, y, xr):
    n = len(x)
    coefficients = [y[0]]

    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
        coefficients.append(y[j])

    # Evaluate the interpolation polynomial at xr
    result = coefficients[0]
    for j in range(1, n):
        term = 1
        for i in range(j):
            term *= (xr - x[i])
        result += coefficients[j] * term

    return result

# Given dataset
x = [12500, 12510, 12520, 12530]
y = [111.8034, 111.8481, 111.8928, 111.9375]
xr = 12506

# Solve using Newton's interpolation method
y_r = newtons_interpolation(x, y, xr)
print("Value of y_r:", y_r)

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:     15-04-2024
# Copyright:   (c) hp 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def custom_interpolation(x, y, xr):
    # Step 1: Find the interval where xr lies
    interval_index = 0
    for i in range(len(x) - 1):
        if x[i] <= xr <= x[i + 1]:
            interval_index = i
            break

    # Step 2: Calculate X and Y
    X = -1
    Y = 1

    # Step 3: Calculate Cr
    Cr = y[interval_index]

    # Step 4: Calculate D
    D = y[interval_index + 1] - y[interval_index]

    # Step 5: Divide D into required parts
    num_parts = interval_index + 1
    D_prime = D / num_parts

    # Step 6: Calculate Dr"
    Dr_double_prime = D_prime * ((xr - x[interval_index]) / (x[interval_index + 1] - x[interval_index]))

    # Step 7: Calculate Cr
    Cr += Dr_double_prime

    # Step 8: Calculate yr
    yr = Cr

    return yr

# Given dataset
x = [12500, 12510, 12520, 12530]
y = [111.8034, 111.8481, 111.8928, 111.9375]
xr = 12506

# Solve using custom interpolation method
y_r = custom_interpolation(x, y, xr)
print("Value of y_r:", y_r)


#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      hp
#
# Created:     15-04-2024
# Copyright:   (c) hp 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def custom_interpolation(x, y, xr_values):
    interpolated_y_values = []

    for xr in xr_values:
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

        interpolated_y_values.append(yr)

    return interpolated_y_values

# Given dataset
x = [12500, 12510, 12520, 12530]
y = [111.8034, 111.8481, 111.8928, 111.9375]

# Generate x values for plotting
x_values = np.linspace(min(x), max(x), 100)

# Use custom interpolation method to get y values
y_values = custom_interpolation(x, y, x_values)

# Plot the curve polynomial
plt.plot(x_values, y_values, label='Interpolation Polynomial', color='blue')
plt.scatter(x, y, color='red', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Custom Interpolation')
plt.legend()
plt.grid(True)
plt.show()


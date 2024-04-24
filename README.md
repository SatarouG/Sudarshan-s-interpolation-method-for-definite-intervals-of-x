# Interpolation Method for definite intervals of x

The Interpolation Method for definite intervals of x is a numerical technique used to interpolate values between data points based on a given dataset of x and y values. This method provides a straightforward approach to estimate intermediate values and is particularly useful when dealing with irregularly spaced data points.

## Usage

To use this Interpolation Method, follow these steps:

1. Define your dataset:
   - Provide a list of x-values (`x`) and corresponding y-values (`y`).

2. Choose the x-value(s) for which you want to interpolate the y-value(s).
   
3. Call the `custom_interpolation` function, passing the dataset and the x-value(s) as arguments.
   ```python
   y_r = custom_interpolation(x, y, xr)
   ```
4. The function will return the interpolated y-value(s) corresponding to the given x-value(s).

## Algorithm

The Interpolation Method for definite intervals of x follows these steps:

1. **Find the Interval**: Determine the interval in the dataset where the x-value lies.

2. **Calculate Initial Values**: Initialize variables X, Y, and Cr based on the interval.

3. **Calculate Cr**: Calculate the value of Cr, the starting y-value for the interval.

4. **Calculate Difference**: Determine the difference (D) between the y-values of the current and next data points.

5. **Divide Difference**: Divide the difference D into equal parts based on the interval.

6. **Calculate Intermediate Value**: Calculate the intermediate value (Dr_double_prime) within the interval.

7. **Adjust Cr**: Adjust the value of Cr based on the calculated intermediate value.

8. **Calculate Interpolated Value**: Calculate the interpolated y-value (yr) based on the adjusted Cr.

## Example

In the provided example, the Interpolation Method for definite intervals of x is used to interpolate the value of y for a given x-value. The method utilizes the dataset of x and y values to estimate the intermediate y-value using the defined algorithm.

## Requirements

- Python 3.x

---

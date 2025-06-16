import math

# 1. Ask user for input
num = float(input("Enter a number: "))

# 2. Perform calculations using math module
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)  # num is in radians

# 3. Display the results
print("Square Root:", sqrt_val)
print("Natural Logarithm (ln):", log_val)
print("Sine (in radians):", sine_val)

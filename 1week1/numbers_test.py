#!/usr/bin/env python3
import random  # Python has a built-in module to make random numbers

# 1. Three numeric types in Python
my_int = 1        # Integer (positive or negative, no decimals)
my_float = 2.8    # Float (contains one or more decimals)
my_complex = 3+5j # Complex (written with a 'j' as the imaginary part)

print("Int:", type(my_int))
print("Float:", type(my_float))
print("Complex:", type(my_complex))

# 2. Float can also be scientific numbers with an "e" to indicate the power of 10
sci_num = 35e3
print("Scientific number (35e3):", sci_num)

# 3. Generating a random number between 1 and 10
random_val = random.randrange(1, 11)
print("Random number between 1 and 10:", random_val)

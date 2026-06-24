from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. Use map() to transform items in a list (e.g., squaring numbers)
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# 2. Use filter() to extract items based on a condition (e.g., keeping even numbers)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# 3. Aggregate elements with reduce() to compute a single cumulative value (e.g., product of all numbers)
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

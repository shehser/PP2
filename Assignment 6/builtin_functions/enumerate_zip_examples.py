names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 1. Use enumerate() to get index and value during iteration
print("Enumerating names:")
for index, name in enumerate(names):
    print(index, name)

# 2. Use zip() to pair elements from multiple lists together
print("\nZipping names and scores:")
for name, score in zip(names, scores):
    print(name, score)

# 3. Demonstrate type checking and conversions
value_str = "150"

# Type checking using isinstance()
if isinstance(value_str, str):
    print(f"\n'{value_str}' is verified as a string.")

# Type conversion from string to integer and float
value_int = int(value_str)
value_float = float(value_str)

print("Converted to integer:", value_int, type(value_int))
print("Converted to float:", value_float, type(value_float))

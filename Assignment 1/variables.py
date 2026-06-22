#1. Creating Variables (Python has no command for declaring a variable)
x = 5
y = "John"
print("x is:", x)
print("y is:", y)

# 2. Variable Names (Case-sensitive, must start with a letter or underscore)
my_var = "Valid Name"
_my_var = "Also Valid"
myVar = "Camel Case"

# 3. Multiple Values to Multiple Variables
a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

# 4. Casting (Specifying a data type explicitly)
integer_to_str = str(3)    # will be '3'
float_to_int = int(4.8)    # will be 4 (truncates the decimal)
int_to_float = float(5)    # will be 5.0

print("Casted values:", integer_to_str, float_to_int, int_to_float)

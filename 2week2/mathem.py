#Task №1
import math
x = int(input())
a = math.radians(x)
print(f"Input degree: {x}")
print(f"Output radian: {a}")

#Task No2
height = int(input())
base1=int(int(input()))
base2 = int(input())
tra = ((base1+base2)/2)*height
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expexted Output: {tra}")

#Task No3
side = int(input())
length = int(input())
pol = pow(length, side/2)
print(f"Input number of sides: {side}")
print(f"Input the length of a side: {length}")
print(f"The area of the polygon is: {pol}")

#Task No4
blength= int(input())
pheight = int(input())
print(f"Length of base: {blength}")
print(f"Height of parallelogram: {pheight}")
print("Expected Output:", blength*pheight)

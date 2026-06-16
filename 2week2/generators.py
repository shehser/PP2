#Task no1
def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

a = int(input())

for num in square_generator(a):
    print(num)

#Task no2
def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n_input = int(input())
result = ", ".join(str(num) for num in even_generator(n_input))
print(result)

#Task no3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(int(input())):
    print(num)

#Task no4

def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a_input = int(input())
b_input = int(input())

for val in squares(a_input, b_input):
    print(val)

#Task no5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(int(input())):
    print(num)

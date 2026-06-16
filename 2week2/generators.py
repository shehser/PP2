#!/usr/bin/env python3

# generators.py

# 1. Iterator Class (Stops after 20 as shown in the text)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

print("--- Testing Iterator Class ---")
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x, end=" ")
print("\n")


# 2. Generator Function using the 'yield' keyword
def countdown(n):
    print("--- Starting yield generator ---")
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(f"Countdown: {num}")

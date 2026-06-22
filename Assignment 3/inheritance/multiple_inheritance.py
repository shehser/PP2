#!/usr/bin/env python3

# First Parent Class
class Flyer:
    def fly(self):
        print("I can fly in the air!")

# Second Parent Class
class Swimmer:
    def swim(self):
        print("I can swim in the water!")

# Child Class inheriting simultaneously from multiple parents
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack! Quack!")

# Testing multiple inheritance capabilities
donald = Duck()
donald.fly()
donald.swim()
donald.quack()

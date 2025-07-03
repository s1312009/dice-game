import random

name = input("What is your name? \n> ")
print(f"Hello, {name}!")

print("Rolling dice...")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total value: {die1 + die2}")

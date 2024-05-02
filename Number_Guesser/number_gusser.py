"""
This module generates a random number within a specified range.
"""
import random

top_of_range = input("Type Of Number:")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()

    else:
        print("Please Type a number next time.")
        quit()

random_number = random.randint(0, top_of_range)
print(random_number)

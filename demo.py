import numpy as np

try:
    limit = input("Add max: ")
    print(f"Your number is {np.random.randint(limit)}")
except:
    print("Please type a number")

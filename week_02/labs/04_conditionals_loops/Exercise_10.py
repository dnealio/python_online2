'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

#initial approach
"""
import math

a = int(input("lower bound: "))
b = int(input("upper bound: "))

for x in range(a,b+1):
    print(x**2)
"""

#consolidated approach

print("Do you want to know what the square root is for a range of numbers?")
print("enter a lower and upper bound separated by a space")

a, b = input().split()

for x in range(int(a), int(b)+1):
    print("The square of", x, "is", x**2)

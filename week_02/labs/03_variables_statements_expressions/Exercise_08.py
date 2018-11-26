'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''

def fahrenheit(c):
    f = c*1.8 + 32
    print(c, "degrees celsius =", f, "degrees fahrenheit")
fahrenheit(float(input("Input degrees celsius: ")))
"""
def fahrenheit(c):
    f = c*1.8 + 32
print("input celsius")
c = input()
fahrenheit(c)
"""

"""
print("Enter temperature in celsius:")
x = input()
c = x
f = (c*1.8 + 32)
print(f)
"""


'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
"""
print("How many miles are you driving?")
m = input()
print("what is the MPG of the car?")
mpg = input()
print("How much does fule cost?")
f = input()

cost = (m/mpg)*(f)
print(cost)

"""
def cost(a,b,c):
    result = (a/b)*c
    print("The cost of the trip in dollars is:",result)
cost(a=int(input("enter the miles to drive: ")),
    b=int(input("enter the mpg of the car: ")),
    c=int(input("enter the price per gallon of fuel: ")))

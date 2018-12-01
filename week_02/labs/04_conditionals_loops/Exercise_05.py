'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

#First we need a lower bound using the input function
#We need an upper bound using the input function
#We need to find all the numbers between bounds and loop through them
#Use a for loop to loop through the user input bounds
#set the sum of this loop to = result
#print result
#calculate amount of numbers in the range by subtracting the lower bound from upper bound
#find average using this # and the result variable


print("Let's calculate the sum and average of the numbers between two bounds")


l = int(input("Lower Bound =: "))
u = int(input("Upper Bound =: "))

result = sum(x for x in range(l, u))
print("The sum of all numbers between", l, "and", u, "=", result)

average = float(result / (u-l))
print("The average =", average)


"""
for x in range(l, u):
    result == sum(x)
    print(result)
"""


"""
    for i in range(l, x):
        if(x%l) == 1:
            break
        else:
            print(x)
"""

"""
L = int(input("Input lower bound: "))
U = int(input("Input upper bound: "))

for x in range(L, U):
    result = sum(x)
    print(result)
"""

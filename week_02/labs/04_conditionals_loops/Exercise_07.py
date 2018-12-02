'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''

"""
#basic approach -works
a = 1000
_sum = 0
while(a>=1):
    _sum = _sum+a
    print(a)
    a+=(-1)
print("The sum is", _sum)
"""
"""
#Every third number
a = 1000

while(a>=1):
    print(a)
    a+=(-3)
"""

"""
#Every third number with summing

a = 1000
_sum = 0

while(a>=1):
    print(a)
    _sum=_sum+a
    a+=(-3)
print("sum is", _sum)
"""


#every third number with user input
print("This script will count backwards every three numbers from the number you input, and sum all the numbers")
a = int(input("Enter number: "))
_sum = 0

while(a>=1):
    print(a)
    _sum=_sum+a
    a+=(-3)
print("sum is", _sum)

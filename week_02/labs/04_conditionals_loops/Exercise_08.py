'''
Demonstrate the use of the "break" statement to exit a loop.

'''


#Counts back from user input every 3 numbers until the sum of the numbers exceeds 500

print("This script will count backwards every three numbers from the number you input, and sum all the numbers until the sum is greater than 500")
a = int(input("Enter number: "))
_sum = 0

while(a>=1):
    print(a)
    _sum=_sum+a
    a+=(-3)
    if _sum >= 500:
        break
print("sum is", _sum)

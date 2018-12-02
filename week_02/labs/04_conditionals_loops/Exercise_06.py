'''
Using a "while" loop, find the sum of numbers from 1-100.
Print the sum to the console.

'''
"""
a = 1

while a <100:
    result = sum(x for x in range(a, a+1))
    print(result)

#^prints endless "1"
"""

"""
a = 1

while a < 100:
    sum(a)
    a += 1
"""

"""
for x in range(1, 100):  #returns a list (datatype: list)
    while x<100:
        result = sum(x)  #only one item is being passed to sum

#'int' object is not iterable

#do not use a while loop inside a for loop unless needed
"""

"""
a = 1

while a < 100:
    result = sum(a)
    a += 1
    print(result)
"""

"""
sum = 0
for i in range(100):
    sum = sum + i
    print(sum)
#Khan academy
"""

a = 1

_sum = 0
while(a<100):
    _sum = _sum + a
    #print("The sum is", _sum) #prints sum before each number in the sequence
    print(a)
    a = a + 1
    #a+=1
print("The sum is", _sum)


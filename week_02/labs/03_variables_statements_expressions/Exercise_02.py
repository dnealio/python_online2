'''
Write the necessary code to print out the result of the following:

	1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17

'''
a = 1
b = 18
c = sum(i for i in range(a, b) if i%2)
print(c)

'''
Print out every prime number between 1 and 100.

'''
a = 1
b = 100


for x in range(a, b+1):
    if x>1:
        for i in range(2, x):
            if(x%i) == 0:
                break
        else:
            print(x)


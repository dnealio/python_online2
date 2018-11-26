'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''
num = int(input("Enter a number between 1 and 7: "))
if num >= 1:
    if num <= 7:
        if num == 1:
            print("Monday")
        if num == 2:
            print("Tuesday")
        if num == 3:
            print("Wednesday")
        if num == 4:
            print("Thursday")
        if num == 5:
            print("Friday")
        if num == 6:
            print("Saturday")
        if num == 7:
            print("Sunday")
    else:
        print("Other")


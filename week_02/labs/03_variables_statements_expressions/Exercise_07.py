'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
def population(b, d, i, c, y):
    seconds = y*365*24*60*60
    births = seconds/b
    deaths = seconds/d
    immigrants = seconds/i
    result = (c+births+immigrants-deaths)
    print(result)
population(6,12,40,380123456,3)

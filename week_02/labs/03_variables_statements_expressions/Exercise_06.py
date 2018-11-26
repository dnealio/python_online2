'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''
def speed(k, h, m, s):
    mile = k/1.6
    time = (h + m/60 + s/3600)
    result = (mile/time)
    print(result)
speed(12, 0, 30, 30)

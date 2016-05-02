# Assignment: Coin Tosses
# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
#
# Ending the program, thank you!

# Here are some hints that might help:
#
# 1. Use the python random module to generate a random number
#
# import random
# random_num = random.random()
# # the random function will return a floating point number,
# # that is 0.0 <= random_num < 1.0
# 2. Use the python built-in round function to convert that floating point number into an integer
#
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1

def coinToss():
    count = 1
    heads = 0
    tails = 0
    for value in range(0,5000):
        import random
        random_num = random.random()
        rounded = round(random_num)
        if rounded == 1:
            heads+=1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got "+ str(heads) +" head(s) so far and "+ str(tails)+" tail(s) so far"
        else:
            tails+=1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ... Got "+ str(heads) +" head(s) so far and "+ str(tails)+" tail(s) so far"
        count+=1
    print "Ending the program, thank you!"
coinToss()

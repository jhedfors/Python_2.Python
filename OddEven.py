# Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the number and specify
 # whether it's an odd or even number.

def count():
    num = 1
    while num <101:
        if num%2 == 0:
            print "Number is %d. This is an even number." %num
        else:
            print "Number is %d. This is an odd number." %num
        num = num +1

count()

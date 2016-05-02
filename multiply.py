# Assignment: Multiply
# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:

a = [2,4,10,16]

def multiply(list,counter):
    result = []
    for value in list:
        result.append(value * counter)
    return result
print multiply(a,5)

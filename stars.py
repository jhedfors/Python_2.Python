# Assignment: Stars
# Part 1
# Create a function called  draw_stars() that takes a list of numbers and prints out  *.
#
# For example:

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def drawStars(arr):
    for value in arr:
        line = ""
        if(isinstance(value, int)):
            for i in range(0,value):
                line+="*"
            print line
        else:
            for i in range(0,len(value)):
                line+=value[0]
            print line.lower()
drawStars(y)

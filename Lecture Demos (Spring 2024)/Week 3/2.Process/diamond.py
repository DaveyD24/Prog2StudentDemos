def showLine(numStars, size):
    #set amount of spaces: size - numStars
    for i in range(size - numStars):
        print(" ", end='')
    #set number of stars: numStars paramater
    for i in range(numStars):
        print("* ", end='')
    

def showTop(size):
    for i in range(1, size):
        showLine(i, size)
        print()

def showMiddle(size):
    showLine(size, 0)
    print()

def showBottom(size):
    for i in range(size, 1, -1):
        showLine(i, size)
        print()

def showDiamond(size):
    showTop(size)
    showMiddle(size)
    showBottom(size)


size = int(input("Size of diamond: "))
showDiamond(size)


#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *


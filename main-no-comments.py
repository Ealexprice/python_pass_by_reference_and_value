"""
This code will demonstrate passing by value and by reference.
Read the code bottom up. Start in main() and trace the code
through main(). When you encounter a function call in main()
then go up and read that function to see what it does, and then
return to reading in main. This file is identical to the other
one in the repo, except it has no comments for easier reading
of the code itself. Read the comments in the other file that
explain each function and the operations being performed.
Study both of the files carefully.
"""

from operator import add

def zeroInts(aList):
    if type(aList) == type([]):
        bList = []
        for value in aList:
            if type(value) == int:
                bList.append(0)
            else:
                bList.append(value)
    else:
        raise TypeError('parameter must be a List')
    return bList


def colorMixer(colors, newcolor):
    if newcolor == 'yellow':
        colors[newcolor] = list(map(add, colors["red"], colors["green"]))
    elif newcolor == 'cyan':
        colors[newcolor] = list(map(add, colors["blue"], colors["green"]))
    elif newcolor == 'magenta':
        colors[newcolor] = list(map(add, colors["red"], colors["blue"]))
    elif newcolor == 'white':
        colors[newcolor] = list(map(add, colors["red"], colors["green"]))
        colors[newcolor] = list(map(add, colors[newcolor], colors["blue"]))


def capitalListStrings(someList):
    if type(someList) == type([]):
        for index, value in enumerate(someList):
            if type(value) == str:
                someList[index] = value.upper()
    else:
        raise TypeError('parameter must be a List')


def myPower(n, x):
    if x >= 0:
        result = pow(n, x)
    else:
        result = 0
    return result

def addOne(a):
    a = a + 1
    return a

def main():
    a = 1
    x = 2.1
    
    print("a =", a)
    print("the result of adding one to a is:", addOne(a))
    print("but a is still =", a)
    
    a = addOne(a)
    print("now a is modified and =", a)
    print()
    
    print("rasing", a, "to", x, "...")
    answer = myPower(x, a)
    print("{:.2f} raised to the power {:.2f} is {:.2f}".format(x, a, answer))
    print("x is still ", x)
    print("a is still ", a)
    print("but the answer is ", answer)
    print()

    myList = [20, "hello", 100.12, "world"]
    
    print("original list =", myList)
    capitalListStrings(myList)
    print("same list, but modified =", myList)
    print()
    
    colors = {"red": [255, 0, 0], "green": [0, 255, 0], "blue": [0, 0, 255]}
    print("original dictionary\n", colors)
    print()

    colorMixer(colors, "yellow")
    print("original dictionary modified\n", colors)
    print()

    colorMixer(colors, "magenta")
    print("original dictionary modified again\n", colors)
    print()

    colorMixer(colors, "cyan")
    print("original dictionary modified again\n", colors)
    print()

    colorMixer(colors, "white")
    print("original dictionary modified, one last time\n", colors)
    print()
    
    myNewList = zeroInts(myList)
    print("new list =", myNewList)
    print("original list =", myList)
    
    myList = zeroInts(myList)
    print("original list modified =", myList)
    
main()
print()

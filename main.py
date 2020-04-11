from operator import add # needed for colorMixer()

def colorMixer(colors, newcolor):
    # function demonstrates pass by reference and also how to element-wise
    # add lists together. it is a "toy" function for demonstration and has
    # no value beyond that
    if newcolor == 'yellow':
        colors[newcolor] = list(map(add, colors["red"], colors["green"]))
    elif newcolor == 'cyan':
        colors[newcolor] = list(map(add, colors["blue"], colors["green"]))
    elif newcolor == 'magenta':
        colors[newcolor] = list(map(add, colors["red"], colors["blue"]))
    elif newcolor == 'white':
        colors[newcolor] = list(map(add, colors["red"], colors["green"]))
        colors[newcolor] = list(map(add, colors[newcolor], colors["blue"]))

    # notice nothing is returned from this function


def capitalListStrings(someList):
    # first check to see we have a list
    if type(someList) == type([]):
        # then loop through indexes and values of the list
        for index, value in enumerate(someList):
            # look for strings
            if type(value) == str:
                # and upper case them
                # this alters the passed variable someList
                # someList is NOT local to this fucntion, it belongs to main()
                someList[index] = value.upper()
    else:
        # raise (i.e. throw) an error if someList is not a List
        raise TypeError('parameter must be a List')

    # notice nothing is returned from this function


def myPower(n, x):
    # make sure we have a positive power
    if x >= 0:
        result = pow(n, x)
    else:
        result = 0
    # this must return result because n, x, and result are local
    # to ths fucntion and pass / returns by value
    return result

def addOne(a):
    # this alters the local variable a defined here
    # it does NOT change the variable a from main
    a = a + 1
    # this must return a because the variable a here is local
    # to ths fucntion and pass / returns by value
    return a

def main():
    
    # these are scalar variables, local to main(), they pass by value.
    # pass by value means ONLY a copy of the contents of
    # the variable is passed, not the variable itself.
    a = 1
    x = 2.1
    
    print(a) # this prints 1, the value in a
    print(addOne(a)) # this prints 2, the value returned by addOne()
    print(a) # this prints 1 because the local variable a did NOT change
    
    a = addOne(a)
    print(a)
    # now the local a has changed, but NOT because of the variable a that is
    # changed in addOne(). it changes because we overwrote the local variable a
    # from main() with the return value of addOne(). the variable a in main()
    # has NOTHING to do with the variable a in addOne()

    answer = myPower(x, a) # notice this x has nothing to do with the x in myPower()
    # study this print line and make sure you understand how it works and
    print("{:.2f} raised to the power {:.2f} is {:.2f}".format(x, a, answer))
    # notice the x here has NOT changed from being passed to the function myPower()
    print()

    # the code in main() so far is demonstrating pass by value. only the values
    # are passed and returned, the variables themselves are not passed or
    # or affected by the passing, unless we purposfully overwrite them
    
    # these next example use objects, they pass by reference
    # this means if you affect them in a fucntion after passing, they WILL change!
    myList = [20, "hello", 100.12, "world"] # this is a List object
    
    print(myList) # show the original list
    capitalListStrings(myList) # pass it to a function that alters it
    # print again showing it have changed
    print(myList)
    # notice NOTHING is returned. this is pass by reference
    print()
    
    # this is a dictionary object holding lists of RGB color values
    colors = {"red": [255, 0, 0], "green": [0, 255, 0], "blue": [0, 0, 255]}
    print(colors)
    colorMixer(colors, "yellow") # notice no return value, this is by reference
    print(colors)
    colorMixer(colors, "magenta") # notice no return value, this is by reference
    print(colors)
    colorMixer(colors, "cyan") # notice no return value, this is by reference
    print(colors)
    colorMixer(colors, "white") # notice no return value, this is by reference
    print(colors)
    
main()
print()

"""
This code will demonstrate passing by value and by reference.
Read the code bottom up. Start in main() and trace the code
through main(). When you encounter a function call in main()
then go up and read that function to see what it does, and then
return to reading in main. Read the comments that explain each
function and the operations being performed. This file is also
in the repo without comments for easier reading of the code.
Study both of them.
"""

from operator import add # needed for colorMixer()

def zeroInts(aList):
    # this function will 0 all ints in a list
    # and leave everything else alone

    # first check to see we actually have a list
    if type(aList) == type([]):
        # MAKE A NEW LIST TO RETURN!
        bList = []
        # then loop through values of alist
        for value in aList:
            # look for ints and construct new list
            if type(value) == int:
                # and make them 0
                bList.append(0)
            else:
                # or else just append the old value
                bList.append(value)
    else:
        # raise (i.e. throw) an error if someList is not a List
        raise TypeError('parameter must be a List')

    # RETURN THE NEW LIST!
    return bList


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
    # first check to see we actualy have a list
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
    
    # these are scalar variables, local to main(), SCALARS PASS BY VALUE (in Python).
    # pass by value means ONLY a copy of the contents of
    # the variable is passed, not the variable itself.
    a = 1
    x = 2.1
    
    print("a =", a) # this prints 1, the value in a
    print("the result of adding one to a is:", addOne(a)) # this prints 2, i.e. the value returned by addOne()
    print("but a is still =", a) # this prints 1 because the local variable a did NOT change
    
    # what if you DO want a modified? pass it and return it to itsef
    a = addOne(a)
    print("now a is modified and =", a)
    # now the local a has changed, but NOT because of the variable a that is
    # changed in addOne(). it changes because we overwrote the local variable a
    # from main() with the return value of addOne(). the variable a in main()
    # has NOTHING to do with the variable a in addOne()
    print()
    
    # this demonstrates local variable name do NOT interact
    print("rasing", a, "to", x, "...")
    answer = myPower(x, a) # notice this x has nothing to do with the x in myPower()
    # study this print line and make sure you understand how it works
    print("{:.2f} raised to the power {:.2f} is {:.2f}".format(x, a, answer))
    # notice the x here has NOT changed from being passed to the function myPower()
    print("x is still ", x)
    print("a is still ", a)
    print("but the answer is ", answer)
    print()

    # the code in main() so far is demonstrating pass by value. only the values
    # are passed and returned, the variables themselves are NOT passed nor affected
    # by passing, unless we purposefully overwrite them.
    
    # these next example use objects, OBJECTS PASS BY REFERENCE (in Python)
    # this means if you affect them in a function after passing, they WILL change!
    myList = [20, "hello", 100.12, "world"] # this is a List object
    
    print("original list =", myList) # show the original list
    capitalListStrings(myList) # pass it to a function that alters it
    # print again showing it have changed
    print("same list, but modified =", myList)
    # notice NOTHING is returned. this is pass by reference
    print()
    
    # this is a dictionary object holding lists of RGB color values
    colors = {"red": [255, 0, 0], "green": [0, 255, 0], "blue": [0, 0, 255]}
    print("original dictionary\n", colors)
    print()

    colorMixer(colors, "yellow") # notice no return value, this is by reference
    print("original dictionary modified\n", colors)
    print()

    colorMixer(colors, "magenta") # notice no return value, this is by reference
    print("original dictionary modified again\n", colors)
    print()

    colorMixer(colors, "cyan") # notice no return value, this is by reference
    print("original dictionary modified again\n", colors)
    print()

    colorMixer(colors, "white") # notice no return value, this is by reference
    print("original dictionary modified, one last time\n", colors)
    print()
    
    # what if you DO want to change the object but ALSO keep the original object?
    # then pass the object to a function that returns a copy, while maintaining the
    # original data. it will still pass by reference, but will not be modified,
    # and a new copy is created and returned. this passes myList to zeroInts(),
    # but that function will NOT modify myList
    myNewList = zeroInts(myList)
    # we get back the altered copy in a new List
    print("new list =", myNewList)
    # and the original is maintained
    print("original list =", myList)
    
    # what if you want to pass a list to a function that does NOT modify the list,
    # but you DO want it modified? then pass it and return it back to itself.
    myList = zeroInts(myList)
    # we get back the altered copy of myList and overwrite myList with it
    print("original list modified =", myList)
    # note what actually happens is the list passed is destroyed and a new list
    # with the same name is created, giving the ILLUSION you modified the original list
    
main()
print()

Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

'''1- creat a simple function that take 2 numbers and print their values '''


def f(x,y) :
    print ('x= ' + x)
    print('y= ' +y)

'''2 - create a simple function that takes 2 numbers and return their value'''

def m(x,y):
    return (x,y)

''' 3 - in the above return function ,use keyword arguments when calling the function'''

m( x= 1,y=0)

''' give x and y default values iof 0 and call the function with no arguments'''

def m(x=0,y=0):
    return (x,y)

m()

'''5 - creat a function  that can take any number og argguments and orint the sum if them'''

def g(*args):
    sum =0
    for sum in args:
        sum +=sum
    return sum

'''6 - creat the same sum function useing the lambda'''

(lambda(*args) : sum(args))

'''7 -call the lambda function at the same definitiion line'''

(lambda(*args) : sum(args))(2,3,5,4)

''' 8- weite the difference between the local variable and global variable'''

print('the local Variable is defined locally , and it will be deleted as soon as we get out of the function or loop')
print('the global Variable is defined globally (within the class) , it can be edited from any sub class , loop or function in the class ( if it is not const)')




#1. Explain in few words what we mean by a class give an example

'''
a class is a code that we use to create Objects
the Objects have the same member variabels and methodes thats the class have
'''

class newClass:
    pass


#2. create a simple class names calculator

class calculator:
    pass

#3. Create a constructor that prints Welcome message

class calculator:
    def __init__(self ,name) :
        print(f'welcome {name} !')

c=calculator('Danny')


'''
4. Add 2 methods to the class sum & mull
5. The sum method return the sum of 2 arguments x
and y
6. The mull method return the multiplication of the
arguments x and y
'''

class calculator2:
    def __init__(self ,name) :
        print(f'welcome {name} !')

    def sum(self,number1,number2):
        return number1+number2

    def mull(self,number1,number2):
        return number1*number2

#7. Take an object from the class
#8. Call the sum method with 10 , 20
#9. Call the mull method with 10 , 20

ca = calculator2('Danny')
print(ca.sum(10,20))
print(ca.mull(10,20))


#10. Explain in few words why we call the self in methods
' to call our Object and its attributes and not an another Object'

#11. What we mean with OOP 4 Pillars
' Abstraction. Encapsulation. Inheritance. Polymorphism'

#12. Why we use OOP in our code
'to increase the readablity in the Code and to make the it easier to reused'



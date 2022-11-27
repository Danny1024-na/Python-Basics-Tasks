#1. What do we mean with the term :
#1. Base class
'''
they provide an interface,
and make sure that derived concrete classes are properly implemented.
They don't contain implementation
'''
#2. Parent class
'The class from which other classes inherit'

#3. Sub class
'The Class that from Parent Class inherit'

#4. Main class
'is the beginning of any Python program'

#5. Derived class

#6. Instance
'is an object that belongs to a class'



#2. Explain in few words what we mean with the word
#polymorphism , give an example
'''
defines methods in the child class
that have the same name as the methods in the parent class
but it can be edited 

EX:
'''
class Parent:
     def sum(self,x,y):
         return x+y

class Child(Parent):
    def sum(self,x,y):
        return x+y+1


#3. Can we inherit from more than one class in python
'yes we can'

#4. If yes how multiple inheritance works
'''
Ex :
'''

class A:
    def __init__(self,name):
        print(f'welcome {name} from class A')

class B:
     def __init__(self,name):
        print(f'welcome {name} from class B')

class C(A,B):
    pass

print('''
        it will be print welcome Danny from class A ,
        beacuase calss A is the first Parent of class C
      ''')

c=C('Danny')

Print('''
        in other Words ,it will be call the Class A first with its methods
        and if A not contains the required method ,then it we call Class B
        ''')

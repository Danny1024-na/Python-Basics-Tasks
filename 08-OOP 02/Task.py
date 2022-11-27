'''
#1. Create a new class names SciCalc with 3 methods ,
sum , mull , power all of them takes 2 argument x, y
#2. Sum return the sum of x and y
#3. Mull return the multiplication of x and y
#4. The power return x power y
#5. Take an object from the class and call the 3 methods
with any numbers
'''


class Calc:
    def __init__(self ,name) :
        print(f'welcome {name} !')

    def sum(self,number1,number2):
        return number1+number2

    def mull(self,number1,number2):
        return number1*number2


class SciCalc (Calc):

    def power(self,x,y):
        return x**y

s=SciCalc('Danny')
print(s.sum(2,4))
print(s.mull(2,4))
print(s.power(2,4))

#6. Can we inherit from the class we created in the first task Calc
' yes'

#7. Inherit from the Calc class , now remove the
#unneeded code the the SciCalc after inheriting
#8. call the 3 methods again from the SciCalc object
#9. Now you should see the same result as before

' Look up please'

#10. Explain in few words what happened after inheriting
'the methods sum and mull is called from the Father Class Calc ,because there are not sum and mull in SciCalc'

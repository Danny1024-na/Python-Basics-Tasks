# 1 what is the diiferences between '' "" ''' '''
''' (") is used when we need to write (') in the middle of a sentence '''
" (''') is used when we need to write in more than one line "
" (') used in other cases "

#2 create a String with the name 'mystro'
s='mystro'

#3 make the String letters capital
s.upper()

#4 create a list of values from 10 to 20
li=[]
for i in range(10,21):
    li.append(i)


#5 add 30 to the end of the list
li.append(30)

#6 add 40 as the second elements in the list
li.insert(1,40)

#7 print how many elements in the list
print(len(li))

#8 replace the second element in the list with 100
li[1]=100

# 9 create a tuple with values from 1 to 5
li2=[]
for i in range(1,6):
    li2.append(i)
tu=tuple(li2)

#10 can we add 10 to the end of the tuple
' NO , but we can make the tuple again a list ,then  adding the number ,then make it again a tuple'

#11 create a dic of value Mahmoud: 28  , Ahmed: 30
dic={ 'Mahmoud' : 28 , 'Ahmed' : 30}


#12 print mahmoud age frome the dict
print (dic['Mahmoud'])

#13 what is the differences between mutable and immutable data types
' (mutable): we can change the value , (immutable) : we cannot change it '

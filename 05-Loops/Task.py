#1. Print numbers from 0 to 10 using while
x=0
while(x<=10):
     print(x)
     x+=1

print('-----------------------------------')
#2. Print numbers from 0 to 1o using for

for y in range(0,11):
    print(y)

print('-----------------------------------')
#3. Stop the loop if the number = 5

for y in range(0,11):
    if(y==5):
        break
    print(y)

print('-----------------------------------')
#4. Skip the 5 iteration from print

for y in range(0,11):
    if(y==5):
        continue
    print(y)

print('-----------------------------------')


#5. Print multiplication table from 1 to 5

for y in range(1,6):
    for z in range(0,11):
        print(f' {y} X {z} = {y*z}')
    print()

print('-----------------------------------')

#6. How to get numbers from 10 to 20 using range
' by typing range(10,21)'

#7. How to get numbers from 10 to 100 with 3 at each step using range
' by typing range(10,100,3)'

#8. Get a list of even numbers from 1 to 100 using for

li=[]
for i in range(1,101):
    if(i%2==0):
        li.append(i)

print('-----------------------------------')

#9. Get a list of even numbers from 1 to 100 using while  

li.clear()
i=1
while(i<=100):
    if(i%2==0):
        li.append(i)
    i+=1

print('-----------------------------------')

#10. Get a list of even numbers from 1 to 100 using range

li=[]
for i in range(1,101):
    if(i%2==0):
        li.append(i)

print('-----------------------------------')

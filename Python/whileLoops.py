#There are 2 types of loops in python for loop and while loop
#Other programming languages also have do-while loops
#while loops there can be while else

x=0

while x < 5:
    print(f'The current value of x is {x}') #f-string is only valid in Python 3
    x += 1
else:
    print('x is not less than 5')

#loops
#pass - do nothing

#This code does nothing
for character in 'hello':
    pass

#continue goes to the top of the closest enclosing loop
for letter in 'Sammy':
    if letter == 'a':    #Don't print a this causes the program to ignore everything 
        continue         #after this line if letter is 'a' and restarts the while loop with the next letter
    
    print(letter)

#break stops a loop (while or for) if some condition is met

while x <5:
    if x==3:            #If we encounter 3 definitely end the loop
        break
    print(x)
    x+=1
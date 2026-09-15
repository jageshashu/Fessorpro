
# This is a simple while loop that prints numbers from 0 to 15. The loop continues indefinitely until the 
# condition in the if statement is met, at which point it breaks out of the loop.
number=0

while True:
    print(number)
    number=number+1
    if number>15:
        break

    for i in range(16):
        print(i)

        l1=[33,44,55,66,77]
        # max=l1[0]
        # for i in l1:
        # if i>max:
        #     max=i
        print('max', max)


# type 3
max=l1[0]
for i in range(len(l1)):
    if l1[i]>max:
        max=l1[i]        
print('max:', max)



index=0
max=l1[0]
while True:
    if l1[index]>max:
        max=l1[index]
    index=index+1
    if index>=len(l1):
        break
print('max:', max)

while True:
    number==int(input('Please enter a prime number'))
    if number==7:
        print(number)
        break

    print('------------')

    # every single problem can be solved using while loop, but not every problem can be solved using for
    # loop. For loop is used when we know the number of iterations, while loop is used when we don't know
    # the number of iterations.
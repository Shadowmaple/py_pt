n = int(input('Please enter the sum of number:'))
num = 1
check = False
while n:
    n -=1
    b = int(input('number:'))
    if b%2:
        num *=b
        check = True
if check:
    print('the result:' + str(num))
else:
    print('There are no odd number!\a')

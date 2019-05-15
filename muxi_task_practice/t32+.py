n = int(input())
a = n // 100
b = n%100 // 10
c = n % 10
if a:
    print('B'*a,end='')
if b:
    print('S'*b,end='')
if c:
    for i in range(c):
        print(i+1,end='')

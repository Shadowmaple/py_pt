n=int(input())
m =n+2
for i in range(n):
    if i <= n//2:
        m -=2
        y = i
    else:
        m +=2
        y = n-i-1
    print(' '*y, end='')
    print('*'*m)

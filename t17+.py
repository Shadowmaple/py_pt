def search(b,x):
    flag = [1]*(x+2)
    y = 2
    while y <= x:
        b.append(y)
        for i in range(y*2,x+1,y):
            flag[i] = 0
        while 1:
            y +=1
            if flag[y]==1:
                break
a, n = [], input().split()
search(a, 200000)
num = a[int(n[0])-1:int(n[1])]
for k in range(len(num)):
    if k==len(num)-1:
        print(num[k],end='')
    elif not (k+1)%10:
        print(num[k])
    else:
        print(num[k],end=' ')

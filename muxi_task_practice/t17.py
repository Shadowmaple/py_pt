import math
count, n = 0, input().split()
a, i= [], 2
while count <= int(n[1]):
    check = True
    for j in range(2,int(math.sqrt(i)+1)):
        if not i%j:
            check = False
            break
    if check:
        count +=1
        a.append(i)
    i +=1
num = a[int(n[0])-1:int(n[1])]
for k in range(len(num)):
    if k==len(num)-1:
        print(num[k],end='')
    elif not (k+1)%10:
        print(num[k])
    else:
        print(num[k],end=' ')

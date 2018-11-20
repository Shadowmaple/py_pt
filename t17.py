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
for k in range(int(n[0]),int(n[1])+1):
    if not (k-4)%10:
        print(a[k-1])
    else:
        print(a[k-1],end=' ')
if int(n[1])%10:
    print()

import math
n = []
check = True
for i in range(2,100):
    for j in range(2, int(math.sqrt(i))+1):
        if i != j:
            continue
        if not i % j:
            check = False
            break
    if check:
        n.append(i)
for i in range(1,len(n)+1):
    print('{:2d} '.format(n[i-1]),end='')
    if not i % 5:
        print()
print()

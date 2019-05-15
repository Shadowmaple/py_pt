import math
a, n = [], int(input())
for i in range(n):
    cx = input().split()
    a.append(math.sqrt(int(cx[1])**2+int(cx[0])**2))
print('{:.2f}'.format(max(a)))

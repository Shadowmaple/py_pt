import math
n = input().split()
n = [float(x) for x in n]
r,p = n[0]*n[2],n[1]+n[3]
a,b = r*math.cos(p),r*math.sin(p)
if -0.005<b<0:
    b = abs(b)
if -0.005<a<0:
    a = abs(a)
print('{:.2f}{:+.2f}i'.format(a,b))

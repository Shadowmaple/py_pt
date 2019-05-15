a, n = [0]*10, input()
n = [int(x) for x in n]
for i in n:
    a[i] +=1
for i in range(10):
    m = a.pop(0)
    if m:
         print('{}:{}'.format(i,m))

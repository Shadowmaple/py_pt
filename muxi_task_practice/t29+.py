a = [int(i) for i in input().split()]
n = a[0]
result = 0
for i in range(1,len(a)):
    result+=a[i]*10*(n-1)
    result+=a[i]*(n-1)
print(result,end="")

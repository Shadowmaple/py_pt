a = []
for i in range(3):
    a.append(int(input()))
if a[0]==a[1]==a[2]:
    print(1)
elif a[0] is a[1] or a[0] is a[2] or a[1] is a[2]:
    print(2)
elif a[0]+a[1]<=a[2] or a[0]-a[1]>=a[2]:
    print(0)
else: print(3)

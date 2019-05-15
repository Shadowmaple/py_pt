n = int(input())
date, name = [], []
check = [1 for i in range(n)]
for i in range(n):
    a = input().split()
    name.append(a[0])
    date.append(int(''.join(a[1].split('/'))))
    if date[i]<18140906 or date[i]>20140906:
        check[i] = 0
num = check.count(1)
for i in range(n):
    if check[i]:
        max_ = min_ = i
        break
for i in range(max_,n):
    if check[i]:
        if date[max_]<date[i]:
            max_ = i
        if date[min_]>date[i]:
            min_ = i
if num:
    print(num, end=' ')
    print(name[min_]+' '+name[max_])
else:
    print(num)

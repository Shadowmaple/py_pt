a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
a.sort(key=abs, reverse=True)
while a:
    print(a.pop(0), end=' ')
print()

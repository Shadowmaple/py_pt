n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.remove(max(a))
a.remove(min(a))
print("{:.2f}".format(sum(a)/(n-2)))

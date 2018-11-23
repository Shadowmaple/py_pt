n, m= int(input()), input().split()
a = []
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        a.append(int(m[i]+m[j]))
print(sum(set(a)))

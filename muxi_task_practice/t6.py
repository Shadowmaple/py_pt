a = []
n = int(input('please enter the sum of number：'))
for i in range(n):
    a.append(int(input('number:')))
a.sort(key=abs, reverse=True)
while a:
    print(a.pop(0), end=' ')
print()

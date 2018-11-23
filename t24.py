n = input()
a = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
n = [int(x) for x in n]
sum_ = str(sum(n))
for i in range(len(sum_)-1):
    print(a[int(sum_[i])],end=' ')
print(a[int(sum_[-1])])

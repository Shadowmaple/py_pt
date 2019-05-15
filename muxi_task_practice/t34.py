n = int(input())
c_a,c_b = 0,0
for i in range(n):
    m = [int(x) for x in input().split()]
    sum_ = m[0]+m[2]
    if sum_==m[1]==m[3] or (sum_!=m[1] and sum_!=m[3]):
        continue
    elif sum_==m[1]:
        c_b +=1
    else:
        c_a +=1
print(c_a,c_b)

n = int(input())
count = 1
result = []
while count <= n:
    count +=1
    num = int(input())
    while num // 10:
        num //=10
    result.append(num)
print(sum(result))
    

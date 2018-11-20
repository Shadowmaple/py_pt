n = int(input())
for i in range(n):
    num = input().split()
    if int(num[0])+int(num[1]) <= int(num[2]):
        check = 'false'
    else:
        check = 'true'
    print('Case #{}: {}'.format(i+1,check))
exit(0)

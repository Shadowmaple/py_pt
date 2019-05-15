strings =  []
n = int(input())
count = 1
while count <= n:
    strings.append(input())
    count +=1
count -=1
while count >=1:
    print(strings[count-1])
    count -=1
print(len(strings))

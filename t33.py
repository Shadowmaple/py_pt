n = input().split()
raw = int(int(n[0])/2+0.5)
print(n[1]*int(n[0]))
for i in range(raw-2):
    print(n[1]+' '*(int(n[0])-2)+n[1])
print(n[1]*int(n[0]))

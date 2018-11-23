n = input()
a = ['','S','B']
count , p= len(n), ''
for i in n:
    if count==1:
        m = [str(x) for x in range(1,int(i)+1)]
        p = p + ''.join(m)
    else:
        p = p + a[count-1]*int(i)
    count -=1
print(p)

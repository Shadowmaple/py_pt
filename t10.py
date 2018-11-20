n,m=int(input('学生数：')),int(input('课程数：'))
st = []
sum_c = []
for i in range(m):
    sum_c.append(0)
for i in range(n):
    print('学生'+str(i+1))
    grade = []
    for j in range(m):
        grade.append(int(input('课程'+str(j+1)+'：')))
        sum_c[j] += grade[j]
    a = grade[:]
    st.append(a)
    print('{:.2f}'.format(sum(grade)/m))
    grade.clear()
for i in range(m):
    print('{:.2f}'.format(sum_c[i]/n),end=' ')
num = 0
for j in range(n):
    check=True
    for i in range(m):
        if st[j][i] < sum_c[i]/n:
            check=False
    if check:
        num +=1
print('\n'+ str(num))

st = input()
result = {'A':0, 'C':0, 'T':0, 'G':0}
re = {'A':'T','T':'A','C':'G','G':'C'}
for x in st:
    result[x] += 1
    result[re[x]] +=1
print(result)

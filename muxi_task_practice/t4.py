m,n=int(input()),int(input())
a=max(m,n)
b=min(m,n)
while b:
    a, b = b, a % b
print(a)

n, m = int(input()), int(input())
if not 0<=n<=100 or not 0<=m<=100:
    print('it is error.')
elif n>=60 and m>=60:
    print('it is pass.')
elif n<60 or m<60:
    print('it is not pass.')

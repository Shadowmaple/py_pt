year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = day
if (not year%400 or not year%4) and year%100:
    days[1] = 29
for i in range(month-1):
    sum +=days[i]
print(sum)

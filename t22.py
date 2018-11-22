c = input().split()
min_ = (int(c[1])-int(c[0]))/100
h = int(min_/3600)
m = int((min_%3600)/60)
s = int(min_%3600%60+0.5)
print('{:0>2d}:{:0>2d}:{:0>2d}'.format(h,m,s))

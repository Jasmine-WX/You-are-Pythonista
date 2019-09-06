x = 0
y = 0
n = int(input('请输入斐波那契数列输出的项数:'))
for i in range(n):
    if i == 0:
        y = 1
    elif i == 1:
        x = 1
        y = 1
    else:
        t,y = y,x+y
        x = t
    print(y,end = ' ')

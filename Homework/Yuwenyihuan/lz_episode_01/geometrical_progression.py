a = int(input('请输入一个任意整数:'))
q = int(input('请输入公比:'))
n = int(input('请输入几番:'))
sum = 0
for i in range(1,n+1):
    sum += a*q**i
print(sum)

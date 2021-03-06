'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘输入。

这题倒也不难，实际上 a+aa+aaa+aa...a 可以转化为 (a * 10**0) + (a * 10**1) + (a * 10**2)……
进而转化为 a * (10**0 + 10**1 + 10**2 ……)，所以用两个 for 循环就搞定了。
注意：第1个 for 循环，range()得从1开始计数，这样子第2个 for 循环一开始才能至少循环一次（如果 i = 0，那么 range(i) 就循环不起来了。

'''

# a = int(input('请输入数字 a：'))
# count = int(input('请输入几个数相加：'))
#
# res = 0  # 初始化最终求解
# for i in range(1, count + 1):  # 循环次数与输入的值一样，但从1开始循环
#     t = 0  # 临时用的变量
#     for j in range(i):
#         t = t + 10 ** j  # 先计算 10**0 + 10**1 + ... + 10**j
#     res = res + (a * t)  # 再计算 a * t
# print(res)


'''
input() 获得的输入是字符，不是数字！而用于字符的乘法表示重复，不是数值运算！！
即是说，字符 a 乘 2 的结果是 aa，字符 '2' 乘 2 的结果是 '22'！之后运算前把 '22' 转换为数字 22 就可以了。
'''
a=input('输入数字>>>')
count=int(input('几个数字相加>>>'))
ret=[]
for i in range(1,count+1):
    ret.append(int(a*i))
    print(ret[i-1])
print(sum(ret))
'''
求1000以内所有3和5的倍数的总和。用求余数的方法简单判断一下1-999之间的所有数字，只要能被3或5整除，就把它加进 sum 里。
'''

sum = 0
for i in range(1,10):
    if i%3 == 0 or i%5 == 0:
        sum += i
print(sum)

# 如果是10的话是：6，9，5，3。所以答案是23。

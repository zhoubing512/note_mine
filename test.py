#%%
print('ddd')


# %%
import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np

X=np.linspace(-np.pi,np.pi,256,endpoint=True)#-π to+π的256个值
C,S=np.cos(X),np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
#在ipython的交互环境中需要这句话才能显示出来
plt.show()

# %%
#nums = [2,7,11,3,12,6]
nums = [3,3]
target = 6
a = {}
result = []
for i in range(0,len(nums)):
    temp = nums[i]
    a[i] = target-temp
    if temp in a.values() and len(a.keys()) > 1:
        for k,v in a.items():
            if k != i and v==temp:
                result.append([k,i])
    else:
        continue
for i in result:
    print(i)


# %%
def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i 
nums=[3,3]
target=6
twoSum(nums,target)

# %%

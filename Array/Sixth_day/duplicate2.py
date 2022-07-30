'''
找出数组中是否存在相同元素的下标之差小于整数k

思路：
使用字典存储元素及其对应的下标，从前往后依次遍历，每次遍历后遇到相同元素则替换原字典中的该元素对应的value值
直至寻找到满足条件的情况返回true或遍历结束完整个数组列表
'''

def containsNearbyDuplicate(nums, k):
    pos = {}  # 用字典保存元素和其对应下标
    for i, num in enumerate(nums):      # enumerate函数返回的是数组中的下标和对应元素
        if num in pos and i - pos[num] <= k:
            print(num, i)
            return True
        pos[num] = i
    return False

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
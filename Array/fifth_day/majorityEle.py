'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

思路：
使用字典来保存每个元素出现的次数，然后再遍历该字典，找到出现次数大于一半的
'''

def majorityElement(nums):
    ele_count = {nums[0]:1}
    for i in range(1, len(nums)):
        if(nums[i] in ele_count.keys()):
            ele_count[nums[i]] += 1
        else:
            ele_count[nums[i]] = 1
    mid = len(nums) // 2

    ele = [i for i in ele_count.keys() if ele_count[i] > mid]
    return ele[0]

nums = [2,2,1,1,1,2,2]
ele = majorityElement(nums)
print(ele)

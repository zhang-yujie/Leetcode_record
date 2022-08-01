'''
汇总区间，给定一个无重复元素的有序整数数组，给出一些个区间刚好覆盖连续的元素

思路：
依次遍历即可
输入:nums = [0,1,2,4,5,7]
输出:["0->2","4->5","7"]
'''

def summaryRanges(nums):
    # 看清题目中是否说的是非空数组，否则要先进行判断，防止超出下标
    l = len(nums)
    if l == 0:
        return []

    first_ele = nums[0]
    ss = []
    for i in range(1, l):
        if nums[i] - nums[i-1] > 1:
            if first_ele == nums[i-1]  or first_ele == nums[i]:   # 第一个元素是单个区间或者最后一个元素是单个区间的情况
                s = str(nums[i-1])
            else:
                s = str(first_ele) + '->' + str(nums[i-1])
            ss.append(s)
            first_ele = nums[i]
    # 处理最后几个元素
    if nums[l-1] != first_ele:
        s = str(first_ele) + '->' + str(nums[l-1])
    else:
        s = str(nums[l-1])
    ss.append(s)
    return ss

nums = []
print(summaryRanges(nums))
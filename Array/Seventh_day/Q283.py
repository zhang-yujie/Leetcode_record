'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

思路：
遍历数组，使得每次将不为0的元素放到原有的数组中，最后再补全0
'''

def moveZeroes(nums):
    l = len(nums)
    k = 0   # 重新排序的数组下标
    for i in range(l):
        if nums[i] != 0 :
            nums[k] = nums[i]
            k += 1
    while k < l:
        nums[k] = 0
        k += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
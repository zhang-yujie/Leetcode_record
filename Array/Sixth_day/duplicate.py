'''
如果数组中有元素出现两次以上则返回true，否则返回false

思路：用集合过滤一下就行了，但空间复杂度会达到O（n）
'''

def containsDuplicate(nums):
    nums_set = set(nums)
    return len(nums_set) < len(nums)

nums = [1,2,3,4]
print(containsDuplicate(nums))
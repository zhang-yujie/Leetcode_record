'''
删除有序列表中重复元素且保持有序不变
'''

def removeDuplicates(nums):
    # nums = list(set(nums))
    # print(nums)
    # return len(nums), nums
    j = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        else:
            nums[j] = nums[i]
            j += 1
    return j

nums = [1, 1, 2]

print(removeDuplicates(nums))
print(nums)
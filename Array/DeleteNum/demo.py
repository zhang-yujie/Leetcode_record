'''
删除列表中指定的元素并返回删除元素之后的列表长度
'''

def removeElement(nums, val):
    for i in range(len(nums)-1, -1, -1):
        print(i, nums[i])
        if nums[i] == val:
            nums.pop(i)
    return len(nums)

nums = [3,2,2,3]
val = 3
now_len = removeElement(nums, val)
print(now_len)
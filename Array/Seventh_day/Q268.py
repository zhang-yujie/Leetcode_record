'''
找到丢失的数字
思路：直接进行遍历就行了

这道题5遍才通过，好多细节的地方没有想清楚，一直有用例不能通过
'''

def missingNumber(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    if nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            return nums[i-1]+1
    return nums[-1] + 1

nums = [0]
print(missingNumber(nums))



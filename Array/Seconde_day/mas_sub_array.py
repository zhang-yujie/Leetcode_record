'''找到数组中和最大的连续数组'''

def maxSubArray(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]  # dp序列的第一个值就应该是数组本身
    for i in range(1, len(nums)):
        dp[i] = max((dp[i-1] + nums[i]), nums[i])
    return max(dp)


def maxSubArray_improve(nums):
    max_sum = nums[0]  # 保存当前遍历到的所有数组中dp最大的
    cur_dp = nums[0]
    for i in range(1, len(nums)):
        cur_dp = max((cur_dp + nums[i]), nums[i])
        max_sum = max(cur_dp, max_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = maxSubArray_improve(nums)
print(max_sum)

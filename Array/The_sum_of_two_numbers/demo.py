'''
 给出一个列表，求两数之和
 输入：[3, 2, 4]   target：6
 输出：[1, 2]

 这道题是经典的leetcode数组简单类，关键点在，每次用tartget减掉一个数后，剩余的数字和数组中其余的数字进行比较
'''


def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        last = target - nums[i]
        temp = nums[:i]   # 不能截取num之后i之后的数组，因为放到temp之后，index会变
        if last in temp:
            result.append(temp.index(last))
            result.append(i)
            return result

# 示例
nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))
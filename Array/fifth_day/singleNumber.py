'''
求给出数组中只出现一次的数，要求线性时间内完成，不使用额外的空间

思路：先对数组进行排序，然后进行一个线性的遍历
'''
from functools import reduce

# 时间复杂度再排序上可能会花的多一点，不满足线性，空间复杂度由于只用了常数个变量，因此空间复杂度满足要求
def singleNumber(nums):
    nums.sort()
    print(nums)
    l = len(nums)
    if l == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[l-1] != nums[l-2]:
        return nums[l-1]
    for i in range(1, l-1):
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            return nums[i]
    return -1

# 方法二：不需要对其进行排序，时间上线性，空间上使用一个集合对其进行保存
# 由于集合中的元素不重复，所以集合中所有元素的两倍和原数组所有元素和的差即为single number
def singleNumber1(nums):
    s = sum(nums)
    nums_set = set(nums)
    s_set = sum(nums_set)
    return s_set*2-s

# 方法三：时间上线性，空间上O（1）。用异或去实现
# 任何数和0进行异或等于该数，任何数和其本身进行异或为0
# 并且异或运算满足结合律和交换律，所以对nums中的每一个数依次进行异或就可以得到最终落单的哪一个
def singleNumber2(nums):
    return reduce(lambda x, y: x ^ y, nums)


nums = [4,1,2,1,2]
single = singleNumber2(nums)
print(single)
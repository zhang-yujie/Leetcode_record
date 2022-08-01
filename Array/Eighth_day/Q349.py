'''
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

思路：
两种，第一种先进行排序，然后同时遍历两个数组
第二种直接遍历一个数组的每个元素，每次在两外一个数组中进行寻找，类似暴力算法
'''

def intersection(nums1, nums2):
    result = []
    for x in nums1:
        if x in nums2:
            result.append(x)
    return list(set(result))    # 用集合过滤掉重复元素



# 排序＋双指针    更优
def intersection1(nums1, nums2):
    result = []
    # nums1 = list(set(nums1))
    # nums2 = list(set(nums2))
    # 先对两组进行排序
    nums1.sort()
    nums2.sort()
    l1 = len(nums1)
    l2 = len(nums2)
    i = j = 0
    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return list(set(result))


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection1(nums1, nums2))
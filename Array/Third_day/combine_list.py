'''
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

思路:
    逐次遍历数组，如果某一个数组长度是0，则直接将另外一个数组赋值到数组nums1中
    若两个数组均有元素，则依次遍历数组，这里利用空间换时间的方法，重新创建一个新的数组nums3来保存合并后的有序数组，然后再赋值给nums1
'''

def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    nums3 = [0 for i in range(m+n)]
    k = 0
    while(i < m and j < n):
        while(i < m  and nums1[i] <= nums2[j]):
            nums3[k] = nums1[i]
            k += 1
            i += 1

        while(j < n and nums2[j] <= nums1[i]):
            nums3[k] = nums2[j]
            k += 1
            j += 1
    while(i < m):
        nums3[k] = nums1[i]
        k += 1
        i += 1
    while(j < n):
        nums3[k] = nums2[j]
        k += 1
        j += 1
    nums1 = nums3
    return nums1


def merge_hh(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge_hh(nums1, m, nums2, n)
print(nums1)
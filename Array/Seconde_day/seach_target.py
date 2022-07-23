'''
在排序数组中找到目标值并返回下标，如果没有找到则返回插入后的下标
'''

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] < target:
            continue
        else:
            nums.append(nums[len(nums)-1])   # 从最后一个元素开始往后移
            for j in range(len(nums)-1, i, -1):
                nums[j] = nums[j-1]
            nums[i] = target
            return i

    # 在数组的最后一个位置插入target
    if i == len(nums) - 1:
        nums.append(target)
        return i + 1


# 使用二分查找进行改进
def searchInsert_improve(nums, target):
    low = 0
    high = len(nums) - 1
    # print(high)
    # mid = (high - low) // 2
    # print(mid)
    while(low <= high):
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid-1

    # print(low, high)
    return low



nums = [1,3,5,6]
target = 7
index = searchInsert_improve(nums, target)
print(index)
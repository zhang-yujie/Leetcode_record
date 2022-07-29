'''
将有序数组转换为高度平衡二叉树

思路：
通过递归的方法去构建树
数组的遍历使用二分查找的遍历方法
依次返回该根节点的左右子树
'''

# 创建树，构造函数中的暂时没有值的属性先用None进行赋值
class TreeNode:
    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode



def sortedArrayToBST(nums):
    return helper(0, len(nums)-1)


def helper(left, right):
    if (left > right):
        return None

    mid = (left + right) // 2  # 找到中间的元素并将其作为根节点
    root = TreeNode(nums[mid])
    root.leftNode = helper(left, mid - 1)
    root.rightNode = helper(mid + 1, right)
    return root

# 层序遍历打印树
def printTree(root):
    s = []
    answer = []
    s.append(root)
    while (len(s)):
        temp = s.pop(0)  #每次取出第一个
        answer.append(temp.value)
        print(temp.value, end=',')
        if temp.leftNode != None:
            s.append(temp.leftNode)
        if temp.rightNode != None:
            s.append(temp.rightNode)


nums = [-10,-3,0,5,9]
test = sortedArrayToBST(nums)
printTree(test)
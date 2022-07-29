'''
返回杨辉三角形的数列组合
'''

def generate(numRows):
    a = []
    for i in range(numRows):       # 创建一个二维数组
        a.append([])
        for j in range(i+1):
            a[i].append(0)

    for i in range(numRows):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2, numRows):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a

# 根据给出的行下标，返回杨辉三角形中该行的结果
def getRow(rowIndex):
    rowIndex += 1
    a = []
    for i in range(rowIndex):  # 创建一个二维数组
        a.append([])
        for j in range(i + 1):
            a[i].append(0)

    for i in range(rowIndex):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2, rowIndex):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    return a[rowIndex-1]


print(getRow(3))
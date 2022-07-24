'''
给出一个由整数组成的列表，整个列表表示的数字表示一个整数，目的是要为该整数上整体加1后发返回一个新的数组

思路：倒序遍历数组，如果当前位为9，则加1后变成0，前一位加1
    若第一位是9，且加1了，则数组长度要加1，第一位新增一位
'''

def plusOne(digits):
    l = len(digits)
    i = l-1
    for i in range(l-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    # if i == 0:        # 遍历到第一个元素，要整体加一位
    #     digits.append(digits[l-1])
    #     for j in range(l-1, 0, -1):
    #         digits[j] = digits[j-1]
    #     digits[0] = 1

    # 以上一段的改进  如果遍历到最后，说明每一位数字都是9, 但是内存会增加
    digits = [0 for i in range(l + 1)]
    digits[0] = 1

    return digits

digits = [1, 9]
new_digits = plusOne(digits)
print(new_digits)
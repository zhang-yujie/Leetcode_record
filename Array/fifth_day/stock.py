'''
题目：只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。若不能有利润则返回0。

思路：
从第二天开始遍历，找到当前第i天前的（i-1）天的最小利益，然后用当前天数减去该最小利益则是当前天数的最大盈利值，该盈利值只有大于等于0的时候才作数
'''

def maxProfit(prices):
    profits = []
    profits.append(0)
    l = len(prices)
    min = prices[0]
    for i in range(1, l):
        min = min if prices[i] > min else prices[i]     # 用一个常量来保存历史最小价格
        curPro = prices[i] - min
        profits.append(curPro)
    mp = max(profits)
    return mp if mp > 0 else 0


prices = [7,6,4,3,1]

print(maxProfit(prices))
# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/3
@function:
121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
题目描述
    给定一段时间内每天的股票价格，已知你只可以买卖各一次，求最大的收益。
输入输出样例
    输入一个一维整数数组，表示每天的股票价格；输出一个整数，表示最大的收益。
    Input: [7,1,5,3,6,4]
    Output: 5
    在这个样例中，最大的利润为在第二天价格为 1 时买入，在第五天价格为 6 时卖出。

题解
    最大收益为：最大售出价格-最低买入价格
    需要记录之前所有价格的最低价格，然后将当前价格作为出售，查看当前收益是否最大
"""
def maxProfit(prices):
    sell=0
    buy=-1e10 # 计算收益的时候，需要做减法，这里直接取负号
    for i in range(len(prices)):
        buy=max(buy, -prices[i])
        sell=max(sell, buy+prices[i])
    return sell

prices=[7,1,5,3,6,4]
sell=maxProfit(prices)
print(sell)
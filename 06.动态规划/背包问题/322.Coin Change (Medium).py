# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
322. Coin Change (Medium)
https://leetcode.com/problems/coin-change/
题目描述
    给定一些硬币的面额，求最少可以用多少颗硬币组成给定的金额。
输入输出样例
    输入一个一维整数数组，表示硬币的面额；以及一个整数，表示给定的金额。输出一个整数，
    表示满足条件的最少的硬币数量。若不存在解，则返回-1。
    Input: coins = [1, 2, 5], amount = 11
    Output: 3
    在这个样例中，最少的组合方法是 11 = 5 + 5 + 1。
题解
    这里求最小化， 所以dp初始化一个极大值， 不能初始化为-1，否则始终为-1，dp里最大的值可以为
    amount+1，所以最大值为amount+2。最多的组成方式是一元硬币，因此amount+2一定大于所有可能的
    组成方式，最小值也不可能是他。动态规划完成后，如果结果还是这个值，说明不存在满足条件的组合。
"""

def coinChange(coins, amount):
    if len(coins)==0:
        return -1
    dp=[amount+2]*(amount+1)
    dp[0]=0
    for i in range(1, amount+1):
        for coin in coins:
            if i>=coin:
                dp[i]=min(dp[i],dp[i-coin]+1) # 加1表示用该面额的硬币表示
    if dp[amount]==amount+2:
        return -1
    return dp[amount]


coins=[1, 2, 5]
amount=11
res=coinChange(coins,amount)
print(res)
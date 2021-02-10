# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/1
@function:
70. Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/
题目描述
    给定 n 节台阶，每次可以走一步或走两步，求一共有多少种方式可以走完这些台阶。
输入输出样例
    输入是一个数字，表示台阶数量；输出是爬台阶的总方式。7.2 基本动态规划：一维 – 41/143 –
    Input: 3
    Output: 3
    在这个样例中，一共有三种方法走完这三节台阶：每次走一步；先走一步，再走两步；先走两步，再走一步
题解
    Fibonacci数列
"""


def climbStairsRecursive(n):
    # 时间复杂度较高
    if n<=2:
        return n
    return climbStairs(n-1)+climbStairs(n-2)


def climbStairsIteration(n):
    # 时间复杂度为O(n), 空间复杂度为O(n)
    if n<=2:
        return n
    dp=[0,1,2]
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]


def climbStairsCompression(n):
    # 时间复杂度为O(n)，空间复杂度为O(1)
    a,b=1,2
    for i in range(2,n+1):
        a,b=b,a+b
    return a


res=climbStairsCompression(3)
print(res)
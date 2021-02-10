# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/2
@function:
279. Perfect Squares (Medium)
https://leetcode.com/problems/perfect-squares/
题目描述
    给定一个正整数，求其  最少  可以由几个   完全平方数   相加构成。
输入输出样例
    输入是给定的正整数，输出也是一个正整数，表示输入的数字最少可以由几个完全平方数相
    加构成。
    Input: n = 13
    Output: 2
    在这个样例中， 13 的最少构成方法为 4+9。
题解
    对于分割类型题， 动态规划的状态转移方程并不依赖相邻的位置，而是依赖于满足分割条件的位置。
    定义一个一维矩阵dp，dp[i]表示数字i最好可以由几个完全平方数相加构成。

"""
# TODO

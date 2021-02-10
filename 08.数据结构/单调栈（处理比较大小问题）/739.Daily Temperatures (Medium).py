# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
739. Daily Temperatures (Medium)
https://leetcode.com/problems/daily-temperatures/
题目描述
    给定每天的温度，求对于每一天需要等几天才可以等到更暖和的一天。如果该天之后不存在更暖和的天气，则记为 0。
输入输出样例
    输入是一个一维整数数组，输出是同样长度的整数数组，表示对于每天需要等待多少天
    Input: [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]
题解
    维持一个单调递增的栈，表示每天的温度。栈内保存的值为位置而非温度本身
"""


def dailyTemperatures(temperatures):
    stack = []
    ans = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while len(stack) > 0:
            pre_index = stack[-1]
            if temperatures[i] <= temperatures[pre_index]:
                break
            stack.pop()
            ans[pre_index] = i - pre_index
        stack.append(i)
    return ans


t = [73, 74, 75, 77, 69, 72, 76, 77]
ans = dailyTemperatures(t)
print(ans)

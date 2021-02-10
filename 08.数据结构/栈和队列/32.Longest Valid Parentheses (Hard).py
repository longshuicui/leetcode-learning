# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/4
@function:
32. Longest Valid Parentheses (Hard)
https://leetcode.com/problems/longest-valid-parentheses/
题目描述
    在给的字符串里面找到 最大长度的 有效 括号字符串
输入输出示例
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
题解
    使用栈
"""


def longestValidParentheses(s):
    stack = []
    maxLength = 0
    stack.append(-1)
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()  # 这里只有小括号， 所以不需要判断，左括号位置出栈即可
            if len(stack) == 0:
                stack.append(i)
            else:
                maxLength = max(maxLength, i - stack[-1])
    return maxLength


s = ")()"
l = longestValidParentheses(s)
print(l)

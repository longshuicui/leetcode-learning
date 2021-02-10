# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/7
@function:
227. Basic Calculator II (Medium)
https://leetcode.com/problems/basic-calculator-ii/
题目描述
    给定一个包含加减乘除整数运算的字符串，求其运算结果，只保留整数。
输入输出样例
    输入是一个合法的运算字符串，输出是一个整数，表示其运算结果。
    Input: " 3+5 / 2 "
    Output: 5
    在这个样例中，因为除法的优先度高于加法，所以结果是 5 而非 4。
"""

def calculate(s):
    s=s.replace("/","//")
    a=eval(s)
    return a


s="3+2*2"
a=calculate(s)
print(a)
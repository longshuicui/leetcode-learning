# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/25
@function:
455. Assign Cookies (Easy)
https://leetcode.com/problems/assign-cookies/
题目描述
    有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃
    一个饼干，且只有饼干的大小不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子
    可以吃饱。
输入输出样例
    输入两个数组，分别代表孩子的饥饿度和饼干的大小。输出最多有多少孩子可以吃饱的数
    量。
    Input: [1,2], [1,2,3]
    Output: 2
策略
    首先考虑最小的孩子，使这个孩子吃饱。
    贪心策略，给剩余孩子里最小饥饿度的孩子分配最小的能吃饱的饼干
"""


def findContentChildren(children, cookies):
    # 首先进行排序，
    children.sort()
    cookies.sort()
    child, cookie = 0, 0
    while child < len(children) and cookie < len(cookies):
        if children[child] <= cookies[cookie]:
            child += 1
        cookie += 1
    return child


children = [1, 2]
cookies = [1, 2, 3]

child = findContentChildren(children, cookies)
print(child)

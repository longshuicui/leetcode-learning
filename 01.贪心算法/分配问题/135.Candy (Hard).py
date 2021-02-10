# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
135.Candy (Hard)
https://leetcode.com/problems/candy/
题目描述
    一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一
    个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；所
    有孩子至少要有一个糖果。求解最少需要多少个糖果。
输入输出样例
    输入是一个数组，表示孩子的评分。输出是最少糖果的数量。
    Input: [1,0,2]
    Output: 5
    [2, 1, 2]
策略
    贪心策略，从左到右，从右到左遍历，每次更新只考虑相邻一侧的大小关系

"""


def candy(ratings):
    # 如果只有一个小孩，给一个就好了
    size = len(ratings)
    if size < 2:
        return size
    outputs = [1] * size
    # 从左到右遍历
    for i in range(1, size):
        if ratings[i] > ratings[i - 1]:
            outputs[i] = outputs[i - 1] + 1
    for i in range(size - 1, 0, -1):
        if ratings[i] < ratings[i - 1]:
            outputs[i - 1] = max(outputs[i - 1], outputs[i] + 1)
    return sum(outputs)


ratings = [1, 0, 2]
nums = candy(ratings)
print(nums)

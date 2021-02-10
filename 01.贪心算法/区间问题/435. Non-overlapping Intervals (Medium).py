# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:
435. Non-overlapping Intervals (Medium)
https://leetcode.com/problems/non-overlapping-intervals/
题目描述
    给定多个区间，计算让这些区间  互不重叠  所需要移除区间的  最少  个数。起止相连不算重叠。

输入输出样例
    输入是一个数组，数组由多个长度固定为 2 的数组组成，表示区间的开始和结尾。输出一个
    整数，表示需要移除的区间数量。
    Input: [[1,2], [2,4], [1,3]]
    Output: 1
    在这个样例中，我们可以移除区间 [1,3]，使得剩余的区间 [[1,2], [2,4]] 互不重叠。

策略
     选择区间的结尾越小，留给其他区间的空间就越大，越能保证互不重叠
     优先保留    结尾小   且   不重叠   的区间
     需要根据实际情况判断区间开头排序还是结尾排序
"""


def nonOverlappingIntervals(intervals):
    # 如果传入的数组为空， 直接返回0就好了
    if len(intervals) == 0:
        return 0
    size = len(intervals)
    # 按照结尾从小到大排序
    intervals = sorted(intervals, key=lambda x: x[1], reverse=False)

    total = 0
    prev = intervals[0][1]  # 第一个区间结尾大小
    for i in range(1, size):
        if intervals[i][0] < prev:
            total += 1
        else:
            prev = intervals[i][1]
    return total


intervals = [[1, 2], [2, 4], [1, 3]]
total = nonOverlappingIntervals(intervals)
print(total)

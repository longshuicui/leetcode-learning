# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/12
@function:
1310. 子数组异或查询 (Medium)
https://leetcode-cn.com/problems/xor-queries-of-a-subarray/
有一个正整数数组arr，现给你一个对应的查询数组queries，其中queries[i] = [Li,Ri]。
对于每个查询i，请你计算从Li到Ri的XOR值（即arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。
并返回一个包含给定查询queries所有结果的数组。
示例 1：
    输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    输出：[2,7,14,8]
    解释：
    数组中元素的二进制表示形式是：
    1 = 0001
    3 = 0011
    4 = 0100
    8 = 1000
    查询的 XOR 值为：
    [0,1] = 1 xor 3 = 2
    [1,2] = 3 xor 4 = 7
    [0,3] = 1 xor 3 xor 4 xor 8 = 14
    [3,3] = 8

示例 2：
    输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
    输出：[8,0,4,4]

"""


def xorQueriesBrute(arr, queries):
    """暴力求解法超时，
    时间复杂度O(nk),n为queries的长度，k为区间最大长度
    额外空间复杂度O(1),常数空间"""
    res = []
    for l, r in queries:
        a = 0
        for i in range(l, r + 1):
            a ^= arr[i]
        res.append(a)
    return res


def xorQueriesPre(arr, queries):
    """前缀异或，这里求出每个位置的前面的异或结果，存储下来，这样就不会重复计算了
    时间复杂度O(n+m),n为arr的长度和queries长度的最大值
    空间复杂度O(n),存储前面的异或结果"""
    pre = []
    a = 0
    for i in range(len(arr)):
        a ^= arr[i]
        pre.append(a)
    res = []
    for l, r in queries:
        if l - 1 < 0:
            res.append(pre[r])
        else:
            res.append(pre[l - 1] ^ pre[r])
    return res


arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
res = xorQueriesPre(arr, queries)
print(res)

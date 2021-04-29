# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/29
@function:
403. 青蛙过河 (Hard)
https://leetcode-cn.com/problems/frog-jump/
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示），请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时，青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了k个单位，那么它接下来的跳跃距离只能选择为k - 1、k或k + 1 个单位。另请注意，青蛙只能向前方（终点的方向）跳跃

示例 1：
    输入：stones = [0,1,3,5,6,8,12,17]
    输出：true
    解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。

示例 2：
    输入：stones = [0,1,2,3,4,8,9,11]
    输出：false
    解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

题解：
    1. DFS 深度优先搜索，暴力搜索， 时间复杂度为O(3^n) 空间复杂度O(3^n) 超时
    2. 记忆化搜索 时间复杂度O(n^2),空间复杂度O(n^2)
    青蛙能否到达中点与当前所在石子的编号以及上次跳跃距离有关
    3. 动态规划

"""

def canCrossBrute(stones):
    hashMap={} # 将石子放入哈希表，为了快速判断是否存在某块石子，以及快速拿到下标
    for i in range(len(stones)):
        hashMap[stones[i]]=i
    if 1 not in hashMap: # 题意中第二个石子必然是1
        return False
    return dfs_brute(stones, 1, 1, hashMap)


def dfs_brute(stones, curr_i, k, hashMap):
    if curr_i == len(stones)-1:
        return True
    # 当前位置为curr_i，上一步跳跃的距离为k，现在跳跃的距离为[k-1, k, k+1]
    for i in range(-1, 2):
        if k+i==0: # 原地跳，不考虑
            continue
        next_v=stones[curr_i]+k+i
        if next_v in hashMap:
            if dfs_brute(stones, hashMap[next_v], k+i, hashMap):
                return True
    return False


def canCrossCache(stones):
    hashMap = {}  # 将石子放入哈希表，为了快速判断是否存在某块石子，以及快速拿到下标
    cache = {}
    for i in range(len(stones)):
        hashMap[stones[i]] = i
    if 1 not in hashMap:  # 题意中第二个石子必然是1
        return False
    return dfs_cache(stones, 1, 1, hashMap, cache)


def dfs_cache(stones, curr_i, k, hashMap, cache):
    key=str(curr_i)+"_"+str(k)
    if key in cache:
        return cache[key]
    if curr_i==len(stones)-1:
        return True
    for i in range(-1,2):
        if k+i==0:
            continue
        next_v=stones[curr_i]+k+i
        if next_v in hashMap:
            curr=dfs_cache(stones, hashMap[next_v], k+i, hashMap, cache)
            cache[key]=curr
            if curr:
                return True
    cache[key]=False
    return False


def canCrossDP(stones):
    pass


stones=[0,1,2,3,4,8,9,11]
res=canCrossCache(stones)
print(res)



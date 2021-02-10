# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/28
@function:
347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/
题目描述
    给定一个数组，求前 k 个最频繁的数字。
输入输出样例
    输入是一个数组和一个目标值 k。输出是一个长度为 k 的数组。
    Input: nums = [1,1,1,1,2,2,3,4], k = 2
    Output: [1,2]
    在这个样例中，最频繁的两个数是 1 和 2。

题解
    桶排序。将相同的值放到同一个桶中，记录这个值出现的次数；然后对桶进行排序，
"""
def topKFrequent(nums, k):
    counts={}
    max_count=0
    for num in nums:
        counts[num]=counts.get(num,0)+1
        max_count=max(max_count, counts[num])
    buckets=[[] for _ in range(max_count+1)] # 按照数量从小到大进行排序
    for num in counts:
        buckets[counts[num]].append(num)

    ans=[]
    for i in range(max_count,-1,-1):
        if i>=0 and len(ans)<k:
            for num in buckets[i]:
                ans.append(num)
                if len(ans)==k:
                    break
    return ans



nums = [1,1,1,1,2,2,3,4]
k = 3
ans=topKFrequent(nums,k)
print(ans)
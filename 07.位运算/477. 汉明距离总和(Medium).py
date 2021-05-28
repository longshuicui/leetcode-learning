# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/28
@function:
477. 汉明距离总和 (Medium)
https://leetcode-cn.com/problems/total-hamming-distance/
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
计算一个数组中，任意两个数之间汉明距离的总和。
示例:
    输入: 4, 14, 2
    输出: 6
    解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
    所以答案为：
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

"""


def totalHammingDistanceBrute(nums):
    """暴力求解 时间复杂度为O(n^2logC)"""

    def hammingDistance(x, y):
        diff = x ^ y
        ans = 0
        while diff:
            ans += diff & 1
            diff >>= 1
        return ans
    ans=0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            ans+=hammingDistance(nums[i],nums[j])
    return ans


def totalHammingDistance(nums):
    """第i位的汉明距离c*(n-c)，c为第i位为1的个数"""
    ans=0
    for i in range(30):
        c=0
        for val in nums:
            c+=(val>>i)&1 # 统计第i位为1的个数
        ans+=c*(len(nums)-c)
    return ans



nums=[4,14,2]
res=totalHammingDistanceBrute(nums)
print(res)
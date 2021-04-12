# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/12
@function:
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。
示例：
    输入：n = 10
    输出：12
    解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。



"""
import heapq
def nthUglyNumberHeap(n):
    """最小堆时间复杂度：O(nlogn) 存储丑数和丑数去重需要的空间不超过O(3n)
    """
    factors=[2,3,5]
    heap=[]
    ugly_nums= {}
    heapq.heappush(heap, 1)
    for i in range(n):
        curr=heapq.heappop(heap)
        for factor in factors:
            num=curr*factor
            if num not in ugly_nums:
                heapq.heappush(heap, num)
                ugly_nums[num]=0
            else:
                ugly_nums[num]+=1
    return curr


def nthUglyNumberDynamicP(n):
    """动态规划， 时间复杂度O(n), 空间复杂度O(n)
    """
    dp=[0]*(n+1)
    dp[1]=1
    p2=p3=p5=1
    for i in range(2, n+1):
        num2, num3, num5=dp[p2]*2, dp[p3]*3, dp[p5]*5
        dp[i]=min(num2, num3, num5)
        if dp[i]==num2:
            p2+=1
        if dp[i]==num3:
            p3+=1
        if dp[i]==num5:
            p5+=1
    return dp[n]


n=10
res=nthUglyNumberDynamicP(n)
print(res)
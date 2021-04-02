# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/5
@function:
239. Sliding Window Maximum (Hard)
题目描述
    给定一个整数数组和一个滑动窗口大小，求在这个窗口的滑动过程中，每个时刻其包含的最大值。
输入输出样例
    输入是一个一维整数数组，和一个表示滑动窗口大小的整数；输出是一个一维整数数组，表
    示每个时刻时的窗口内最大值。
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    在这个样例中，滑动窗口在每个位置的最大包含值取法如下：
题解
    可以利用双端队列进行操作：每当向右移动时，把窗口左端的值从队列左端删除，把队列右边小于
    窗口右端的值全部剔除。这样双端队列的最左端永远是当前窗口内的最大值。
    双端队列从左到右递减维持大小关系
"""
from collections import deque

def maxSlidingWindowBrute(nums, k):
    """暴力搜索O(n*k)，超时"""
    ans = []
    for i in range(len(nums) - k + 1):
        windows = nums[i:i + k]
        maxVal = windows[0]
        for val in windows:
            if val > maxVal:
                maxVal = val
        ans.append(maxVal)
    return ans


def maxSlidingWindow(nums, k):
    """双端队列"""
    que=deque()
    res=[]
    for i in range(len(nums)):
        if que and que[0]==i-k:
            que.popleft() # 将队列头部的值删除，也就是窗口左边的值
        while que and nums[que[-1]]<nums[i]: # 队列右端小于窗口右端的值全部删除
            que.pop()
        que.append(i)
        if i+1>=k:
            res.append(nums[que[0]])
    return res


def sumSlidingWindow(nums, k):
    que=deque()
    res=[]
    temp=0
    for i in range(len(nums)):
        if que and que[0]==i-k:
            temp-=nums[que[0]]
            que.popleft()
        que.append(i)
        temp+=nums[i]
        if i+1>=k:
            res.append(temp)
    return max(res)



nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = sumSlidingWindow(nums, k)
print(res)

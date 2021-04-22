# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/19
@function:.
220. 存在重复元素 III(Medium)
给你一个整数数组 nums 和两个整数k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。
示例:
    输入：nums = [1,2,3,1], k = 3, t = 0
    输出：true
    输入：nums = [1,0,1,1], k = 1, t = 2
    输出：true
    输入：nums = [1,5,9,1,5,9], k = 2, t = 3
    输出：false
"""


def containsNearbyAlmostDuplicateBrute(nums, k, t):
    # 暴力求解 时间复杂度是O(n*k) 超时
    if len(nums)<=1:
        return False
    windowSize=min(len(nums), k+1)
    for i in range(len(nums)-windowSize+1):
        # 在该滑窗内满足下标的差小于等于滑窗大小
        window=nums[i:i+windowSize]
        window.sort()
        p=1
        while p<windowSize:
            if window[p]-t<=window[p-1]:
                return True
            else:
                p+=1
    return False


def containsNearbyAlmostDuplicateSlideWindowSet(nums, k, t):
    """滑动窗口+有序集合
    对于序列中元素x，左侧的至多k个元素，如果k个元素中有一个落在区间[x-t,x+t]中就找到了一对符合条件的元素。
    在有序集合中查找大于x-t的元素y，如果y存在且y小于等于x+t，就找到了符合条件的元素，完成检查后将x添加到有序集合
    如果有序集合中存在相同元素，直接返回True，
    """
    n=len(nums)
    rec=set()
    for i in range(n):

        rec.add(nums[i])
        if i>=k:
            rec.remove(nums[i-k])


def containsNearbyAlmostDuplicateBucket(nums, k, t):
    """桶排序，按照元素的大小进行分桶，维护一个滑动窗口。时间复杂度O(n), 空间复杂度O(min(n,k))
    设定桶的大小为t+1，因为对于x，影响的区间是[x-t, x+t]闭区间。注意桶的大小不能是2*t+1，这样会导致越界
    如果两个元素属于同一个桶，那么这两个元素符合条件，如果两个元素属于相邻桶，那么需要校验两个元素的差值不超过t；
    如果两个元素不属于同一个桶，也不属于相邻桶，那么这两个元素必然不符合条件
    如何建桶呢？遍历该序列， 假设当前元素x，检查x所属的桶是否已经存在元素，如果存在就找到了符合条件的元素
    """
    n=len(nums)
    bucket={}

    def getID(x, w):
        if x>=0:
            return int(x/w)
        return int((x+1)/w-1)

    for i in range(n):
        idx=getID(nums[i],t+1)
        if idx in bucket: # 当前桶存在数据
            return True
        if idx-1 in bucket and abs(nums[i]-bucket[idx-1])<=t:
            return True
        if idx+1 in bucket and abs(nums[i]-bucket[idx+1])<=t:
            return True

        bucket[idx]=nums[i]
        if i>=k:
            bucket.pop(getID(nums[i-k], t+1))

    return False






nums=[1,5,9,1,5,9]
k=2
t=3
res=containsNearbyAlmostDuplicateBucket(nums, k, t)
print(res)
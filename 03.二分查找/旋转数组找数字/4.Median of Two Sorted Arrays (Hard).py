# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/18
@function:
4. Median of Two Sorted Arrays (Hard)
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

在O(log(m+n))的时间复杂度内求两个数组的中位数
先将两个数组按照大小关系合并，然后根据合并之后的数组长度，求中位数

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
"""

def findMedianSortedArrays(nums1, nums2):
    merged=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    while i<len(nums1):
        merged.append(nums1[i])
        i+=1
    while j<len(nums2):
        merged.append(nums2[j])
        j+=1

    if len(merged)%2==0:
        mid=(len(merged)-1)//2
        return (merged[mid]+merged[mid+1])/2
    else:
        return merged[(len(merged)-1)//2]


nums1=[2]
nums2=[]
res=findMedianSortedArrays(nums1, nums2)
print(res)

# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/26
@function:

88. Merge Sorted Array (Easy)
https://leetcode.com/problems/merge-sorted-array/
题目描述
    给定两个 *有序* 数组，把两个数组合并为一个。
输入输出样例
    输入是两个数组和它们分别的长度 m 和 n。其中第一个数组的长度被延长至 m + n，多出的
    n 位被 0 填补。题目要求把第二个数组归并到第一个数组上， 不需要开辟额外空间。
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: nums1 = [1,2,2,3,5,6]
题解
    数组已经排好序，将两个指针放在两个数组的 *末尾*。每次将较大的数字复制到nums1的后面，然后向前移动一位。
    要定位nums1的末尾，所以需要第三个指针。便于复制

    直接利用m和n两个数组的指针，再额外创建一个pos指针， 初始位置为m+n-1，用于复制。如果nums1的数字已经复制完，
    要将nums2的数字继续复制，如果nums2的数字复制完剩余的数字就不需要改变了。
"""


def mergeSortedArray(nums1, m, nums2, n):
    pos = m + n - 1
    while m - 1 >= 0 and n - 1 >= 0:
        a = nums1[m - 1]
        b = nums2[n - 1]
        if a > b:
            nums1[pos] = a
            m -= 1
        else:
            nums1[pos] = b
            n -= 1
        pos -= 1

    while n - 1 >= 0:
        nums1[pos] = nums2[n - 1]
        pos -= 1
        n -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
res = mergeSortedArray(nums1, m, nums2, n)
print(res)

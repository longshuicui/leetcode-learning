# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/5/18
@function:
1442. 形成两个异或相等数组的三元组数目 (Medium)
https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
给你一个整数数组 arr 。
现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。
a 和 b 定义如下：
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]  # i和j的前缀异或结果
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] # j和k+1的异或结果
注意：^ 表示 按位异或 操作。
请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。
示例 1：
    输入：arr = [2,3,1,6,7]
    输出：4
    解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：
    输入：arr = [1,1,1,1,1]
    输出：10
示例 3：
    输入：arr = [2,3]
    输出：0
示例 4：
    输入：arr = [1,3,5,7,9]
    输出：3
示例 5：
    输入：arr = [7,11,12,9,5,2,7,17,22]
    输出：8
题解：
    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]  # i和j的前缀异或结果
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k] # j和k+1的前缀异或结果
    若a==b, 则有Si^Sj==Sj^Sk+1，所以Si=Sk+1

"""


def countTripletsTriple(arr):
    """时间复杂度为O(n^3)，空间复杂度为O(n)"""
    pre= [0]
    for num in arr:
        pre.append(num^pre[-1])

    ans=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j, len(arr)):
                if pre[i]==pre[k+1]:
                    ans+=1
    return ans


def countTripletsDouble(arr):
    """时间复杂度为O(n^2)，空间复杂度为O(n)
        j满足i<j<=k,所以不用去考虑j
    """
    pre= [0]
    for num in arr:
        pre.append(num^pre[-1])
    ans=0
    for i in range(len(arr)):
            for k in range(i+1, len(arr)):
                if pre[i]==pre[k+1]:
                    ans+=k-i
    return ans


def countTripletsOne(arr):
    """针对于二重循环，对于k，若i满足si=sk+1则有
    k-i1+k-i2+...k-im=m*k-(i1+i2+...+im),则需要统计i的个数m和i的下标和
    只需要一重循环就可以，时间复杂度O(n),空间复杂度O(n)
    """
    cnt, total={}, {}
    ans = s =0
    for k, num in enumerate(arr):
        t=s^num
        if t in cnt:
            ans+=cnt[t]*k-total[t]
        cnt[s]=cnt.get(s,0)+1
        total[s]=total.get(s,0)+k
        s=t
    return ans



arr=[2,3,1,6,7]
res=countTripletsOne(arr)
print(res)
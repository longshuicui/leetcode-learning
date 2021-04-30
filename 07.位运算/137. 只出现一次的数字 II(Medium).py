# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/4/14
@function:
137. 只出现一次的数字 II (Medium)
https://leetcode-cn.com/problems/single-number-ii/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
示例：
    输入: [2,2,3,2]
    输出: 3。

    输入: [0,1,0,1,0,1,99]
    输出: 99
题解：
考虑答案的第i个二进制位。对于数组中非答案的元素，每个元素都出现三次，对应着第i个位置是3个0或者3个1，无论那种情况，
都是3的倍数。所以，答案的第i个二进制位就是数组中所有元素的第i个二进制位之和除以3的余数。

"""

def singleNumber(nums):
    ans=0
    for i in range(32):
        total=sum((num>>i)&1 for num in nums) # 计算每一位的和
        if total%3:
            if i==31:
                ans -= (1<<i)
            else:
                ans |= (1<<i)
    return ans


nums=[2,2,3,2]
res=singleNumber(nums)
print(res)
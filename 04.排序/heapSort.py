# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/2/19
@function:
"""


def heapSort(nums):
    l=len(nums)
    # 构建大顶堆， 从非叶子节点开始倒序遍历，l//2-1正好是最后一个非叶子节点
    for i in range(l//2-1,-1,-1):
        buildHeap(nums, i, l-1)
    # 上面已经完成大顶堆的构造，最大值已经移到最前面，交换根节点和末尾节点的位置，重新调整大顶堆
    for j in range(l-1,-1,-1):
        nums[0],nums[j]=nums[j],nums[0]
        buildHeap(nums, 0, j-1)
    return nums


def buildHeap(nums,i, l):
    left, right=2*i+1, 2*i+2 # 左右子节点的下标
    largeIndex=i
    if left<=l and nums[i]<nums[left]:
        largeIndex=left
    if right<=l and nums[left]<nums[right]:
        largeIndex=right
    # 子节点和左右节点比较，得出三个元素之间较大的下标，如果较大下标不是父节点的下标，说明交换后需要调整大顶堆
    if largeIndex!=i:
        nums[i], nums[largeIndex]=nums[largeIndex], nums[i]
        buildHeap(nums, largeIndex, l)



import numpy as np
import time
nums=np.random.randint(1,20000,20000).tolist()
print(nums)
s=time.time()
nums=heapSort(nums)
print(nums)
print(time.time()-s)
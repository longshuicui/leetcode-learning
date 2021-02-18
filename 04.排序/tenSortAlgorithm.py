# -*- coding: utf-8 -*-
"""
@author: longshuicui
@date  :   2021/1/27
@function: 对一个无序数组，进行大小排序
划分方法有：稳定性/内外排序/时空复杂度
稳定性：如果 a 在 b 的前面，而 a 等于 b，稳定排序的结果 a 依然在 b 前面，不稳定排序 a 有可能在 b 的后面；
内外排序：内排序操作只用到内存， 外排序数据较大，需用到外部存储空间；
时空复杂度：时间复杂度和空间复杂度。运行时间和运行所需内存大小。

排序算法    平均时间复杂度     最好情况    最坏情况    空间复杂度   内外排序    稳定性
冒泡排序    O(n**2)           O(n)       O(n**2)     O(1)       in-place    稳定
选择排序    O(n**2)           O(n**2)    O(n**2)     O(1)       in-place    不稳定
插入排序    O(n**2)           O(n)       O(n**2)     O(1)       in-place    稳定
快速排序    O(nlogn)          O(nlogn)   O(n**2)     O(logn)    in-place    不稳定
归并排序    O(nlogn)          O(nlogn)   O(nlogn)    O(n)       out-place   稳定
桶排序      O(n+k)            O(n+k)     O(n**2)     O(n+k)     out-place   稳定
堆排序      O(nlogn)          O(nlogn)   O(nlogn)    O(1)       in-place    不稳定
如果数组已经排好序，冒泡和插入就只需要遍历一遍即可
如果基准值位置可以平分数组，那么就是logn， 不能就是n。遍历比较复杂度使n，所以最差为n**2，最优为nlogn
"""


def selectionSort(nums):
    """不断找到最小的放到起始位置或者最大的放到终末位置"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def bubbleSort(nums):
    """针对相邻元素的比较， 将大的元素移动到数组尾部"""
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


def insertionSort(nums):
    """插入到前面已排好的数组中"""
    for i in range(1, len(nums)):
        # while i>0 and nums[i]<nums[i-1]:
        #     nums[i-1], nums[i]=nums[i], nums[i-1]
        #     i-=1
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


def quickSort(nums):
    """选择一个值，小于该值的放到左边，大于该值的放到右边，分割成两部分，
    固定该值位置，对剩下两部分继续排序"""
    n = len(nums)

    def recursive(left, right):
        if left >= right:
            return nums
        pivot = left  # 取left为固定值
        i, j = left, right
        while i < j:
            while i < j and nums[j] > nums[pivot]:  # 寻找位于基准右侧且比基准小的数
                j -= 1
            while i < j and nums[i] <= nums[pivot]:  # 寻找位于基准左侧且比基准大的数
                i += 1
            nums[i], nums[j] = nums[j], nums[i]  # 两个数位置互换
        nums[pivot], nums[j] = nums[j], nums[pivot]  # 基准位置更换
        recursive(left, j - 1)
        recursive(j + 1, right)
        return nums

    return recursive(0, n - 1)


def mergeSort(nums):
    """将数组分为几个子序列，先将子序列内部排序，然后子序列间排序，最后合并成有序数组"""

    def merge(left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2  # 序列对半分
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


def heapSort(nums):
    """利用堆的数据结构进行排序，建堆，从底向上调整堆，使父节点的值大于子节点，构成大顶堆。"""

    def adjustHeapIteration(nums, startpos, endpos):
        newitem = nums[startpos]
        pos = startpos
        childpos = pos * 2 + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and nums[rightpos] >= nums[childpos]:
                childpos = rightpos
            if newitem < nums[childpos]:
                nums[pos] = nums[childpos]
                pos = childpos
                childpos = pos * 2 + 1
            else:
                break
        nums[pos] = newitem

    def adjustHeapRecursive(nums, startpos, endpos):
        pos = startpos
        childpos = pos * 2 + 1
        if childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and nums[rightpos] > nums[childpos]:
                childpos = rightpos
            if nums[childpos] > nums[pos]:
                nums[pos], nums[childpos] = nums[childpos], nums[pos]
                adjustHeapRecursive(nums, childpos, endpos)

    n = len(nums)
    # 建堆
    for i in reversed(range(n // 2)):
        adjustHeapIteration(nums, i, n)

    # 调整堆
    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        adjustHeapIteration(nums, 0, i)
    return nums


def bucketSort(nums, bucketSize):
    """输入数据服从均匀分布的， 将数据分到有限的桶里，桶内再继续排序，
    bucketSize 为不同数字的个数，例如bucketSize=5，桶内可以是[0,1,2,3,4], 也可以使10000个3
    """
    if len(nums) <= 1:
        return nums
    _min = min(nums)
    _max = max(nums)
    # 需要桶的个数
    bucketNum = (_max - _min) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    # 将数放到相应的桶中
    for num in nums:
        buckets[(num - _min) // bucketSize].append(num)  # 在这个步骤中实现了排序，下面只是将桶内数据放到额外内存空间中
    res = []
    for bucket in buckets:
        if not bucket: continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            if bucketNum == 1:  # 都装到一个桶里了，桶的容量太大了
                bucketSize -= 1
            res.extend(bucketSort(bucket, bucketSize))
    return res


if __name__ == '__main__':
    nums = [2,3,1,1]
    # nums=selectionSort(nums)
    # nums=bubbleSort(nums)
    # nums=insertionSort(nums)
    nums=quickSort(nums)
    # nums = mergeSort(nums)
    # nums=bucketSort(nums, bucketSize=2)
    # nums = heapSort(nums)
    print(nums)

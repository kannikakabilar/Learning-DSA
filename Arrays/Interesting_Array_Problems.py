# Interesting Array Problems

# Q1 Merge Sorted Array
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example1
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    last = m + n - 1

    # merge both the arrays in reverse order in nums1 array
    while m > 0 and n > 0:  # stopping when reached either end of the lists in reverse order
        if nums1[m - 1] > nums2[n - 1]:   # array 1 value is more,  
            nums1[last] = nums1[m - 1]    # than add it to the array last
            m -= 1                        # and deccrement m-- index pointers
        else:                             # when array 2 value is more or when 1 == 2
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1  # of the two conditions one will be true, & new last pointer will be defined

    # fill nums1 with leftover nums2 elements, not doing the same for nums1 cause nums1 element already stays in nums1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n, last = n - 1, last - 1

# Q2 Pascal's Triangle
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 
(Google a picture of PAscal's triangle)

Example1
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
def generate(numRows: int) -> List[List[int]]:
    l = []
    for i in range(numRows):
        l.append([])
        for j in range(i+1):
            if i == 0 or i == 1:
                l[i].append(1)
            elif j == 0 or j == i:
                l[i].append(1)
            else:
                l[i].append(l[i-1][j-1] + l[i-1][j])
    return l

# Q3 Best Time To Buy And Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example1
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example2
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
def maxProfit(prices: List[int]) -> int:

    if prices != []:
        min = prices[0]
    diff = 0
    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        if diff < prices[i] - min:
            diff = prices[i] - min
    return diff

# Q3 Single Number
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example1
Input: nums = [4,1,2,1,2]
Output: 4
"""

def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

    

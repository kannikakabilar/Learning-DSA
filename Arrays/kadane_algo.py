# Maximum Subarrya
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(nums: List[int]) -> int:
    # Kadane's algorithm
    maxi=nums[0] 
    # Only if the resulting sum needs to contain at least 1 element, 
    # if empty list can be included => then it should equal 0
    sums=0
    for i in range(len(nums)):
        sums+=nums[i]
        maxi=max(sums,maxi)
        # To ensure that sums doesn't keep adding negatives 
        # because it wont result in a higher sum from sub array
        if sums<0: 
            sums=0
    
    return maxi

# Kadane's algorithm can also be used to find the minimum subarray
def minSubArray(nums: List[int]) -> int:
    # Kadane's algorithm
    mini=nums[0] 
    # Only if the resulting sum needs to contain at least 1 element, 
    # if empty list can be included => then it should equal 0
    sums=0
    for i in range(len(nums)):
        sums+=nums[i]
        mini=min(sums,mini) # Basically change max to min
        # To ensure that sums doesn't keep adding positives 
        # because it wont result in a lower sum from sub array
        # Basically just change the sign
        if sums>0: 
            sums=0
    
    return mini

# Best Time to Buy and Sell Stock
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
    maxCur = 0
    maxSoFar = 0

    for i in range(1, len(prices)):
        maxCur += prices[i] - prices[i-1]
        maxCur = max(0, maxCur)
        maxSoFar = max(maxCur, maxSoFar)

    return maxSoFar


	


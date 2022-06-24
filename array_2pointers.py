from multiprocessing.dummy import Array

# DOUBLE POINTERS
# Q1 Remove Duplicates from Sorted Array (return the size of array)
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
def removeDuplicates(nums: List[int]) -> int:
    length = len(nums)
    if length == 1:    # If length of array is 1, return 1
        return 1
    # more than 1 element
    else:
        j = 0                          # i and j double pointers
        i = 1
        count = 1                      # If len of array is greater than 1, then it has atleast 1 distinct element
        
        for i in range(length):        # Loop through the array
            if nums[i] != nums[j]:
                j += 1                 # j only increases if i reaches a distinct element
                nums[j] = nums[i]      # set the next repeated element into the next distinct, else set the next element as itself
                count += 1             # keeps track of total distinct elements
        
        return count

# Q2 Remove Given Element From Array (Return the output size of the array)
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

def removeElement(nums: List[int], val: int) -> int:
    j = 0                        # Create 2 pointers i and j
    i = 0
    for j in range:              # Loop through array elements - *Note: j goes through all index of the array
        if nums[j] != val:       
            nums[i] = nums[j]    # sets it to the same element if val does not exist in the array, else at index i where it equals val => set it to the next non-val element in the array
            i += 1               # value of i (index in array) remains the same if the current value is equal to val so that it can be set to the next non-val element
    return i

# Q3 Move Zeros to the End of the Array while Maintaing the Order (Return the Array)
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(nums: List[int]) -> None:
    i = 0                        # Create 2 pointers i and j
    j = 0
    zero = 0                     # keeps track of total number of zeros ina array
    for j in range(len(nums)):   # loop through the array
        if nums[j] != 0:         # similar to above problem, remove zeros and collect all non-zero elements ito the front of the list
            nums[i] = nums[j]
            i += 1
        else:
            zero += 1
    for j in range(zero):       # for total number of zeros, set the zeros at the end of the array
        nums[len(nums)-(j+1)] = 0
        
    return nums


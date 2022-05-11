"""
minSubArrayLen - return minimal length of a contiguous subarray
@target: target sum
@nums: list of integers
Return : 0 if minLen less than 0 otherwise minLen
(slide window technique)
leetcode 209
"""

def minSubArrayLen(target,nums):
    minLen = float('inf')
    sumElement = 0
    left = 0
    for right in range(0,len(nums)):
        sumElement += nums[right]
        while sumElement >= target:
            minLen = (right - left + 1)
            sumElement -= nums[left]
            left += 1
    return 0 if minLen == float('inf') 0 else minLen


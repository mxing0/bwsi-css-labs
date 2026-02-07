"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    maxSum = float('-inf')
    currentSum = 0


    for num in nums:
        currentSum += num

        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum

# Example usage:
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main()
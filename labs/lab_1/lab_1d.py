"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def two_sum(nums: list[int], target: int) -> list[int]:
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return [] 

# Example usage:
def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()
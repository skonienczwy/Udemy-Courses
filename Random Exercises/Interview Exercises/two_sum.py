# Problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 9

# Constraints
# 2 ≤ nums.length ≤ 10⁴
# -10⁹ ≤ nums[i] ≤ 10⁹
# -10⁹ ≤ target ≤ 10⁹


nums = [2,7,11,15] 
target = 9


# def two_sum(nums, target):
#     sum = 0
#     sum_of_indices = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             sum = nums[i]+ nums[j]
#             if sum == target:
#                 sum_of_indices.append(i)
#                 sum_of_indices.append(j)
#     return sum_of_indices




def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]   # return as a list [index1, index2]
        seen[num] = i
    return []

print(two_sum(nums, target))
# Top K Frequent Elements
# Difficulty: Medium
# Pattern: Hash Map + Heap / Sorting
# Problem
# Given an integer array nums and an integer k, return the k most frequent elements.
# Example
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Constraints
# 1 ≤ nums.length ≤ 10⁵
# -10⁴ ≤ nums[i] ≤ 10⁴
# 1 ≤ k ≤ number of unique elements

    
    

nums = [1,1,1,2,2,3]
k = 2


group = {}
for key in nums:
    group[key] = sorted(nums, key=nums.get, reverse=True)
    
print(group)  

















# def top_k_elements(nums, k):
#     group = {}
#     for key in nums:
#         group[key] = group.get(key, 0) + 1

#     top_k = sorted(group, key=group.get, reverse=True)[:k]
#     return top_k


# print(top_k_elements(nums, k))        
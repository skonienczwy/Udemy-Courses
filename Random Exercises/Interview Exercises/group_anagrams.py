# Group Anagrams
# Difficulty: Medium
# Pattern: Hash Map + Sorting

# Problem
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# Example
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Constraints
# 1 ≤ strs.length ≤ 10⁴
# 0 ≤ strs[i].length ≤ 100
# strs[i] consists of lowercase English letters 


strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagram(strs):
    anagrams = {}
    for word in strs:
        key = "".join(sorted(word)) 
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())


print(group_anagram(strs))




# def groupAnagrams(strs):
#     groups = {}

#     for word in strs:
#         key = ''.join(sorted(word))  # canonical anagram key

#         if key not in groups:
#             groups[key] = []         # create list if key not exists

#         groups[key].append(word)     # add word to correct group

#     return list(groups.values())


# print(groupAnagrams(strs))
# Problem: Valid Anagram
# Platform: LeetCode
# Language: Python
# Approach: Using Counter (Hash Map Frequency Comparison)

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

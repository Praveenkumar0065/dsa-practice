# Problem: Valid_Anagram
# Platform: LeetCode
#Language: Pyhton

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

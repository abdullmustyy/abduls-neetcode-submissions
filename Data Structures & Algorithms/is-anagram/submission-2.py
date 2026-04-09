class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
        
"""
Sorting:
- sort s and t
- do an equality check for the sorted s and t string
- if they are equal then they are anagrams

"""
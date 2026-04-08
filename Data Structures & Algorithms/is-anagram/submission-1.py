class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        if len(s) == len(t):
            for char in s:
                if char not in s_map:
                    s_map[char] = s.count(char)
            
            for char in t:
                if char not in t_map:
                    t_map[char] = t.count(char)

            for k in s_map:
                if k in s_map and k in t_map:
                    if s_map[k] != t_map[k]:
                        return False
                else:
                    return False

            return True
        else:
            return False
        
"""
Brute force:
- compare the length of s and t (they should be equal)
- track the length of each chars in s and t
- iterate over s map to check that all chars have the same
lengths as in t
- return false at the first negation
- return true if they all have the same length

"""
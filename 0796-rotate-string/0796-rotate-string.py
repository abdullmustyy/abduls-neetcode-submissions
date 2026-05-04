class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)

"""
- i learned that if we concatenate s to it self, then
it will consist of every possible rotation occurrence
- check whether goal is in the concatenated string and
return the boolean result

"""
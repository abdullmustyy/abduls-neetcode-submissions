class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        s_rot = s

        for _ in range(len(s)):
            if s_rot == goal:
                return True
            s_rot = s_rot[1:] + s_rot[0]

        return False

"""
- define a variable to track the rotation
- iterate over s, compare the equality of s and goal
- remove the current char of s in from the stored rotation
and add it to the end of s

"""
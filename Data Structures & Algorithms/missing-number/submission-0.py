class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

"""
- iterate over the range of the nums length plus one
to ensure that we account for cases where the highest
number in the range is the missing one
- range(n + 1) where n = len(nums)
- return the number in nums that is missing from the
range

"""
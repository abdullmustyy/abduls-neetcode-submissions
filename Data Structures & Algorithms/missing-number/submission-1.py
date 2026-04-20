class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

"""
- the length of the nums lisr is the range where the
missing number lies
- to get the range of numbers in the nums list from
lowest to highest we use range(n + 1) -> n = len(nums)
- substract the sum of nums from that of the range to
reveal the missing number

"""
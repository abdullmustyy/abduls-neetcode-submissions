class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # The set() function removes duplicates from an array
        # Compare the actual length and the set() length of the nums array
        # If they aren't equal, then there is a duplicate

        return len(nums) != len(set(nums))
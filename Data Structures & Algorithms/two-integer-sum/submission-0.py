class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        

"""
hash map:
- define prev_map to track values and indices -> {value: index}
- enumaerate the nums array and iterate over it -> [(i, n)]
- substract the current n from the target -> diff
- if diff is in prev_map, return it's index and the current n's
index
- if not, add n and i to prev_map

"""
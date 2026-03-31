class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, num in enumerate(nums):
            if target - num in maps:
                return [maps[target - num], i]
            maps[num] = i
        return [-1,-1]
        
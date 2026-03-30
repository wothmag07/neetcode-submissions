class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        for i in range(0, max_val):
            if i not in nums:
                return i
        return max_val+1
        
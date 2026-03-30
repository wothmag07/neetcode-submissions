class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        xor = len(nums)
        for i in range(len(nums)):
            xor = xor ^ i ^ nums[i]
        return xor
        
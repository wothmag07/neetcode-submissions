class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            if val > n/2:
                return key

        
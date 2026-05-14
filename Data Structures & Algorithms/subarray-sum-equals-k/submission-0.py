class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        sum_freq = {0:1}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_freq:
                count += sum_freq[curr_sum - k]
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1
        return count


            

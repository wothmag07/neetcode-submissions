class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsize = float("inf")
        lptr = 0
        tot = 0
        for rptr in range(len(nums)):
            tot += nums[rptr]
            while tot >= target:
                minsize = min(minsize, rptr-lptr+1)
                tot -= nums[lptr]
                lptr += 1
        return 0 if minsize == float("inf") else minsize
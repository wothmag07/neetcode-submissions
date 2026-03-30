class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        lptr = 0
        for rptr in range(k-1 , len(nums)):
            val = max(nums[lptr: rptr+1])
            out.append(val)
            lptr += 1
        return out
        
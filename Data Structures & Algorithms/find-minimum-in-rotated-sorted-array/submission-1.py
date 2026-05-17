class Solution:
    def findMin(self, nums: List[int]) -> int:
        lptr, rptr = 0, len(nums)-1
        while lptr < rptr:
            mid = (lptr + rptr)//2
            if nums[mid] < nums[rptr]:
                rptr = mid
            else:
                lptr = mid+1
        return nums[lptr]
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        lptr, rptr = 0, len(nums)-1
        while lptr <= rptr:
            mid = (lptr+rptr) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lptr = mid+1
            else:
                rptr = mid-1
        return -1
        
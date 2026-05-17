class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        lptr, rptr = 0, len(nums)-1
        while lptr <= rptr:
            mid = (lptr + rptr) // 2
            if nums[mid] == target:
                return True

            if nums[lptr] == nums[mid] == nums[rptr]:
                lptr += 1
                rptr -= 1

            elif nums[lptr] <= nums[mid]:
                if nums[lptr] <= target < nums[mid]:
                    rptr = mid-1
                else:
                    lptr = mid+1
            else:
                if nums[mid] < target <= nums[rptr]:
                    lptr = mid + 1
                else:
                    rptr = mid-1
        return False
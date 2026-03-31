class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lptr, rptr = i+1, len(nums)-1
            while lptr < rptr:
                out = nums[i] + nums[lptr] + nums[rptr]
                if out > 0:
                    rptr -= 1
                elif out < 0:
                    lptr += 1 
                else:
                    res.append([num, nums[lptr], nums[rptr]])
                    lptr +=1
                    while lptr < rptr and nums[lptr] == nums[lptr-1]:
                        lptr += 1
        return res
            

        
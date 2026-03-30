class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            lptr, rptr = i+1, len(nums)-1
            while lptr < rptr:
                threesum = num + nums[lptr] + nums[rptr]
                if threesum > 0:
                    rptr -= 1
                elif threesum < 0:
                    lptr += 1
                else:
                    out.append([num, nums[lptr], nums[rptr]])
                    lptr += 1
                    while nums[lptr] == nums[lptr-1] and lptr < rptr:
                        lptr += 1
        return out
                

        

        
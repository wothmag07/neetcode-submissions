class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        res = []

        for i in range(len(nums)-3):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                lptr, rptr = j+1, len(nums)-1

                while lptr < rptr:
                    tot = nums[i] + nums[j] + nums[lptr] + nums[rptr]
                    if tot == target:
                        res.append([nums[i], nums[j], nums[lptr], nums[rptr]])
                        lptr += 1
                        rptr -= 1

                        while lptr < rptr and nums[lptr] == nums[lptr-1]:
                            lptr += 1
                        while lptr < rptr and nums[rptr] == nums[rptr+1]:
                            rptr -= 1
                    
                    elif tot < target:
                        lptr += 1
                    else:
                        rptr -= 1
        
        return res
        
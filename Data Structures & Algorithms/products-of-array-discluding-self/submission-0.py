class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            out = 1
            for j in range(len(nums)):
                if i!=j:
                    out *= nums[j]
            ans.append(out)
        return ans

        
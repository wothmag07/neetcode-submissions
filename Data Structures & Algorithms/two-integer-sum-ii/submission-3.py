class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr, rptr = 0, len(numbers)-1
        while lptr < rptr:
            if numbers[lptr] + numbers[rptr] < target:
                lptr += 1
            elif numbers[lptr] + numbers[rptr] > target:
                rptr -= 1
            else:
                return [lptr+1, rptr+1]
        return [-1,-1]
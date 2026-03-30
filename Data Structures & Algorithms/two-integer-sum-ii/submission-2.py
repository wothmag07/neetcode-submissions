class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr, rptr =  0, len(numbers)-1
        while lptr < rptr:
            currsum = numbers[lptr] + numbers[rptr]
            if currsum > target:
                rptr -= 1
            elif currsum < target:
                lptr += 1
            else:
                return[lptr+1, rptr+1]
        return []
        
        
        
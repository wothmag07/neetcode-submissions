class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            lptr, rptr = i+1, len(numbers)-1
            out = target - numbers[i]
            while lptr <= rptr:
                mid = (lptr + rptr) // 2
                if numbers[mid] == out:
                    return [i+1, mid+1]
                elif numbers[mid] < out:
                    lptr = mid + 1
                else:
                    rptr = mid - 1
        return []
        
        
        
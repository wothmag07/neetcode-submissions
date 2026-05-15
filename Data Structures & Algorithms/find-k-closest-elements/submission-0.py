class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lptr, rptr = 0, len(arr)-k
        while lptr < rptr:
            mid = (lptr + rptr) // 2
            if x - arr[mid] > arr[mid+k] - x:
                lptr = mid+1
            else:
                rptr = mid
        return arr[lptr: lptr+k]
        
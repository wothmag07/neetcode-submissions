class Solution:
    def trap(self, height: List[int]) -> int:
        lptr = 0
        n = len(height)
        summ = 0

        while lptr < n-1:
            mid = lptr+1
            curr = 0
            while mid < n and height[mid] < height[lptr]:
                curr += height[lptr] - height[mid]
                mid += 1
                if mid >= n:
                    curr = 0
                    break
            summ += curr
            lptr = mid

        rptr = n-1
        while rptr > 0:
            mid = rptr-1
            curr = 0
            while mid >= 0 and height[mid] <= height[rptr]:
                curr += height[rptr] - height[mid]
                mid -= 1
                if mid < 0:
                    curr = 0
                    break
            summ += curr
            rptr = mid
        
        return summ


        
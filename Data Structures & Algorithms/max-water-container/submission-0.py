class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr, rptr = 0, len(heights)-1
        maxarea = 0
        while lptr < rptr:
            area = (rptr - lptr)* min(heights[lptr], heights[rptr])
            maxarea = max(area, maxarea)
            if heights[lptr] < heights[rptr]:
                lptr += 1
            elif heights[lptr] >= heights[rptr]:
                rptr -= 1
            
        return maxarea
        
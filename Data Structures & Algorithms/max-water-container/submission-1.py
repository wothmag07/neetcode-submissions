class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        lptr, rptr = 0, len(heights)-1
        maxarea = float("-inf")
        while lptr < rptr:
            area = min(heights[lptr], heights[rptr])*(rptr-lptr)
            maxarea = max(maxarea, area)
            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return maxarea
        
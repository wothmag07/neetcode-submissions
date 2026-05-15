class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        lptr, rptr = 0, len(height)-1

        tot = 0
        leftmax = height[lptr]
        rightmax = height[rptr]

        while lptr < rptr:
            if leftmax < rightmax:
                lptr += 1
                leftmax = max(leftmax, height[lptr])
                tot += leftmax - height[lptr]
            else:
                rptr -= 1
                rightmax = max(rightmax, height[rptr])
                tot += rightmax - height[rptr]
        return tot
        
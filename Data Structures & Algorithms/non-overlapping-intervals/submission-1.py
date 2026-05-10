class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        """
        intervals=[[1,100],[11,22],[1,11],[2,12]]


        """
        last_end = intervals[0][1]
        count = 0

        for x, y in intervals[1:]:
            if x < last_end:
                count += 1
                last_end = min(last_end, y)
            else:
                last_end = y
            
        return count

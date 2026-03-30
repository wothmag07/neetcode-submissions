import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        
        for num, count in counter.items():
            freq[count].append(num)
        
        out = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                out.append(num)
                print(out)
                if len(out) == k:
                    return out



        
        



        
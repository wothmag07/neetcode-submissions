class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        while i < m:
            nums3.append(nums1[i])
            i += 1
        while j < n:
            nums3.append(nums2[j])
            j += 1
        
        leng = len(nums3)
        if leng%2 == 0:
            return (nums3[leng//2 - 1] + nums3[leng//2]) / 2.0
        else:
            return nums3[leng//2]


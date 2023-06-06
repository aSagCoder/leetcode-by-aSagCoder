class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i = 0
        j = 0

        #merge the arrays together into a new array called nums3

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        nums3.extend(nums1[i:])
        nums3.extend(nums2[j:])

        #calculate median

        n = len(nums3)
        if n % 2 == 1:
            return nums3[n // 2]
        else:
            mid1 = nums3[n // 2 - 1]
            mid2 = nums3[n // 2]
            return (mid1 + mid2) / 2.0

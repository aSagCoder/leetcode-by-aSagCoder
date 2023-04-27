from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        #reverse the entire array 
        nums.reverse()

        #reverse the first k elements in array 
        self.reverse(nums, 0, k-1)
        #reverse the remaining n-k elements
        self.reverse(nums, k, n-1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        

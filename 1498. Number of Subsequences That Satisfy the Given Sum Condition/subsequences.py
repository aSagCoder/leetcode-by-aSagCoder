class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = int(1e9) + 7
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        count = 0
        
        # Precompute the powers of 2
        powers_of_two = [1] * (n + 1)
        for i in range(1, n + 1):
            powers_of_two[i] = (powers_of_two[i - 1] * 2) % MOD
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers_of_two[right - left]) % MOD
                left += 1
            else:
                right -= 1
        
        return count

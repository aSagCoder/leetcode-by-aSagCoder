class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [num_dict[target - nums[i]], i]
            num_dict[nums[i]] = i 
        return []

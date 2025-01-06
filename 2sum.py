class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers and their indices
        seen = {}

        # Loop through the list
        for i, num in enumerate(nums):
            complement = target - num 

            if complement in seen:
                return [seen[complement], i]

            
            seen[num] = i

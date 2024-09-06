class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index == index2:
                    continue
                if num + num2 == target:
                    return [index, index2]
        
    

# Given an array of integers, 
# return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have
#  exactly one solution, 
#  and you may not use the same element twice.


class Solution():
    def twoSum(self, nums, target):
        dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dict:
                return [dict[complement], index]
            dict[value] = index 
        return []


instance = Solution()
result = instance.twoSum([2, 7, 11, 15], 9)
print(result)
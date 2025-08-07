#0001. Two Sum
#思路：使用字典记录数字及索引 来回读取
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [dict[diff],i]
            else:
                dict[num] = i
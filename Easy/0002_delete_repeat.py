#灵活运用双指针赋值 return
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums :
            return 0
        slow = 0
        for fast in range(1,len(nums)) :
            if nums[fast] != nums[slow] :
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
__author__ = 'liu.xingjie'

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        sz = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[sz] = nums[i]
                sz += 1
        return sz

s = Solution()
res = s.removeDuplicates([1,1,1,2,2,2])
print res

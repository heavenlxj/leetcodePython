__author__ = 'liu.xingjie'

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True

s=Solution()
res= s.canJump([2,3,1,1,4])
print res
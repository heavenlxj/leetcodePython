__author__ = 'liu.xingjie'

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        length = len(nums)
        if length == 0: return []
        if length == 1: return [nums]
        nums.sort()
        res = []
        previousNum = None
        for i in range(length):
            if nums[i] == previousNum: continue
            previousNum = nums[i]
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res

s= Solution()
res = s.permuteUnique([1,1,2])
print res
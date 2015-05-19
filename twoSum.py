__author__ = 'liu.xingjie'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if dict.get(target-nums[i], None) == None:
                dict[nums[i]] = i
            else:
                return (dict[target-nums[i]] + 1, i + 1)


s=Solution()
res = s.twoSum([3,2,4], 6)
print res
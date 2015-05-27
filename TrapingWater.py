__author__ = 'liu.xingjie'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, height):
        leftmosthigh = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax: leftmax = height[i]
            leftmosthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax: rightmax = height[i]
            if min(rightmax, leftmosthigh[i]) > height[i]:
                sum += min(rightmax, leftmosthigh[i]) - height[i]
        return sum

s= Solution()
res=s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print res
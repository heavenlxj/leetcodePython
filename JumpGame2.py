__author__ = 'liu.xingjie'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        maxj, maxn, tms = 0, 0, 0
        for i in range(len(A) - 1):
            maxn = max(maxn, A[i] + i)
            if i == maxj:
                maxj, tms = maxn, tms + 1
        return tms

s=Solution()
res = s.jump([2,3,1,1,4,1,1,1,3,1,1])
print res

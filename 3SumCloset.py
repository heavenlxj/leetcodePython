__author__ = 'liu.xingjie'

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        ans = None
        for i in range(len(num)):
            l, r = i + 1, len(num) - 1
            while (l < r):
                sum = num[l] + num[r] + num[i]
                if ans is None or abs(sum- target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        return ans

s=Solution()
res = s.threeSumClosest([-1,2,1,-4], 1)
print res
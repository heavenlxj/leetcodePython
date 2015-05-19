__author__ = 'liu.xingjie'

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0: return False
        k = 1
        while x / k >= 10: k *= 10
        while x > 0:
            if x / k != x % 10: return False
            x = (x - x / k * k) / 10
            k /= 100
        return True

s = Solution()
res = s.isPalindrome(1234567654321)
print 'Yes' if res else 'No'
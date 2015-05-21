class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return self.pow(x, n)


    def pow(self, x, n):
        if n == 0:
            return 1

        xx = self.pow(x, n >> 1)
        xx*= xx
        if n & 1: xx *=x
        return xx

s = Solution()
print s.myPow(3, 4)
print s.myPow(4, -2)
print s.myPow(-4, 2)
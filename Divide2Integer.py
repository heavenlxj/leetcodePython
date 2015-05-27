__author__ = 'liu.xingjie'

import timeit
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        max, min = 2**31 -1, -2**31
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
        if res > max:
            res = max
        elif res < min:
            res = min

        return res

s = Solution()
res = s.divide(100, 2)
print
res = s.divide(1000, 1)
print res
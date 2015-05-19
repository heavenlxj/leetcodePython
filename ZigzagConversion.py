__author__ = 'liu.xingjie'

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1 or len(s) == 0:
            return s
        res, lens = [], len(s)
        add, now = [nRows * 2 - 2, 0], 0
        for i in range(nRows):
            if i < lens:
                res.append(i)
            while res[-1] + add[now] < lens:
                if add[now] > 0:
                    res.append(res[-1] + add[now])
                now ^= 1
            add, now = [add[0] - 2, add[1] + 2], 0
        return ''.join([s[i] for i in res])

s = Solution()
print s.convert("PAYPALISHIRINGTIHKDLELSLGNF", 5)

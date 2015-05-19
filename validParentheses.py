__author__ = 'liu.xingjie'

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        dct = {'(':')', '[':']', '{':'}'}
        stk = []
        for c in s:
            if dct.get(c, None):
                stk.append(c)
            elif len(stk) == 0 or dct[stk[-1]] != c:
                return False
            else:
                stk.pop()
        return True if len(stk) == 0 else False

s = Solution()
res = s.isValid('{}[]()([{}])')
print res

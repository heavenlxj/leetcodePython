__author__ = 'liu.xingjie'

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        self.ans, tmp = [], []
        lb = 0
        self.dfs(lb, 0, n, tmp)
        return self.ans

    def dfs(self, lb, p, n, tmp):
        if p == n * 2:
            self.ans.append(''.join(tmp))
            return
        if lb < n:
            tmp.append('(')
            self.dfs(lb + 1, p + 1, n, tmp)
            tmp.pop()
        if p - lb < lb:
            tmp.append(')')
            self.dfs(lb, p + 1, n, tmp)
            tmp.pop()
s= Solution()
res = s.generateParenthesis(3)
print res
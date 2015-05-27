__author__ = 'liu.xingjie'

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.ans, tmp = [], []
        self.dfs(candidates, target, 0, 0, tmp)
        return self.ans
    def dfs(self, candidates, target, p, now, tmp):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(candidates)):
            if now + candidates[i] <= target:
                tmp.append(candidates[i])
                self.dfs(candidates, target, i, now+candidates[i], tmp)
                tmp.pop()

s=Solution()
res= s.combinationSum([2,3,6,7], 7)
print res
__author__ = 'liu.xingjie'

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if len(s) == 0 or len(wordDict) == 0:
            return False

        dp = [ 0 ]
        for i in range(1, len(s) + 1):
            for j in xrange( len( dp ) - 1, -1, -1):
                substr = s[dp[j] : i]
                if substr in wordDict:
                    dp.append(i)
                    break
        return dp[-1] == len(s)

s= Solution()
res = s.wordBreak('leetcodetest', ['leet', 'code'])
print res
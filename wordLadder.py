__author__ = 'liu.xingjie'
#BFS
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set of string!!!wordDict is a set type!!!
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        wordDict.add(endWord)
        aplha = 'abcdefghijklmnopqrstuvwxyz'
        q = []
        q.append((beginWord, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == endWord: return currlen
            for i in range(len(beginWord)):
                part1 = currword[:i]; part2 = currword[i+1:]
                for j in aplha:
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in wordDict:
                            q.append((nextword, currlen+1));
                            wordDict.remove(nextword)
        return 0

s=Solution()
test = ['hot','dot','dog','lot','log']
d = set(test)
res= s.ladderLength('hit', 'cog', d)
print res
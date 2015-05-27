__author__ = 'liu.xingjie'

class Solution:
    # @return a string
    def count(self,s):
        t, count,curr = '', 0, '#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s

s = Solution()
print s.countAndSay(3)
print s.countAndSay(2)
print s.countAndSay(4)
print s.countAndSay(5)
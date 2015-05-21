__author__ = 'liu.xingjie'

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        nHead = ListNode(0)
        nHead.next = head
        p2, lenl = head, 0
        while p2: p2, lenl = p2.next, lenl + 1
        now, pre, ind = head, nHead, 1
        preHead, preHeadNext = nHead, head
        while now:
            if lenl - ind < lenl % k:
                break
            next = now.next
            now.next = pre
            if ind % k == 0:
                preHead.next = now
                preHeadNext.next = next
                preHead = preHeadNext
                pre = preHead
                preHeadNext = next
            else:
                pre = now
            now, ind = next, ind + 1
        return nHead.next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
f=ListNode(6)
g=ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
s = Solution()
res = s.reverseKGroup(a, 3)
print res


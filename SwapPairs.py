__author__ = 'liu.xingjie'

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        nHead = ListNode(0)
        nHead.next = head
        p1, p2 = nHead, head
        while p2 and p2.next:
            p2 = p2.next.next
            p1.next.next.next = p1.next
            p1.next = p1.next.next
            p1.next.next.next = p2
            p1 = p1.next.next
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
res = s.swapPairs(a)
print res
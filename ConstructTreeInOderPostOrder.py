__author__ = 'liu.xingjie'

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

s = Solution()
res = s.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])
print res

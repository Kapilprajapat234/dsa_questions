# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getdepth(self , root):
        if  root == None :
            return 0 
        left  = self.getdepth(root.left)
        right = self.getdepth(root.right)

        self.diameter  = max(self.diameter , left + right)

        return 1 + max(left , right)

    
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0 
        self.getdepth(root)
        return self.diameter 

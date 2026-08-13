# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getdepth(self, root):
        if root == None :
            return 0
        left = self.getdepth(root.left)
        right = self.getdepth(root.right)


        return 1 + max(left, right)

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None :
            return True 
        lefthight = self.getdepth(root.left)
        righthight = self.getdepth(root.right)

        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)


        return abs(lefthight - righthight) <= 1 and left_balanced and right_balanced

        
        

        
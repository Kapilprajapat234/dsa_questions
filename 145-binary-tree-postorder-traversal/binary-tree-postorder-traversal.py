# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root):
        if root == None :
            return 
        self.helper(root.left)
        self.helper(root.right)
        self.arr.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.arr = []
        self.helper(root)
        return self.arr
        
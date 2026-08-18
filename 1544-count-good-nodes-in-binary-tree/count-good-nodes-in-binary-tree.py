# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self , root , max_value):
        if root == None :
            return 0
        count = 0 

        if root.val >= max_value:
            count += 1 
        else :
            count = 0 
        
        max_value = max(max_value, root.val)



        left = self.helper(root.left , max_value)
        right = self.helper(root.right , max_value)

        return count + left + right
        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.helper(root , root.val)
      
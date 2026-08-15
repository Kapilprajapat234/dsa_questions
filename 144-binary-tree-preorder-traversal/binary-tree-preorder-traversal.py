# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def __init__(self):
    #     self.arr = []
    def helper (self, root):
        if root == None :
            return 
        self.arr.append(root.val)

        self.helper(root.left)
        self.helper(root.right)
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.arr = []
        self.helper(root)
        return self.arr
        # if root == None :
        #     return self.arr

        
        # self.arr.append(root.val)

        # left = self.preorderTraversal(root.left)
       
        # right = self.preorderTraversal(root.right)
       

        # return self.arr

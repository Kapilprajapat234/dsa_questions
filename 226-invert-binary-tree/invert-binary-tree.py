# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        result = []
        que = deque()
        que.append(root)
        while len(que) != 0 :
            e = que.popleft()
            e.left, e.right = e.right, e.left
            if e.left is not None :
                que.append (e.left)
            if e.right is not None :
                que.append(e.right)
        
        return root
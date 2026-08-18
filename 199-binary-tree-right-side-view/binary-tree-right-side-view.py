# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []
        que = deque([root])

        while que:
            level = []

            for i in range(len(que)):
                e = que.popleft()
                level.append(e.val)

                if e.left is not None:
                    que.append(e.left)

                if e.right is not None:
                    que.append(e.right)

            result.append(level[-1])

        return result
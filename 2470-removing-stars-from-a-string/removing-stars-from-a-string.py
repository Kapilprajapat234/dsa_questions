class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if not stack and s[0] != '*':
                stack.append(s[i])
            elif s[i] != '*':
                stack.append(s[i])
            elif s[i] == '*':
                stack.pop()
        s = "".join(stack)
        return s
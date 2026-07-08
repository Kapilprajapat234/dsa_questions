class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if not stack and  not i.isdigit():
                stack.append(i)
            elif not i.isdigit():
                stack.append(i)
            elif i.isdigit():
                stack.pop()
        s = "".join(stack)
        return s 

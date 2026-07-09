class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 3 :
                if stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a' :
                    stack.pop()
                    stack.pop()
                    stack.pop()
            
        if len(stack) == 0 :
            return True 
        else :
            return False 

            
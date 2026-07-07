from math import trunc
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)) :
            try:
                stack.append(int(tokens[i]))
                continue
            except ValueError:
                pass 
            
            if tokens[i] ==  "+" :
                A = stack.pop()
                B = stack.pop()
                X = A + B
                stack.append(X)

            elif tokens[i] ==  "-" :
                A = stack.pop()
                B = stack.pop()
                X = B- A
                stack.append(X)
            elif tokens[i] ==  "*" :
                A = stack.pop()
                B = stack.pop()
                X = A * B
                stack.append(X)
            elif tokens[i] ==  "/" :
                A = stack.pop()
                B = stack.pop()
                X = trunc(float(B) / float(A))
                stack.append(X)
            
        
        return stack[-1]



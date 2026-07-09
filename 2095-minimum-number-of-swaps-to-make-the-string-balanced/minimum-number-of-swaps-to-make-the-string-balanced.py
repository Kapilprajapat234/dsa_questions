class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        balance = 0 
        for i in s :
            if i == '[':
                balance += 1 
            elif  i  == ']' and balance > 0 :
                balance -=  1 
            elif i == ']' and balance == 0 :
                count += 1 
        count = (count + 1) // 2
        return count 
        
        
            
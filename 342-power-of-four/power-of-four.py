class Solution(object):
    i = 0 
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 4 ** self.i == n :
            return True  
        elif 4 ** self.i > n :
            return False 
        else :
            self.i += 1 
            return self.isPowerOfFour(n)
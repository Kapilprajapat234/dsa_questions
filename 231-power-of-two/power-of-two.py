class Solution(object):
    i = 0 
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 2 ** self.i == n :
            return True 
        elif 2 ** self.i > n :
            return False 
        else : 
            self.i += 1 
            return self.isPowerOfTwo(n)

        

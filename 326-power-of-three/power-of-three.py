class Solution(object):
    i = 0 
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 3 ** self.i == n :
            return True 
        elif 3 ** self.i > n :
            return False 
        else :
            self.i += 1 
            return self.isPowerOfThree(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        
        hash_map = [0] * 26 
        hash_map2 = [0] * 26 
        for ch in s:
            index = ord(ch) - 97 
            hash_map[index] += 1 

        for ch in t :
            index = ord(ch) - 97 
            hash_map2[index] += 1 

        if hash_map == hash_map2:
            return True 
        else :
            return False 
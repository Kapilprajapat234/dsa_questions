class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        hash_map1 = {}
        hash_map2 = {}
        for i in range (len(s)):
            if s[i] in hash_map1 and hash_map1[s[i]] != t[i]:
                return False
            else:
                hash_map1[s[i]] = t[i]
        for i in range(len(t)):
            if t[i] in hash_map2 and hash_map2[t[i]] != s[i] :
                return False 
            else:
                hash_map2[t[i]] = s[i]
        return True 
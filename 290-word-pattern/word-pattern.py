class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s):
            return False 
        hash_map1 = {}
        hash_map2 = {}
       
        for i in range (len(pattern)):
            if pattern[i] in hash_map1 and hash_map1[pattern[i]] != s[i]:
                return False
            else:
                hash_map1[pattern[i]] = s[i]
        for i in range(len(s)):
            if s[i] in hash_map2 and hash_map2[s[i]] != pattern[i] :
                return False 
            else:
                hash_map2[s[i]] = pattern[i]
        return True 
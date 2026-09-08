class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for i in range(len(s)) :
            hash_map[s[i]] = hash_map.get(s[i], 0 ) + 1 
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i 
        return -1 
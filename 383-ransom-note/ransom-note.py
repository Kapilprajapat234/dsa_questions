class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_list = [0] * 26
        hash_list2 = [0] * 26 
        for ch in ransomNote:
            index = ord(ch) - 97
            hash_list[index] += 1 
        for ch in magazine:
            index = ord(ch) - 97 
            hash_list2[index] += 1

        
        
        for i in range(26) :
            if hash_list[i] > hash_list2[i]:
                return False 
        return True

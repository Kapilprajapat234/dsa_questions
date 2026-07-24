class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        for i in range(len(s)):
            if i > 0 :

                if s[i]  == 'V' and s[i-1] == 'I':
                    count -= 2 
                elif s[i]  == 'X' and s[i-1] == 'I':
                    count -= 2
                elif s[i]  == 'L' and s[i-1] == 'X':
                    count -= 20
                elif s[i]  == 'C' and s[i-1] == 'X':
                    count -= 20
                elif s[i]  == 'D' and s[i-1] == 'C':
                    count -= 200
                elif s[i]  == 'M' and s[i-1] == 'C':
                    count -= 200
                
            count += roman[s[i]]
        return count 
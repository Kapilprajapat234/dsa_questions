class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0 
        left = 0
        right = k - 1
        window = right - left + 1
        while left <= right :
            if s[left] in 'aeiou':
                count += 1
            left += 1 
        left = 0 
        right = k
        max_count = count 
        while right < len(s):
            if s[left] in 'aeiou':
                count -= 1

            if s[right] in 'aeiou':
                count += 1
            left += 1 
            right += 1 
            max_count = max(max_count , count )
        return max_count 
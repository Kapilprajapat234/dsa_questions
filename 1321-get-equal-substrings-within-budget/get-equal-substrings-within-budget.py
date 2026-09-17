class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        
        arr1 = [ord(ch) for ch in s]
        arr2 = [ord(ch) for ch in t] 
        left = 0
        total = 0
        ans = 0 

        for right in range(len(arr1)):
            total += abs(arr1[right] - arr2[right])

            while total > maxCost:
                total -= abs(arr1[left] - arr2[left])
                left += 1

            ans = max(ans ,right - left +  1 )
        return ans 
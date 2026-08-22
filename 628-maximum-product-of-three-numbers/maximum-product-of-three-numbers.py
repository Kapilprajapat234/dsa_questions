class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest1 = None 
        largest2 = None 
        largest3 = None 
        smallest = None 
        smallest2 = None 

        for n in nums:
        
            if largest1 is None or n > largest1:
                largest3 = largest2
                largest2 = largest1 
                largest1 = n

            elif largest2 is None or n > largest2:
                largest3 = largest2
                largest2 = n

            elif largest3 is None or n > largest3:
                largest3 = n

            if smallest  is None or n < smallest :
                smallest2 = smallest 
                smallest = n 
            elif smallest2 is None or n < smallest2:
                smallest2 = n 
            
        return max(largest1 * largest2 * largest3 , smallest * smallest2 * largest1)

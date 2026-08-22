class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = None 
        second = None 
        third = None 
        smallest = None 
        second_small = None 

        for n in nums:
        
            if largest is None or n > largest:
                third = second
                second = largest 
                largest = n

            elif second is None or n > second:
                third = second
                second = n

            elif third is None or n > third:
                third = n

            if smallest  is None or n < smallest :
                second_small = smallest 
                smallest = n 
            elif second_small is None or n < second_small:
                second_small = n 
            
        return max(largest * second * third , smallest * second_small * largest)

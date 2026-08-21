class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = None 
        second = None 
        third = None 
        for i in nums :
            if first == i or second == i or third == i :
                continue 
            elif first is  None or i  > first  :
                third = second 
                second = first 
                first = i
            elif second is None or i > second :
                third = second 
                second = i 
            elif  third is None or i > third  :
                third = i 
        if third is  None :
            return first 
        return third 
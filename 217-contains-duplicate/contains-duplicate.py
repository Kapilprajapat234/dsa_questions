class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # sets = set( )
        # for num in nums:
           
        #     if num in sets  :
        #         return True 

        #     sets.add(num)
        # return False 
        hash_map = {}
        for i in nums:
            if i in hash_map :

                hash_map[i] += 1 
            else :
                hash_map[i] = 1
        for i in hash_map : 
            if hash_map[i] > 1 :
                return True 
            
        return False  
          


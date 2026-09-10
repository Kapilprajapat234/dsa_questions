class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in range(len(nums) - 1 ):
        #     for j in range(i+ 1 , len(nums)):
        #         if nums[i] == nums[j]:
        #             dis = abs(i - j) 
        #             if dis <= k :
        #                 return True 
        # return False 

        hash_map = {}
        for i in range (len (nums)):
            if nums[i] in hash_map :
                diff = abs(i - hash_map[nums[i]])
                if diff <= k :
                    return True 
            
            hash_map [nums[i]] = i
        return False 
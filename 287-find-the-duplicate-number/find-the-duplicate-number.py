class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sets = set()
        for i in range(len(nums)):
            if nums[i] not in sets :
                sets.add(nums[i])
            elif nums[i] in sets :
                return nums[i]
        return -1 
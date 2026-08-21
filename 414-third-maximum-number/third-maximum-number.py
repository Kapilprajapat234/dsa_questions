class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num = list(set(nums))
        if len(num) < 3 :
            return num[-1]

        num.sort()

        return num[len(num) - 3]
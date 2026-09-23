class Solution(object):
    def findMiddleIndex(self, nums):
        leftsum = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            leftsum.append(total)

        rightsum = []
        total2 = 0

        for i in range(len(nums) - 1, -1, -1):
            total2 += nums[i]
            rightsum.append(total2)

        for i in range(len(nums)):
            left = leftsum[i] - nums[i]
            right = rightsum[len(nums) - 1 - i] - nums[i]

            if left == right:
                return i

        return -1
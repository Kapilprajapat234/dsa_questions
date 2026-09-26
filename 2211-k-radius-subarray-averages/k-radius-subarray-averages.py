class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = list()
        prefix = []
        window = 2*k + 1
        total = 0  
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)

        for i in range(len(prefix)):
            if i - k < 0 or  i + k >= len(prefix) :
                arr.append(-1 )
            else:
                start = i - k
                end = i + k

                if start == 0:
                    total = prefix[end]
                else:
                    total = prefix[end] - prefix[start - 1]

                avg = total // window
                arr.append(avg)
        return arr
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        nums.sort()

        prefix = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)

        answer = []

        for query in queries:
            count = 0

            for i in range(len(prefix)):
                if prefix[i] <= query:
                    count += 1

            answer.append(count)

        return answer
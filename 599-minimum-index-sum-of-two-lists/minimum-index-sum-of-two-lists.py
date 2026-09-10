class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        arr = list()
        min_sum = float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                index_sum = i + j 
                
        
                if index_sum < min_sum:
                    min_sum = index_sum
                    arr = [list1[i]]
                elif index_sum == min_sum :
                    arr.append(list1[i])
                else :
                    continue 
        return arr 
        
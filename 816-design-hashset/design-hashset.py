class MyHashSet(object):

    def __init__(self):
        self.bucket = [[] for _ in range(10)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % 10 
        if key not in self.bucket[index]:
            self.bucket[index].append(key)
        
            
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % 10 
        if key in self.bucket[index]:
            self.bucket[index].remove(key)
        else :
            pass
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = key % 10

        return key in self.bucket[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)





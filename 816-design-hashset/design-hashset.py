class MyHashSet(object):

    def __init__(self):
        self.void = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.void:
            self.void.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.void:
            self.void.remove(key)
        else :
            pass
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.void :
            return True 
        else :
            return False 
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)





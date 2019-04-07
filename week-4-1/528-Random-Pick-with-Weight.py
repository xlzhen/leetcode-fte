from collections import defaultdict
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.lst = []
        
        for index, val in enumerate(w):
            while val > 0:
                self.lst.append(index)
                val -= 1
    
    def pickIndex(self):
        """
        :rtype: int
        """
        i = random.randint(0, len(self.lst)-1)
        return self.lst[i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

------Time Limit Exceeded-----------------------------------------------

class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum_weights = sum(w)
        self.weights = w
        
        for i in range(1, len(w)):
            self.weights[i] += self.weights[i-1]
 

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.sum_weights)
        l, r = 0, len(self.weights) - 1
        while l < r:
            mid = (l + r) // 2
            if rand <= self.weights[mid]:
                r = mid
            else:
                l = mid + 1
        return l 
        
------Binary Search -----------------------------------------------


from collections import defaultdict
from heapq import *

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_ = defaultdict(int)
        for i in s:
            dict_[i] += 1
        heap = []
        for key, val in dict_.iteritems():
            heappush(heap, (val, key))
        output = ""
        while heap:
            temp = heappop(heap)
            output += temp[0]*temp[1]
        return output[::-1]
            
            

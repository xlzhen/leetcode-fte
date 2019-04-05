from collections import defaultdict
from heapq import heappush, heappop


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
    
        heap = []
        for key,value in dic.iteritems():
            heappush(heap, (value, key))
    
        while len(heap) > k:  # pop out lease frequent elements
            heappop(heap)
        
        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res

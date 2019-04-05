from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict_ = defaultdict(int)
        presum = ans = 0
        dict_[0] = 1
        for i in nums:
            presum += i
            ans += dict_[presum - k]
            dict_[presum] += 1
        return ans
            
        
                    
        

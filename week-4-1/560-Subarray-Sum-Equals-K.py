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
            

# DP -  Time Limit Exceeded
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_nums = len(nums)
        dp = [[0 for i in range(len_nums)] for j in range(len_nums)]
    
        count = 0
        
        for i in range(len_nums):
            dp[i][i] = nums[i]
            if dp[i][i] == k:
                count += 1
            
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                dp[i][j] = dp[i][j-1] + nums[j]
                if dp[i][j] == k:
                    count += 1
        
        return count
                    
        
                    
        

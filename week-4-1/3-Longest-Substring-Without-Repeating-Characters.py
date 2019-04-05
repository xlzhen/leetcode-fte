class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_length = 0
        index_dict = {}
        
        for i in range(len(s)):
            if s[i] in index_dict and start <= index_dict[s[i]]:
                start = index_dict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            index_dict[s[i]] = i
        
        return max_length

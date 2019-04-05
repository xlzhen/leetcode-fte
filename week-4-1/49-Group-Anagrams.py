from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = defaultdict(list)
        for s in strs:
            c = [0]*26
            for char in s:
                c[ord(char) - ord('a')] += 1
            anagram[tuple(c)].append(s)
        return anagram.values()
    
# tuple is hashable

        
                
            

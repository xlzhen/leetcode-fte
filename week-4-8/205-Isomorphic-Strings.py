from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_one = defaultdict(list)
        dict_two = defaultdict(list)
        
        for index, val in enumerate(s):
            dict_one[val].append(index)
        for index, val in enumerate(t):
            dict_two[val].append(index)

        return sorted(dict_one.values()) == sorted(dict_two.values())
        

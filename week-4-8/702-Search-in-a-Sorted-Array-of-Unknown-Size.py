class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 2147483647
        
        while left <= right:
            mid=(left+right)//2
            x = reader.get(mid)
            if (x==2147483647) or (x>target):
                right=mid-1 
            elif x<target:
                left=mid+1
            else:
                return mid
        return -1

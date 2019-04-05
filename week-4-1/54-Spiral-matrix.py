class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # matrix mutation
        rtn = []
        while matrix:
            rtn.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    rtn.append(row.pop())
            if matrix:
                rtn.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    rtn.append(row.pop(0))
        return rtn
            
        

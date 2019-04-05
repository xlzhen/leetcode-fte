class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        rtn = [0 for i in range(len(T))]
        for i in range(len(T)):
            count = 1
            for j in range(i+1, len(T)):
                if T[j] > T[i]:
                    rtn[i] = count
                    break
                else:
                    count += 1
        return rtn
# Time Limit Exceed

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        rtn = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > stack[-1][1]:
                index, val = stack.pop()
                rtn[index] = i - index
            stack.append((i, T[i]))
        return rtn
            
            
# USE Stack

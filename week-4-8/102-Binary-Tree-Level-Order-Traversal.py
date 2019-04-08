# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        stack.append([root])
        rtn = []
        while stack:
            temp = []
            next_level = []
            nodes = stack.pop()
            for node in nodes:
                if node:
                    temp.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            if temp:
                rtn.append(temp)
            if next_level:
                stack.append(next_level)
        return rtn
            
                
            
        

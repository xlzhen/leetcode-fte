# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        ans = []
        self.addLevel(ans, 0, root)
        return ans
    
    def addLevel(self, ans, level, root):
        if not root:
            return
        if len(ans) <= level:
            ans.append([root.val])
        elif level%2:
            ans[level].insert(0, root.val)
        else:
            ans[level].extend([root.val])
        self.addLevel(ans, level+1, root.left)
        self.addLevel(ans, level+1, root.right)
        

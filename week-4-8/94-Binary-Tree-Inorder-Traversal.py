# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        def inorder(root):
            if not root:
                return 
            if root.left:
                inorder(root.left)
            path.extend([root.val])
            if root.right:
                inorder(root.right)
        inorder(root)
        return path
        
 # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
 
 

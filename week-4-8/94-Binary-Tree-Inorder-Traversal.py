# iterative

class Solution(object):
    def inorderTraversal(self, root):
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

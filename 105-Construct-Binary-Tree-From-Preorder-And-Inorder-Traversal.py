from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder: 
            return
        rootValue = preorder[0]
        index = inorder.index(rootValue)
        preorder.pop(0)

        root = TreeNode(rootValue)
        # order of the next 2 lines matters
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root
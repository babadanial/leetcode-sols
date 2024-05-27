from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = root.val
        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal answer
            
            if not root:
                return 0
            leftOneWay = max(dfs(root.left), 0)
            rightOneWay = max(dfs(root.right), 0)

            # set answer to be value of max path going through root, both ways
            answer = max(answer, root.val + leftOneWay + rightOneWay)

            # return value of max one-way path involving root
            return root.val + max(leftOneWay, rightOneWay)

        dfs(root)
        return answer
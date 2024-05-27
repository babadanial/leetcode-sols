from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        myMap = {}
        q = deque()
        if root:
            q.append(root)
        
        level = 0
        while len(q) > 0:
            for i in range(len(q)):
                cur = q.popleft()
                myMap[level] = myMap.get(level, []) + [cur.val]
                print(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1
        res = []
        for v in myMap.values():
            res.append(v[-1])

        return res
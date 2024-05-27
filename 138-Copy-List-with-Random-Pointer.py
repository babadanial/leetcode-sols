from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        temp=head
        while temp is not None:
            new=Node(temp.val) 
            new.next=temp.next  
            temp.next=new 
            temp=temp.next.next 
        itr=head
        while itr is not None:
            if itr.random!=None:
                itr.next.random=itr.random.next 
            itr=itr.next.next 
        dummy=Node(0)
        itr=head
        temp=dummy
        while itr is not None:
            fast=itr.next.next 
            temp.next=itr.next  
            itr.next = fast 
            temp=temp.next  
            itr=fast 
      
        return dummy.next
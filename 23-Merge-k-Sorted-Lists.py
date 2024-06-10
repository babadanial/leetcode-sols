# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]):
            if not (list1 or list2):
                return None
            if not list1:
                return list2
            if not list2:
                return list1

            returnList = ListNode()
            current = returnList
            while list1 or list2:
                if not list1 or (list2 and list2.val == min(list1.val, list2.val)):
                    current.next = list2
                    list2 = list2.next
                else:  # list1 exists and list2 either doesn't exist or it is not the min value
                    current.next = list1
                    list1 = list1.next
                current = current.next
            return returnList.next

        while len(lists) > 1:
            list1 = lists.pop(0)
            list2 = lists.pop(0)
            merged = merge2Lists(list1, list2)
            if merged is not None:
                lists.append(merged)

        if len(lists) == 1:
            return lists[0]
        else:  # len(lists) == 0
            return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        p = head
        print(p)

        counter = 0
        while p != None:
            counter = counter + 1
            p = p.next

        print(counter)

        counter = counter // 2
        print(counter)

        p = head

        j = 0
        while j != counter:
            j += 1
            p = p.next

        print(p.val)
        return p






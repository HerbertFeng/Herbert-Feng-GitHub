'''
@Project : Class
@File : 2816. Double a Number Represented as a Linked List (medium).py
@Author : Herbert
@Date : 5/7/2024 10:51 AM
'''
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def doubleIt(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head.val > 4:
        head = ListNode(0, head)
    node = head
    while node:
        node.val = (node.val * 2) % 10
        if node.next and node.next.val > 4:
            node.val += 1
        node = node.next
    return head
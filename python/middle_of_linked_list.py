from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def print_linked_list(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next

# Test the solution
solution = Solution()
input_list = [1, 2, 3, 4, 5]
linked_list = solution.create_linked_list(input_list)
middle_node = solution.middleNode(linked_list)

print("Original linked list:")
solution.print_linked_list(linked_list)
print("Middle node value:", middle_node.val)

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def from(self, arr):
        self.head: Optional[ListNode]

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return True

def test_hasCycle():
    node = ListNode(3)
    print('\n')
    print(node.next)
    print('ola')
    # assert Solution.hasCycle() == False

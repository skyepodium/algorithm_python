# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []

        node = head

        while node:
            result.append(node.val)
            node = node.next

        return result == result[::-1]
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        post_head = ListNode(head.val)
        cp_head = head 
        while cp_head.next != None:
            cur_head = cp_head.next
            new_post_head = ListNode(cur_head.val, post_head)
            post_head = new_post_head
            cp_head = cur_head
            pass 
        
        is_palin = True 
        while post_head.next != None:
            if post_head.next.val != head.next.val: 
                is_palin = False 
                break 
        
            post_head = post_head.next 
            head = head.next
        return is_palin
    
s = Solution()
n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)

n0.next = n1 
n1.next = n2
r = s.reverseList(n0)
print(r)
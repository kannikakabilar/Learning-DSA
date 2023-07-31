# Linked List Questions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Q1 Merge Two Sorted Lists
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()                    # Leabe a pointer to the head of the node
        m = head                             # We will use this variable to traverse through
        while (l1 and l2):                   # As long as long as there are elements in l1 and l2 traverse through
            if l1.val < l2.val:              # if element at l1 is smaller then create a linked node of its value and append it to m
                m.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val <= l1.val:          # if element at l2 is smaller then create a linked node of its value and append it to m
                m.next = ListNode(l2.val)
                l2 = l2.next
            m = m.next
        
        if l1 is not None:                  # if either l1 or l2 has extra elements append them to m
            m.next = l1
        if l2 is not None:
            m.next = l2
        return head.next                    # since first head node is empty, return head.next


# Q2 Remove Duplicates from Sorted Linked List
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example1
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

def deleteDuplicates(head: ListNode) -> ListNode:
    if head is None:                # Handle empty linked list case
        return head
    m = head                        # Leave a pointer to the head
    prev = m.val                    # Keep track of the previous unique value
    temp = m                        # Keep track of the previous unique node
    m = m.next
    while m is not None:            # traverse through m 
        if m.val == prev:           # If value of current node equals the value previous node, 
            temp.next = m.next      # set pointer of previous unique node to the next node of current node
        
        else:                       # If current node is unique, keep traversing
            prev = m.val            # Update value of previous node
            temp = temp.next        # Update previous unique node
        m = m.next
    return head

# Q3 Remove Linked List Elements
"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""


def removeElements(head: ListNode, val: int) -> ListNode:
    if head is None:                               # Handle Empty Linked List case
        return head
    m = head                                       
    while (m is not None) and m.val == val:        # Find first node that does NOT equal val
        m = m.next
    
    head = m                                       # Leave a pointer to the (new) head
    temp = m                                       # Points at last node whose value NOT equal to val
    if m is not None:                              # Skip current node, since it does not equal val
        m = m.next
    while m is not None:                           # Travers through m
        if m.val == val:                           # If value of current node equals
            temp.next = m.next                     # set pointer of previous 'non-val' node to the next node of current node
        
        else:                                      # If current node is unique, keep traversing
            temp = temp.next                       # Update previous 'non-val' node
        m = m.next
    return head

# Q4 Reverse Linked List
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
def reverseList(head: ListNode) -> ListNode:
    if (head is None) or (head.next is None):       # Handle empty linked list and 1-element linked list case
        return head    
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

# Q5 Palindrome Linked List
"""
Given the head of a singly linked list, return true if it is a palindrome.

Example
Input: head = [1,2,2,1]
Output: true
"""

def isPalindrome(head: ListNode) -> bool:
    ## if  list of one element
    if not head.next:
        return True

## find the middle        
#         cnt = 0
#         cur = head
#         while cur:
#             cnt +=1 
#             cur = cur.next        
#         idx = int(cnt/2)

    
# find the middle using two pointers - when fast gets to the end , slow is in the middle
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half of the linked list
    prev = None        
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    
    # check if palindrome:
    left, right = head, prev
    # strat from the beginning and end , and compare each element one step at a time
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True         

# Q6 Delete Node in a Linked List
"""
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling your function.
"""

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    tmp = node                       
    while node.next is not None:
        tmp = node                       # Keep track of previous node
        node.val = node.next.val         # Set the value of the next node to current node (current node value gets deleted)
        node = node.next                 # Keep going until end of linked list has reached
    tmp.next = None                      # To prevent the last node value repeated, delete last node by setting it to none
        
# Q7 Middle of the Linked List
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""

def middleNode(head: ListNode) -> ListNode:
    place = 0
    tmp = head
    while not(tmp is None):      # Calculate the size of the linked list
        place += 1
        tmp = tmp.next
    mid = place // 2             # Find the mid point
    
    #mid += 1
    res = head
    while mid != 0:              # Traverse until mid node is found
        res = res.next
        mid -= 1
    return res

# Q8 Convert Binary Number in a Linked List to Integer
"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""
def getDecimalValue(head: ListNode) -> int:
    
    res = 0                           # Stores the final total value
    place = 0                         # Keep track of the place holder
    if head is None:                  # Handle empty linked list case
        return res
    tmp = head
    while not(tmp is None):           # Calculate the total number of digits
        place += 1
        tmp = tmp.next
    tmp2 = head
    place -= 1                        # Since first digit in binary number is for 2^0
    while not(tmp2 is None):          # Traverse the binary number stored in Linked List
        res += (2**place)*tmp2.val    # Using the place holder value and value provided in linked list, calculate base 10 value
        tmp2 = tmp2.next
        place -= 1
    return res

# 27 problems

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List

"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse 
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. 

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the 
linked list sorted as well. 

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter. 

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


def hasCycle(self, head: Optional[ListNode]) -> bool:
    pass


"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of the 
key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key 
exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this 
operation, evict the least recently used key. The functions get and put must each run in O(1) average time complexity. 

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If 
the two linked lists have no intersection at all, return null. 

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node. listA 
- The first linked list. listB - The second linked list. skipA - The number of nodes to skip ahead in listA (starting 
from the head) to get to the intersected node. skipB - The number of nodes to skip ahead in listB (starting from the 
head) to get to the intersected node. The judge will then create the linked structure based on these inputs and pass 
the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will 
be accepted. 

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 Output: Intersected at '8' 
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the 
head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the 
intersected node in A; There are 3 nodes before the intersected node in B. Example 2: 


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 Output: Intersected at '2' 
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the 
head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected 
node in A; There are 1 node before the intersected node in B. Example 3: 


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 Output: No intersection Explanation: 
From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, 
intersectVal must be 0, while skipA and skipB can be arbitrary values. Explanation: The two lists do not intersect, 
so return null. """


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pass


"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == 
val, and return the new head. 

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
"""


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    pass


"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
"""


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, 
instead you will be given access to the node to be deleted directly. 

It is guaranteed that the node to be deleted is not a tail node in the list.

 

Example 1:


Input: head = [4,5,1,9], node = 5 Output: [4,1,9] Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling your function. Example 2: 


Input: head = [4,5,1,9], node = 1 Output: [4,5,9] Explanation: You are given the third node with value 1, the linked 
list should become 4 -> 5 -> 9 after calling your function. Example 3: 

Input: head = [1,2,3,4], node = 3
Output: [1,2,4]
Example 4:

Input: head = [0,1], node = 0
Output: [1]
Example 5:

Input: head = [-3,5,-99], node = -3
Output: [5,-99]
"""


def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    pass


"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with 
even indices, and return the reordered list. 

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""


def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""You are given the head of a linked list containing unique integer values and an integer array nums that is a 
subset of the linked list values. 

Return the number of connected components in nums where two values are connected if they appear consecutively in the 
linked list. 

 

Example 1:


Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:


Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
"""


def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
    pass


"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k. boolean insertFront() Adds an item at the 
front of Deque. Returns true if the operation is successful, or false otherwise. boolean insertLast() Adds an item at 
the rear of Deque. Returns true if the operation is successful, or false otherwise. boolean deleteFront() Deletes an 
item from the front of Deque. Returns true if the operation is successful, or false otherwise. boolean deleteLast() 
Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise. int 
getFront() Returns the front item from the Deque. Returns -1 if the deque is empty. int getRear() Returns the last 
item from Deque. Returns -1 if the deque is empty. boolean isEmpty() Returns true if the deque is empty, 
or false otherwise. boolean isFull() Returns true if the deque is full, or false otherwise. 
 

Example 1:

Input ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", 
"deleteLast", "insertFront", "getFront"] [[3], [1], [2], [3], [4], [], [], [], [4], []] Output [null, true, true, 
true, false, 2, true, true, true, 4] 

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
"""


class MyCircularDeque:

    def __init__(self, k: int):
        pass

    def insertFront(self, value: int) -> bool:
        pass

    def insertLast(self, value: int) -> bool:
        pass

    def deleteFront(self) -> bool:
        pass

    def deleteLast(self) -> bool:
        pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pass


"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a 
multiple of k then left-out nodes, in the end, should remain as it is. 

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

"""


def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    pass


"""
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the 
first node that is next to it and has a strictly larger value than it. 

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If 
the ith node does not have a next greater node, set answer[i] = 0. 



Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
"""


def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    pass

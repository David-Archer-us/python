# Merge two sorted linked lists and return it 
# as a new sorted list. 
# The new list should be made by 
# splicing together the nodes of the first two lists.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # while loop
        head = ListNode()
        nextNode = head
        l1temp = l1
        l2temp = l2
        while True:
            if l1temp == None:
                nextNode.next = l2temp
                break
            elif l2temp == None:
                nextNode.next = l1temp
                break
            else:
                if l1temp.val < l2temp.val:
                    nextNode.next = l1temp
                    l1temp = l1temp.next
                else:
                    nextNode.next = l2temp
                    l2temp = l2temp.next
                nextNode = nextNode.next
        return head.next

        # # recursive
        # if not l1: return l2
        # if not l2: return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2


instance = Solution()
input1, input2 = ListNode(1), ListNode(1)
newNode1, newNode2 = ListNode(2), ListNode(3)
input1.next = newNode1
input2.next = newNode2
newNode3, newNode4 = ListNode(4), ListNode(4)
newNode1.next = newNode3
newNode2.next = newNode4
result = instance.mergeTwoLists(input1, input2)

while(result):
    print(result.val)
    result = result.next
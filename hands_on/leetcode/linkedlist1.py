# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=0
        num2=0
        i=0
        
        node = l1

        while node:
            num1 += node.val*(10**i)
            node = node.next
            i+=1

        node = l2
        i=0     
        
        while node:
            num2 += node.val*(10**i)
            node = node.next
            i+=1
        
        total = sum([num1,num2])
        print(total)
        
        
        node = ListNode(0)
        
        while total>0:
            rem = total%10
            print(rem)
            total = total//10
            if node.val>0:
                curr_node = node
                while curr_node.next:
                    curr_node = curr_node.next
                curr_node.next=ListNode(val=rem)
            elif rem>0 and not node.next:
                node.val = rem
        return node
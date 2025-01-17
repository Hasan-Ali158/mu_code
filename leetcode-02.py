class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        tail = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            _sum = digit1 + digit2 + carry
            digit = _sum % 10
            carry = _sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return head.next

def main():
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(5)
    l2.next = ListNode(7)
    l2.next.next = ListNode(6)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    while result is not None:
        print(result.val, end=" ")
        result = result.next

main()

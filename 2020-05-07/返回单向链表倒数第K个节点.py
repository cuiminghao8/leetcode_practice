# Definition for singly-linked list.
import time
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head, k):
        """暴力递归法"""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[len(result) - k]

    def kthToLast2(self, head, k):
        """快慢指针
        快慢指针可以解决链表是否成环的问题，如果fast指针追上了slow指针，那么就可以判断链表成环
        这题先把fast移动k-1次，到达k处节点
        此时再同时移动fs和sl
        当fs == 空时
        sl的位置就是m-k+1，即是倒数第k个节点的位置
        """
        fast = head
        slow = head
        """
        f s 
        | |
        [1]--->[2]--->[3]--->[4]--->[5]---[6]
        """
        while k > 0:
            fast = fast.next
            k -= 1
        """
          s<----k----->f
          |            |  先将快指针移动k，这时候快慢指针之间间距就是k
        [1]--->[2]--->[3]--->[4]--->[5]---[6]       
        """
        while fast != None:
            fast = fast.next
            slow = slow.next
        """
                              s<----k----->f
            >>>>>>>>>>>>>>>   |            |   快慢指针同时移动，当快指针==空时，慢指针就是倒数第k个节点位置
        [1]--->[2]--->[3]--->[4]--->[5]---[6]       
        """
        return slow.val


def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    result = Solution()
    k = 2
    begin=time.perf_counter()
    print(result.kthToLast(node1, k))
    end = time.perf_counter()
    print(end-begin)
    begin = time.perf_counter()
    print(result.kthToLast2(node1, k))
    end = time.perf_counter()
    print(end - begin)

if __name__ == "__main__":
    main()

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(list1, list2):

        def _read_ll(ll):
            collected = []

            if ll is None:
                return []

            while ll is not None:
                collected.append(ll.val)
                ll = ll.next

            print(collected)
            return collected

        def _populate_ll(data):
            new_list_head = ListNode()
            for i, v in enumerate(data):
                if i == 0:
                    new_list_head.val = v
                    new_list = ListNode()
                    new_list_head.next = new_list
                    continue
                if i + 1 == len(data):
                    new_list.val = v
                    new_list.next = None
                else:
                    new_list.val = v
                    new_list.next = ListNode()
                    new_list = new_list.next

            return new_list_head

        l1 = _read_ll(list1)
        l2 = _read_ll(list2)
        combined = l1 + l2
        sorted_combined = sorted(combined)
        return _populate_ll(sorted_combined)

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 2
l1.next.next = ListNode()
l1.next.next.val = 4

l2 = ListNode()
l2.val = 1
l2.next = ListNode()
l2.next.val = 3
l2.next.next = ListNode()
l2.next.next.val = 4

r = Solution.mergeTwoLists(l1, l2)

print("Result ll:")
while r is not None:
    print(r.val)
    r = r.next

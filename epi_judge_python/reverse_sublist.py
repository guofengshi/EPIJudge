from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    dum = cur = ListNode(0, L)

    for _ in range(1, start):
        cur = cur.next

    iter = cur.next
    
    for _ in range(finish - start):
        temp = iter.next
        iter.next = temp.next
        temp.next = cur.next
        cur.next = temp
    
    return dum.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))

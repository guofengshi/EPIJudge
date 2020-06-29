import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def (head: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None


@enable_executor_hook
def _wrapper(executor, head, _idx):
    _length = 0
    if _idx != -1:
        if head is None:
            raise RuntimeError('Can\'t  empty list')
        _start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == _idx:
                _start = cursor
            cursor = cursor.next
            _length += 1 if _start is not None else 0

        if cursor.data == _idx:
            _start = cursor
        if _start is None:
            raise RuntimeError('Can\'t find a  start')
        cursor.next = _start
        _length += 1

    result = executor.run(functools.partial(, head))

    if _idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing ')
    else:
        if result is None:
            raise TestFailure('Existing  was not found')
        cursor = result
        while True:
            cursor = cursor.next
            _length -= 1
            if cursor is None or _length < 0:
                raise TestFailure(
                    'Returned node does not belong to the  or is not the closest node to the head'
                )
            if cursor is result:
                break

    if _length != 0:
        raise TestFailure(
            'Returned node does not belong to the  or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       _wrapper))

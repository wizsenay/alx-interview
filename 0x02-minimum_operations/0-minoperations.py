#!/usr/bin/python3
"""
Calculate the minimum number of operations required
... to achieve exactly n 'H' characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required
    ... to achieve exactly n 'H' characters.

    The operations are:
    1. Copy All
    2. Paste

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0
    
    num_of_h = 1
    count_opration = 0
    paste_num = 0

    while num_of_h != n:
        if n % num_of_h == 0:
            count_opration += 2
            paste_num = num_of_h
            num_of_h += num_of_h
        else:
            count_opration += 1
            num_of_h += paste_num
    return count_opration

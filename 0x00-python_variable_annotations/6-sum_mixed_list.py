#!/usr/bin/env python3
'''task 6's module
'''

from typing import list, union

def sum_mixed_list(mxd_lst: list[union[int, float]]) -> float:
    '''gives the sum of float and int in a list
    '''
    return float(sum(mxd_lst))

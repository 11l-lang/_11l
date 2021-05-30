Char = str
Byte = int
Int64 = int
UInt64 = int
UInt32 = int
BigInt = int

def move(obj):
    return obj

from copy import copy, deepcopy

from typing import List, Tuple, NamedTuple, Dict, DefaultDict, Callable, Set, Optional, IO
from enum import IntEnum

import collections # for `defaultdict` and `deque`


# [https://stackoverflow.com/questions/4223349/python-implementation-for-next-permutation-in-stl <- google:‘next_permutation python’]
def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        a.reverse()
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True

# [https://stackoverflow.com/a/41278973/2692494 <- google:‘is_sorted python’]
def is_sorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

# [https://www.rosettacode.org/wiki/Suffixation_of_decimal_numbers#Python]
def format_float(x, precision):
    return f'{x:.{precision}f}'

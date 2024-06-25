Char = str
Byte = int
Int8 = int
Int16 = int
Int32 = int
Int64 = int
UInt16 = int
UInt32 = int
UInt64 = int
BigInt = int
Size   = int
USize  = int

def move(obj):
    return obj

def ref(obj):
    return obj

from copy import copy, deepcopy

from typing import List, Tuple, NamedTuple, Dict, DefaultDict, Callable, Set, Optional, IO, TextIO, BinaryIO
TextOutput = TextIO
BinaryOutput = BinaryIO
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

def format_float_exp(x, precision, width = 0):
    return f'{x:{width}.{precision}e}'

# For [https://www.rosettacode.org/wiki/Peaceful_chess_queen_armies#D]
# class IVec2

#def set_str_char(s, char_index, char)

# For [https://www.rosettacode.org/wiki/Range_modifications#Python]
# def set_tuple_element(t, element_index, element_value):
#     l = list(t)
#     l[element_index] = element_value
#     return tuple(l)

# def add_to_tuple_element(t, element_index, addendum):
#     l = list(t)
#     l[element_index] += addendum
#     return tuple(l)

class MutTupleClass: # [-FIX mypy error: Invalid type "1.MutTuple"-]
    def __getitem__(self, params):
        return list
    def __call__(self, *elems):
        return list(elems)
MutTuple = MutTupleClass()


def hexu(n):
    return hex(n)[2:].upper()

def wrap(x, min_val, max_val):
    return (x - min_val) % (max_val - min_val) + min_val

# [https://www.rosettacode.org/wiki/First_perfect_square_in_base_n_with_n_unique_digits#D]
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def int_to_str_with_radix(num, base):
    assert(base >= 2 and base <= 36)
    cnum = abs(num)
    result = ''
    while True:
        result += ALPHABET[cnum % base]
        cnum //= base
        if cnum == 0: break
    if num < 0:
        result += '-'
    return result[::-1]

# [https://www.rosettacode.org/wiki/MD5/Implementation#Python]
def rotl32(x, amount):
    x &= 0xFFFFFFFF
    return ((x<<amount) | (x>>(32-amount))) & 0xFFFFFFFF

def rotr32(x, amount):
    x &= 0xFFFFFFFF
    return ((x>>amount) | (x<<(32-amount))) & 0xFFFFFFFF

def popcount(x):
    return bin(x).count('1')

def Bytes(s): # if you need `b"\xAE"`, please note that `Bytes("\xAE")` will not work, use `[Byte(0xAE)]` or `bytes(b"\xAE")` instead
    return bytes(s, 'ascii')

# [https://en.wikipedia.org/wiki/Product_(mathematics)#Product_of_a_sequence]
def product_of_a_seq(seq):
    r = 1
    for v in seq:
        r *= v
    return r

def nidiv(a, b):
    return a // b

def nmod(a, b):
    return a % b

try:
    import colorama
    colorama.init()

    term_colors = {
        ''      : colorama.Style.RESET_ALL,
        'red'   : colorama.Fore.LIGHTRED_EX,
        'green' : colorama.Fore.LIGHTGREEN_EX,
        'blue'  : colorama.Fore.LIGHTBLUE_EX,
        'gray'  : colorama.Style.DIM,
    }

    def term_color(color = ''):
        print(term_colors[color], end = '')

except ImportError:
    def term_color(color = ''):
        pass

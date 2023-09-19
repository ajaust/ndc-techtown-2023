from typing import Iterable, Tuple

# Your task is to implement the functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_packing.py -x -v


def remove_first_and_last_items_using_unpacking(iterable):
    _, *iterable, _ = iterable
    return iterable

def swap_the_third_and_fifth_item(iterable):
    first, second, third, fourth, fifth, *remaining = iterable
    return first, second, fifth, fourth, third, *remaining

def join_two_lists_using_packing(iterable1, iterable2):
    return [*iterable1, *iterable2]

def double_first_and_halve_second(iterable: Iterable[Tuple[int, int]]):
    return [(f*2, s/2) for (f, s) in iterable]

def unpack_the_third_item_in_the_second_item(iterable: Iterable[Iterable]):
    f, [fi, si, ti, *irest], *rest = iterable
    return ti

# please do not use list() or tuple()
def make_list_from_generator_using_unpacking(generator):
    return [*generator]

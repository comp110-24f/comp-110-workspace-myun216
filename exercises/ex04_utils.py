"""Ex04: List Utility Functions."""

__author__ = "730462791"


def all(a: list[int], target: int) -> bool:
    # checks each element matches the target number given
    for elem in a:
        if elem != target:
            return False  # returns false if not all elements match target
    else:
        return True  # returns True if all elements match target


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = 0  # to set as the max number
    for elem in input:  # to loop through every element
        while elem > max_num:  # compare if element is greater than max number
            elem = max_num  # if it is, set that equal to max number
            return max_num  # return max number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]):
    for elem in list2:  # loop through each item in list
        list1.append(elem)  # add items in second list to first list

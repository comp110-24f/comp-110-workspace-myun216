"""Ex04: List Utility Functions."""

__author__ = "730462791"


def all(a: list[int], target: int) -> bool:
    # checks each element matches the target number given
    if len(a) == 0:
        return False
    for elem in a:
        if elem != target:
            return False  # returns false if not all elements match target
    return True  # returns True if all elements match target


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = input[0]  # to set as the max number
    for elem in input:  # to loop through every element
        if elem > max_num:  # compare if element is greater than max number
            max_num = elem  # if it is, set that equal to max number
    return max_num  # return max number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:  # loop through each item in list
        list1.append(elem)  # add items in second list to first list

"While Loops Challenge Questions"

__author__ = "730462791"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    idx: int = 0
    while idx < len(phrase):
        if phrase[idx] == search_char:
            count = count + 1
        idx = idx + 1
    return count

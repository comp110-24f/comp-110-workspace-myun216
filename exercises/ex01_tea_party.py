"""This program will help you plan a cozy tea party."""

__author__ = "730462791"


def main_planner(guests: int) -> None:
    """This function sums the costs for a tea party for a number of guests."""
    print(
        " A cozy tea party for " + str(guests) + " people!"
    )  # must convert number of guests into a string
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests)))
    )  # must fill value for both parameters of cost. variables=tea/treat count
    return None  # no return, just printing plan


def tea_bags(people: int) -> int:
    """This computes the number of tea bags based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """This gives # of treats based on the # of teas"""
    return round(
        tea_bags(people=people) * 1.5
    )  # needed to convert number of treats into integer-> round up


def cost(tea_count: int, treat_count: int) -> float:
    """This computes the cost of tea and treats combined."""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # multiply cost by number of tea and treats


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # place at end of code because python reads from top down

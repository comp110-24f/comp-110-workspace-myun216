"""Challenge question 00: functions"""

__author__ = "730462791"


def mimic(message: str) -> str:
    """This function will take yout input and repeat it back to you."""
    return message


def main() -> None:
    """This will print the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()

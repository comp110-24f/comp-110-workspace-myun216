"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("Thats a small number")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


less_than_10(num=5)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Comp 110!"
    else:
        return "Keep sleeping, you deserve it. :)"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="fox", letter="z"))


def get_weather_report() -> str:
    """Docstring"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()

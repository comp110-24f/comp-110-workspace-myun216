"""The classic game of Wordle!"""

__author__ = "730462791"


def input_guess(secret_word_len: int) -> str:
    """Takes guess and compares to correct length, prompting user to provide a guess
    until length is correct"""
    guess: str = input(f"Enter a {secret_word_len} character word:")
    while len(guess) != secret_word_len:
        guess = str(
            input(f"That wasn't {secret_word_len} chars! Try again: ")
        )  # need to return an input and run through while loop again
    return guess


def contains_char(word: str, char: str) -> bool:
    "This will check if a specific char string matches any in the secret word"
    assert len(char) == 1
    word_idx: int = 0  # to check each index of the word
    while word_idx < len(word):
        if word[word_idx] == char:  # check if char matches each index of word
            return True
        word_idx += 1
    return False


def emojified(secret: str, guess: str) -> str:
    "Comparing 2 strings of equal length, returning an emoji box if correct chars"
    assert len(secret) == len(guess)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    idx: int = 0
    box: str = ""  # need to define the returned output, empty string to start with
    while idx < len(secret):
        if secret[idx] == guess[idx]:  # if letters match at right spots
            box += green_box  # concatenating an emoji into an empty string
        elif (
            contains_char(secret, guess[idx]) is True
        ):  # using contains_char for second scenario
            box += yellow_box
        else:
            # if guess chars doesn't match secret word chars and neither scenarios met
            box += white_box
        idx += 1
    return box


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    turns: int = 1
    while turns < 7:  # making sure game only runs 6 turns
        print(
            f"=== Turn {turns}/6 ==="
        )  # tells player what turn they're on before they start
        guess: str = input_guess(len(secret))
        # use to make sure character enters 6 letter word, shows initial input message
        print(emojified(guess, secret))
        if guess == secret:  # user won in this scenario
            return print(f"You won in {turns}/6 turns!")
        if turns == 6:  # if turns becomes 6 and user did not get secret word
            print("X/6 - Sorry, try again tomorrow!")
        turns += 1


if __name__ == "__main__":
    main(secret="codes")

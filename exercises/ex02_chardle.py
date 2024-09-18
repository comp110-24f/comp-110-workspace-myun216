"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730462791"


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # pulling previous step functions into this function


def input_word() -> str:
    word: str = str(input("Enter a 5-character word: "))
    if len(word) != 5:  # using "!=" simplifies from using "<" & ">" as 2 lines
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    letter: str = str(input("Enter a single character: "))
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    word = word  # assigning parameter "word" to local variable also called "word"
    letter = letter
    count: int = 0  # using index which starts at 0

    print("Searching for " + str(letter) + " in " + str(word))
    if letter == word[0]:  # check for each index
        print(str(letter) + " found at index 0")
        count = count + 1  # adds 1 every time contains_char is found
    if letter == word[1]:
        print(
            str(letter) + " found at index 1"
        )  # use a separate if statement incase of multiple matching letters
        count = count + 1
    if letter == word[2]:
        print(str(letter) + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(str(letter) + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(str(letter) + " found at index 4")
        count = count + 1
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    if count == 1:
        print(
            str(count) + " instance of " + letter + " found in " + word
        )  # need different output if only 1 match
    if count < 1:
        print(
            "No instances of " + letter + " found in " + word
        )  # need different output if no matches found


if __name__ == "__main__":
    main()

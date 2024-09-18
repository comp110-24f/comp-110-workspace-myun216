"""Challenge question 02: conditionals"""

__author__ = "730462791"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(
        input("Guess a number: ")
    )  # Putting this line after guess is defined but before conditional statements
    print("Your guess was " + str(guess))
    if guess == secret:  # secret is the number you're comparing the input x to.
        print("You got it!")
    elif guess > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        if guess < secret:
            print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()

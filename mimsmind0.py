# Imports
import sys
import random


# Body
def get_length():
    """argv to get length
    default to 1"""
    length = 1
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except:
            print("Invalid Input")
    return length


def generate_random_number(length):
    """gen random number by length"""
    start = 10**(length - 1)
    end = 10**length - 1
    return random.randint(start, end)


def game_flow(length, random_num, tries=1, feedback=""):
    # prompt user for guess (inform them how many)
    if tries == 1:
        print("Let's play the mimsmind0 game.")
        msg = "Guess a {}-digit number: ".format(length)
    else:
        msg = feedback
    guess = input(msg)
    guess = validate_input(guess)
    feedback = determine_feedback(guess, random_num, tries)
    game_flow(length, random_num, tries+1, feedback)


def validate_input(guess):
    while True:
        try:
            guess = int(guess)
        except:
            guess = input("Not a valid input. Try again: ")
        else:
            return guess


def determine_feedback(guess, random_num, tries):
    if guess == random_num:
        print("Congratulations. You guessed the correct number in {} tries.".
              format(tries))
        quit()
    elif guess > random_num:
        feedback = "Try again. Guess a lower number: "
    else:
        feedback = "Try again. Guess a higher number: "
    return feedback


def main():
    length = get_length()
    random_num = generate_random_number(length)
    # print(get_length())
    # print(generate_random_number(1))
    # print(generate_random_number(2))
    # print(generate_random_number(3))
    # print(validate_input("1"))
    # print(validate_input("one"))
    # print(determine_feedback(1, 2, 3))
    # print(determine_feedback(1, 0, 3))
    # print(determine_feedback(1, 1, 3))
    game_flow(length, random_num)

if __name__ == "__main__":
    main()

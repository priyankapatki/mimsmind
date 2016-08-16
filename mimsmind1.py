#!/usr/bin/env python
# mimsmind1.py
# Sample Exam #2
# https://www.ischool.berkeley.edu/intranet/students/newstudents/info206/
###############################################################################
# Import
import sys
import random


# Body
def get_length():
    if len(sys.argv) == 2:
        length = sys.argv[1]
    else:
        length = "3"
    return length  # This is a string.


def get_random(length):
    rand_num = ""
    for n in range(int(length)):
        rand_num += str(random.randint(0, 9))
    return rand_num  # This is a string.


def get_maxrounds(length):
    length = int(length)
    return (2**length) + length


def get_initial_guess(length):
    guess = input('\nGuess a {0}-digit number: '.format(length))
    guess_count = 0
    return guess, guess_count


def validate_guess(guess, rand_num):
    while True:
        try:
            int(guess)
            if not len(guess) == len(rand_num):
                raise ValueError
        except Exception:
            guess = input("Invalid input. Try again: ")
            continue
        return guess


def provide_feedback(guess, rand_num, guess_count, maxrounds):
    while guess_count < maxrounds:
        guess = validate_guess(guess, rand_num)

        guess_count += 1  # Increment for valid guess

        if guess == rand_num:
            print("Congratulations. "
                  "You guessed the correct number in {0} tries."
                  .format(guess_count))
            return

        bulls, cows = get_bullcow(guess, rand_num)

        guess = input("{0} bull(s), {1} cow(s). Try again: "
                          .format(bulls, cows))
    # If maxrounds reached.
    print("Sorry. You did not guess the number in {0} tries. "
          "The correct number is {1}.".format(maxrounds, rand_num))


def get_bullcow(guess, rand_num):
    # Turn to lists to enable mutation.
    guess_list = list(guess)
    rand_num_list = list(rand_num)
    bulls = 0
    cows = 0
    # One bull loop per digit. If perfect match, replace digits.
    # Digits must be replaced w/ different chars to avoid match in cow loop
    # 32 for 23
    idx = 0
    while idx < len(guess_list):
        if guess_list[idx] == rand_num_list[idx]:
            bulls += 1
            rand_num_list[idx] = " "
            guess_list[idx] = "_"
        idx += 1
    # One cow loop per remaining digit. If in, replace.
    idx = 0
    while idx < len(guess_list):
        if guess_list[idx] in rand_num_list:
            cows += 1
            rand_num_list[rand_num_list.index(guess_list[idx])] = " "
            guess_list[idx] = "_"
        idx += 1
    return bulls, cows

###############################################################################
# Testing:


def testing():
    print(get_random(1), "one-digit")
    print(get_random(2), "two-digits")
    print(get_random(3), "three-digits")
    print()

    # Borrowed from Example 1
    for each in ["789", "891", "189", "135", "111", "132", "125"]:
        print("Guess:", each)
        print("{0} bull(s), {1} cow(s)".format(*get_bullcow(each, "123")))
    print()

    # Borrowed from Example 2
    for each in ["012", "010", "100", "700"]:
        print("Guess:", each)
        print("{0} bull(s), {1} cow(s)".format(*get_bullcow(each, "007")))
    print()

    # Extra test case #1
    for each in ["111", "222", "333"]:
        print("Guess:", each)
        print("{0} bull(s), {1} cow(s)".format(*get_bullcow(each, "123")))
    print()

    # Extra test case #2
    for each in ["011"]:
        print("Guess:", each)
        print("{0} bull(s), {1} cow(s)".format(*get_bullcow(each, "123")))
    print()

###############################################################################


def main():
    print("Let's play the mimsmind1 game.")
    # testing()

    length = get_length()
    rand_num = get_random(length)
    maxrounds = get_maxrounds(length)
    guess, guess_count = get_initial_guess(length)
    provide_feedback(guess, rand_num, guess_count, maxrounds)

if __name__ == "__main__":
    main()

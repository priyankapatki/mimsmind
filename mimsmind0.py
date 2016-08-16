#!/usr/bin/env python3
# mimsmind0.py
# Sample Exam #1
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
        length = 1
    return length


# Two get_random functions are presented for teaching purposes.
# Comment out the second to test the first (the second overwrites the first).
# get_random with exponentiation
def get_random(length):
    length = int(length)
    upper = (10**length) - 1
    lower = (10**(length-1))
    if length == 1:
        lower = 0
    rand_num = random.randint(lower, upper)
    return rand_num


# get_random with strings and for loop
def get_random(length):
    rand_num = ""
    for n in range(int(length)):
        rand_num += str(random.randint(0, 9))
    return int(rand_num)


def get_initial_guess(length):
    guess = input('\nGuess a {0}-digit number: '.format(length))
    guess_count = 1
    return guess, guess_count


# Two provide_feedback functions are presented for teaching purposes.
# Comment out the second to test the first (the second overwrites the first).
# provide_feedback with recursion
def provide_feedback(guess, rand_num, guess_count):
    guess = int(guess)
    if guess == rand_num:
        print("\nCongratulations. You guessed the correct number in {0} tries."
              .format(guess_count))
        return
    elif guess < rand_num:
        guess = input("\nTry again. Guess a higher number: ")
    else:
        guess = input("\nTry again. Guess a lower number: ")
    guess_count += 1
    provide_feedback(guess, rand_num, guess_count)


# provide_feedback with while
def provide_feedback(guess, rand_num, guess_count):
    while True:
        guess = int(guess)
        if guess == rand_num:
            print("\nCongratulations. "
                  "You guessed the correct number in {0} tries."
                  .format(guess_count))
            return
        elif guess < rand_num:
            guess = input("\nTry again. Guess a higher number: ")
        else:
            guess = input("\nTry again. Guess a lower number: ")
        guess_count += 1

###############################################################################
# Testing: (uncomment to test)


def testing():
    print(get_random(1), "one-digit")
    print(get_random(2), "two-digits")
    print(get_random(3), "three-digits")

    test_input = (5, 4, 1)
    print('provided guess = {}, rand_num = {}, count = {}'
          .format(*test_input))
    provide_feedback(*test_input)

###############################################################################


def main():
    print("Let's play the mimsmind0 game.")
    # testing()

    length = get_length()
    rand_num = get_random(length)
    guess, guess_count = get_initial_guess(length)
    provide_feedback(guess, rand_num, guess_count)

if __name__ == "__main__":
    main()

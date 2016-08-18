#!/usr/bin/env python3
# Imports
import sys
import random

# Body

def random_int():
    if len(sys.argv) > 1:
        try:
            sys_arg = int(sys.argv[1])
        except:
            print("\nSince argument invalid, default length = 1")
            sys_arg = 1
    else:
        sys_arg = 1

    start = 10**(sys_arg - 1) 
    end = 10**(sys_arg) - 1
    rand_int = random.randint(start, end)
    # print("r ={}".format(rand_int))
    # print("s ={}".format(start))
    # print("e ={}".format(end))
    # print("sys ={}".format(sys_arg))

    return (rand_int, sys_arg)

def try_num(lowhigh, guess_count):
    user_guess = ''
    guess_num = guess_count
    while user_guess == '':
        try:
            user_guess = int(input("\nTry again. Guess a {} number: ".
                format(lowhigh)))
        except:
            print("\nNot a valid integer.")
            guess_num += 1
    else:
        guess_num += 1
    return (user_guess, guess_num)



def mimsmind0():

    rand_int, dig_len = random_int()
    # print("sys ={}, rand = {}".format(dig_len, repr(rand_int)))
    user_input = ''
    guess_num = 1
    while user_input == '':
        try:
            user_input = int(input("\nGuess a {}-digit number: ".format(dig_len)))

        except:
            print("\n Not a valid integer.")
            guess_num += 1

    while user_input != rand_int:
        if user_input < rand_int:
            (user_input, guess_num) = try_num('higher', guess_num)

        elif user_input > rand_int:
            (user_input, guess_num) = try_num('lower', guess_num)
    else:
        print("\nCongratulations. You guessed the correct number in {} tries.\n"
            .format(guess_num))


def main():
    # print(sys.argv,type(sys.argv))
    # print(len(sys.argv))
    print("\nLet's play the mimsmind0 game.")
    mimsmind0()


if __name__ == '__main__':
    main()
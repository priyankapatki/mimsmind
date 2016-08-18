#!/usr/bin/env python3
import random
import sys

def random_int():
    if len(sys.argv) > 1:
        try:
            no_digits = int(sys.argv[1])
        except:
            print("\nSince argument invalid, default length = 3")
            no_digits = 3
    else:
        no_digits = 3

    # Generating a random integer
    start = 0 
    end = 10**(no_digits) - 1
    rand_int = random.randint(0, end)
    ran_len = len(str(rand_int))

    # Adds leading zeroes to the random integer if required.
    if ran_len != no_digits:
        new_rand_str = str(rand_int).zfill(no_digits)
    else:
        new_rand_str = str(rand_int)

    # Calculating max number of tries
    no_of_tries = 2 ** no_digits + no_digits
    return (new_rand_str, no_digits, no_of_tries)


def try_again(line, num_digits):
    ''' This function provides the user input prompt. If the user input is invalid ,
    The prompt will continue to provide invalid prompt, until valid value is entered
    by user '''
    user_guess = ''
    while user_guess == '':
        user_str = str(input(line))
        if len(user_str) == num_digits: # eg 003 == 003
            try:
                user_guess = str(int(user_str))
            except:
                user_guess = str(try_again('\nInvalid input. Try again:',
                num_digits))
                return user_guess
            else:
                return user_guess
        else:
            # eg: 03 != 003
            user_guess = str(try_again('\nInvalid input. Try again: ',
                num_digits))
            return user_guess


def count_dict(num_str):
    """This function will store the number of times each digit
     appears in the number """
    # unique_num : is a list of distinct digits that appear in the num_str
    unique_num = list(set(list(num_str)))
    cnt_dict = {}

    for c_key in unique_num:
        cnt_dict[c_key] = num_str.count(c_key)

    return cnt_dict

def cows(rand_str, user_str):
    # Checks if each digit in user input is present in random number or not
    # If present, the function will not count a number twice.
    # note: It also includes bull values, which will be removed later.
    rand_dict = count_dict(rand_str)
    user_dict = count_dict(user_str)
    cow = 0

    for u_key in user_dict:
        if u_key in rand_dict:
            temp_cow = min(user_dict[u_key], rand_dict[u_key]) #to prevent from counting digits that repeat twice.
            cow += temp_cow

    return cow

def bull(rand_str, user_str):
    # Calculates bull values
    bull = 0
    limit = len(rand_str)

    for i in range(0, limit):
        if rand_str[i] == user_str[i]:
            bull += 1
    return bull

def bulls_cows(user_input, random_no_str):

    # guess_len = len(str(user_input))
    guess_str = str(user_input)
    no_of_bulls = bull(random_no_str, guess_str)
    no_of_cows = cows(random_no_str, guess_str)
    # removes bull values which are counted twice to calculate
    #final number of cows
    
    total_cows = no_of_cows - no_of_bulls

    return (no_of_bulls, total_cows)

def mimsmind1():
    (random_no, num_digits, max_guesses) = random_int()
    # print(random_no)
    print("\nLet's play the mimsmind1 game. You have {} guesses".
        format(max_guesses))
    user_input = ''
    guess_num = 1
    user_input = str(try_again("\nGuess a {}-digit number: ".format(num_digits), num_digits ))
    user_input = user_input.zfill(num_digits)  # add leading 0's

    while (user_input != random_no) and (guess_num < max_guesses):
        # retrieving bulls and cows
        (bulls, cows) = bulls_cows(user_input, random_no)
        user_input = str(try_again("\n{} bull(s), {} cow(s). Try again: ".
            format(bulls, repr(cows)), num_digits))
        # adding leading 0s
        user_input = user_input.zfill(num_digits)
        guess_num += 1

    else:
        if user_input == random_no:
            print("\nCongratulations. You guessed the correct number in {} tries.\n"
                .format(guess_num))
        elif guess_num >= max_guesses:
            print("\nSorry. You did not guess the number in {} tries. The correct number is {}\n".
                format(max_guesses, repr(random_no)))


def main():
    
    mimsmind1()

if __name__ == '__main__':
    main()

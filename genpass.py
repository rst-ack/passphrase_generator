#!/usr/bin/env python

import argparse
import os
import secrets

def parse_args():
    parser = argparse.ArgumentParser("Secure passphrase generator")
    parser.add_argument(
        "-w",
        "--wordlist",
        type=str,
        dest="wordlist_path",
        default="./wordlists/words.txt",
        help="Specify a path to a wordlist"
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        dest="num_passwds",
        default=1,
        help="Specify the number of passphrases to generate"
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        dest="passwd_size",
        default=4,
        help="Specify the length (in words) of the generated passphrase(s)"
    )
    parser.add_argument(
        "--spaces",
        action="store_true",
        dest="use_spaces",
        default=False,
        help="Use this to generate a passphrase with spaces between each word"
    )

    args = parser.parse_args()

    # We only want to accept valid file paths
    if not os.path.isfile(args.wordlist_path):
        raise OSError("Specified path to wordlist is either invalid or does not exist. Exiting...")
        exit(1)
    else:
        return args

def gen_pass(length, use_spaces, wordlist):
    """Generate a secure passphrase

    Params:
    - length (int)
        The length of the password to generate (in number of words)
    - use_spaces (bool)
        Generate passphrase with or without spaces
    - wordlist (list)
        A list of individual words

    Returns:
    - string
    """
    phrase = ""
    last_word = False
    for i in range (0, length -1):
        if i == length - 1:
            last_word = True
        index = secrets.randbelow(len(wordlist) - 1)
        phrase += wordlist[index]
        if not last_word and use_spaces:
            phrase += " "

    return phrase

if __name__ == "__main__":

    args = parse_args()

    wordlist = []
    with open(args.wordlist_path, "r") as wordlist_file:
        wordlist_raw = wordlist_file.readlines()
        for word in wordlist_raw:
            wordlist.append(word.rstrip())

    for i in range (0, args.num_passwds):
        print(gen_pass(args.passwd_size, args.use_spaces, wordlist))


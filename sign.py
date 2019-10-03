#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# this program checks the sign of an integer


import random


def main():
    # this function checks the sign of an integer

    # input
    print("Let me check the sign of your integer.")
    num = int(input("Enter your integer: "))

    # process
    if num > 0:
        # output
        print("")
        print("The sign of this integer is positive.")
    elif num < 0:
        print("")
        print("The sign of this integer is negative.")
    else:
        print("")
        print("0")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program checks the sign of an integer


def main():
    # this function checks the sign of an integer

    # input
    print("Let me check the sign of your integer.")
    num = int(input("Enter your integer: "))

    # process
    if num > 0:
        # output
        print("")
        print("The sign of this integer is positive (+).")
        # output
    elif num < 0:
        # output
        print("")
        print("The sign of this integer is negative (-).")
    else:
        # output
        print("")
        print("0")


if __name__ == "__main__":
    main()

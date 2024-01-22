#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0

    try:
        for i in range(x):
            # Check if the current element is an integer
            if type(my_list[i]) is int:
                # Use "{:d}".format() to print the integer value
                print("{:d}".format(my_list[i]), end=" ")
                integers_printed += 1

        # Print a new line after all integers are printed
        print()

    except (ValueError, TypeError, IndexError):
        # Handle the cases where there is a non-integer value or index is out of range
        pass

    return (integers_printed)

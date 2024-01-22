#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end=" ")
                integers_printed += 1

        print()

    except (ValueError, TypeError, IndexError):
        pass

    return (integers_printed)

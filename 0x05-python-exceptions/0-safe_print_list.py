#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            elements_printed += 1

    except IndexError:
        # Handle the case where the index is out of range
        pass

    finally:
        # Print a new line after all elements are printed or in case of an error
        print()

    return elements_printed

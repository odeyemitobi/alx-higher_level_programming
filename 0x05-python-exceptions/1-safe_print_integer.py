#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Use "{:d}".format() to print the integer value
        print("{:d}".format(value))

        # Print a new line after the integer
        print()

        # Return True to indicate that the value has been correctly printed
        return True

    except (ValueError, TypeError):
        # Handle the case where the value is not an integer
        return False

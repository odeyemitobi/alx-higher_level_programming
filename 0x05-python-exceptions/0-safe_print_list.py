def safe_print_list(my_list=[], x=0):
    # Initialize a variable to keep track of the number of elements printed
    elements_printed = 0

    # Use try-except block to handle potential errors
    try:
        # Iterate through the list up to the specified number of elements (x)
        for i in range(x):
            # Print the element on the same line
            print(my_list[i], end="")

            # Increment the count of elements printed
            elements_printed += 1

        # Print a new line after all elements are printed
        print()

    except IndexError:
        # Handle the case where the index is out of range
        print()

    # Return the real number of elements printed
    return (elements_printed)
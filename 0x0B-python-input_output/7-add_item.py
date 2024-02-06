#!/usr/bin/python3
"""
This script adds command line arguments to a list and saves it to a JSON file.

Usage:
    ./add_item.py arg1 arg2 ...

Arguments:
    arg1, arg2, ... : Command line arguments to be added to the list.

The list is saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it will be created.
"""

import json
import sys
from os import path


def save_to_json_file(my_obj, filename):
    """
    Save the given object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename: The name of the JSON file.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename: The name of the JSON file.

    Returns:
        The loaded object.
    """
    result = []
    if path.exists(filename):
        with open(filename, "r") as f:
            result = json.load(f)
    return result


def add_arguments_to_list(arguments_list, filename):
    """
    Add command line arguments to the list and save to a JSON file.

    Args:
        arguments_list: The list to which arguments will be added.
        filename: The name of the JSON file.
    """
    # Add all command line arguments to the list
    arguments_list.extend(sys.argv[1:])

    # Save the list to a JSON file using save_to_json_file function
    save_to_json_file(arguments_list, filename)


if __name__ == "__main__":
    # Initialize an empty list or load existing list from add_item.json
    my_list = load_from_json_file("add_item.json")

    # Add command line arguments to the list and save to add_item.json
    add_arguments_to_list(my_list, "add_item.json")

    print(f"Arguments added to the list and saved to add_item.json: {my_list}")

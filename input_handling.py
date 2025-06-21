"""
This module provides functinallity to handle user input using the first
commandline argument or through promts in the console.
"""
import sys


def get_valid_input(valid_options,
                    prompt_text="Choose an option: ",
                    prompt="> ",
                    error_text="... Invalid input."):
    """
    Get a valid input from the user or command line arguments.

    Args:
        valid_options: List of valid options
        prompt: Promt before the user input. Defaults to "> ".

    Returns:
        str: the selected option from the valid options
    """
    # Check command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in valid_options:
            return arg

    # Ask user until valid input is given
    while True:
        print(prompt_text, valid_options)
        user_input = input(prompt)

        if user_input in valid_options:
            return user_input
        print(error_text)

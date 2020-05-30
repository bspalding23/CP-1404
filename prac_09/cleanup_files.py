"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

#
# def main():
#     """Demo os module functions."""
#     print("Starting directory is: {}".format(os.getcwd()))
#
#     # Change to desired directory
#     os.chdir('Lyrics/Christmas')
#
#     # Print a list of all files in current directory
#     print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
#
#     # Make a new directory
#     # The next time you run this, it will crash if the directory exists
#     try:
#         os.mkdir('temp')
#     except FileExistsError:
#         print("File already exists sorry")
#         pass
#
#     # Loop through each file in the (current) directory
#     for filename in os.listdir('.'):
#         # Ignore directories, just process files
#         if os.path.isdir(filename):
#             continue
#
#         new_name = get_fixed_filename(filename)
#         print("Renaming {} to {}".format(filename, new_name))
#
#
# def get_fixed_filename(filename):
#     """Return a 'fixed' version of filename."""
#     new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
#     return new_name
#
#
# def demo_walk():
#     """Process all subdirectories using os.walk()."""
#     os.chdir('Lyrics')
#     for directory_name, subdirectories, filenames in os.walk('.'):
#         print("Directory:", directory_name)
#         print("\tcontains subdirectories:", subdirectories)
#         print("\tand files:", filenames)
#         print("(Current working directory is: {})".format(os.getcwd()))
#
#         for filename in filenames:
#             full_name = os.path.join(directory_name, filename)
#             new_name = os.path.join(directory_name, get_fixed_filename(filename))
#             os.rename(full_name, new_name)
#
#
# # main()
# demo_walk()

"""
CP1404/CP5632 Practical - Suggested Solution
Cleanup inconsistent song lyrics file names

Note: A complete solution for this exercise is NOT provided.
It's a very good thinking exercise and is less about the patterns we usually focus on
and more of a "tricky" problem to solve.
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()

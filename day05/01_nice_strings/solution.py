""" Solution to the first puzzle of Day 5 on adventofcode.com
"""
import os
import re

def validate(value):
    """ Determine if this string is naughty or nice
    """

    # First make sure it has at least three vowels
    no_vowels = re.sub(r'[^aeiou]', '', value)

    if len(no_vowels) < 3:
        return False

    found_double = False
    for element in range(1, len(value)):
        if value[element] == value[element-1]:
            found_double = True
            break

    if not found_double:
        return False

    if "ab" in value or \
       "cd" in value or \
       "pq" in value or \
       "xy" in value:
        return False

    return True


def main():
    """ Read in strings and count how many nice strings
        there are.
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    valid_strings = 0

    with open(file_path, 'r') as input_file:
        for line in input_file:
            if validate(line):
                valid_strings += 1

    print "Found {} valid strings.".format(valid_strings)

    assert valid_strings == 255

if __name__ == '__main__':
    main()

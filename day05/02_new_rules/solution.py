""" Solution to the second puzzle of Day 5 on adventofcode.com
"""
import os
import re

def validate(value):
    """ Determine if this string is naughty or nice
    """

    found_repeat = False
    for element in range(len(value)-1):
        search = value[element:element+2]
        reg_result = re.findall(search, value)
        if len(reg_result) >= 2:
            found_repeat = True
            continue

    if not found_repeat:
        return False

    found_sandwich = False
    for element in range(len(value)-2):
        if value[element] == value[element+2]:
            found_sandwich = True
            break

    if not found_sandwich:
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

    assert valid_strings == 55

if __name__ == '__main__':
    main()

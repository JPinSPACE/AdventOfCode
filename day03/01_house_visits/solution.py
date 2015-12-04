""" Solution to the first puzzle of Day 3 on adventofcode.com
"""
import os
from collections import defaultdict

def main():
    """ Intercept positional data on Santa and determine how many houses
        were visited at least once
    """
    house_tracker = defaultdict(int)
    house_tracker["0:0"] = 1

    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    (x_pos, y_pos) = (0, 0)
    with open(file_path, 'r') as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break

            if char == '<':
                x_pos -= 1
            elif char == '>':
                x_pos += 1
            elif char == '^':
                y_pos += 1
            elif char == 'v':
                y_pos -= 1
            elif char == '\n':
                continue
            else:
                print "Unexpected character: '{}'".format(char)

            house_tracker["{}:{}".format(x_pos, y_pos)] += 1

    print len(house_tracker.keys())

    # save the correct solution in case of refactors
    assert len(house_tracker.keys()) == 2081

if __name__ == '__main__':
    main()

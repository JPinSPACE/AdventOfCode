""" Solution to the second puzzle of Day 3 on adventofcode.com
"""
import os
from collections import defaultdict

def main():
    """ Intercept positional data on Robo-Santa and determine how
        many houses were visited at least once
    """
    house_tracker = defaultdict(int)
    house_tracker["0:0"] = 1

    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    (x_pos_santa, y_pos_santa) = (0, 0)
    (x_pos_robot, y_pos_robot) = (0, 0)

    which_santa = 0
    with open(file_path, 'r') as input_file:
        while True:
            char = input_file.read(1)
            if not char:
                break

            x_update = 0
            y_update = 0

            if char == '<':
                x_update = -1
            elif char == '>':
                x_update = 1
            elif char == '^':
                y_update = 1
            elif char == 'v':
                y_update = -1
            elif char == '\n':
                continue
            else:
                print "Unexpected character: '{}'".format(char)

            if which_santa % 2 == 0:
                x_pos_santa += x_update
                y_pos_santa += y_update
            else:
                x_pos_robot += x_update
                y_pos_robot += y_update

            which_santa += 1

            house_tracker["{}:{}".format(x_pos_santa, y_pos_santa)] += 1
            house_tracker["{}:{}".format(x_pos_robot, y_pos_robot)] += 1

    print len(house_tracker.keys())

    # save the correct solution in case of refactors
    assert len(house_tracker.keys()) == 2341


if __name__ == '__main__':
    main()

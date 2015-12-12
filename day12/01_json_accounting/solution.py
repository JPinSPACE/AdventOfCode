""" Solution to the first puzzle of Day 12 on adventofcode.com
"""
import os
import json

def json_sum(value):
    """ Sum up all the numbers!
    """
    summed = 0
    if isinstance(value, int):
        summed = value
    elif isinstance(value, basestring) and value.isdigit():
        summed = int(value)
    elif value is None:
        summed = 0
    elif isinstance(value, list):
        for subval in value:
            summed += json_sum(subval)
    elif isinstance(value, dict):
        for subval in value:
            summed += json_sum(value[subval])

    return summed


def main():
    """ Optimize Santa's route!
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    total = 0
    with open(file_path, 'r') as input_file:
        json_input = json.loads(input_file.read().strip())
        total += json_sum(json_input)

    print total

    assert total == 156366

if __name__ == '__main__':
    main()

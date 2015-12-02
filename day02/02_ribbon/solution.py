""" Solution to the second puzzle of Day 2 on adventofcode.com
"""
import os

def calculate_ribbon_length(package):
    """ Determine the amount of ribbon required to wrap a given package
        per the rules specified on adventofcode.com.
        Expected format: /^\d+x\d+x\d+$/
    """
    dimensions = sorted([int(dim) for dim in package.split('x')])
    base_ribbon = 2*dimensions[0] + 2*dimensions[1]
    bow = dimensions[0] * dimensions[1] * dimensions[2]

    return base_ribbon + bow


def main():
    """ Read in data from the elves and output the amount of ribbon they need.
    """
    ribbon_length = 0

    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    with open(file_path, 'r') as input_file:
        for line in input_file:
            ribbon_length += calculate_ribbon_length(line.strip())

    print "{} feet".format(ribbon_length)


if __name__ == '__main__':
    main()

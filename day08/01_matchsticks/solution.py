""" Solution to the first puzzle of Day 8 on adventofcode.com
"""
import os

def main():
    """ Read in Santa's list and calculate how much space it needs
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    total_length = 0
    evaled_length = 0

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            total_length += len(line)
            evaled_length += len(eval(line))

    print total_length - evaled_length

    assert total_length - evaled_length == 1342

if __name__ == '__main__':
    main()

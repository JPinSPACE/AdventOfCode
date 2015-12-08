""" Solution to the second puzzle of Day 8 on adventofcode.com
"""
import os

def main():
    """ Read in Santa's list and escape it
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    total_length = 0
    escaped_length = 0

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            total_length += len(line)

            line = line.replace(chr(92), chr(92)+chr(92))
            line = line.replace('"', chr(92) + '"')
            line = '"' + line + '"'

            escaped_length += len(line)

    print escaped_length - total_length

    assert escaped_length - total_length == 2074

if __name__ == '__main__':
    main()

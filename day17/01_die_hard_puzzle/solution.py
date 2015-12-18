""" Solution to the first puzzle of Day 17 on adventofcode.com
"""
import os
import itertools

def main():
    """ This puzzle brought to you by Simon Gruber
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    boxes = []

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            boxes.append(int(line))

    target = 150
    combos_found = 0
    for length in range(len(boxes) - 1):
        for combo in list(itertools.combinations(boxes, length+1)):
            if sum(combo) == target:
                combos_found += 1

    print combos_found, "combos found"




if __name__ == '__main__':
    main()

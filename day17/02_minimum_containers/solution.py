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
    shortest_combo = 9999
    shortest_combos = []
    for length in range(len(boxes) - 1):
        for combo in list(itertools.combinations(boxes, length+1)):
            if sum(combo) == target:
                if len(combo) < shortest_combo:
                    shortest_combo = len(combo)
                    shortest_combos = [combo]
                elif len(combo) == shortest_combo:
                    shortest_combos.append(combo)

    print "There are {} combos with " \
          "the shortest length {}".format(len(shortest_combos), shortest_combo)




if __name__ == '__main__':
    main()

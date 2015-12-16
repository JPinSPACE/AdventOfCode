""" Solution to the second puzzle of Day 15 on adventofcode.com
"""
import os

def evaluate_cookie(parts, part_names, ratios):
    """ I evaluate cookies by eating them.
    """
    cookie_score = 1

    attrs = sorted(parts[part_names[0]].keys())

    for attr in attrs:
        attr_score = 0
        for pos, ratio in enumerate(ratios):
            attr_score += ratio * parts[part_names[pos]][attr]
        if attr_score <= 0:
            return 0

        if attr == 'calories':
            if attr_score != 500:
                return 0
        else:
            cookie_score *= attr_score

    return cookie_score



def main():
    """ These are some seriously delicious cookies
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    parts = {}
    part_names = []

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            pieces = line.split(' ')
            part_names.append(pieces[0][:-1])
            parts[pieces[0][:-1]] = {
                                'capacity': int(pieces[2][:-1]),
                                'durability': int(pieces[4][:-1]),
                                'flavor': int(pieces[6][:-1]),
                                'texture': int(pieces[8][:-1]),
                                'calories': int(pieces[10])
                               }

    best_score = 0
    best_ratio = []

    for first in range(101)[1:]:
        for second in range(101 - first)[1:]:
            for third in range(101 - (first + second))[1:]:
                fourth = 100 - (first + second + third)
                score = evaluate_cookie(parts, part_names, [first,
                                                            second,
                                                            third,
                                                            fourth])
                if score > best_score:
                    best_score = score
                    best_ratio = [first, second, third, fourth]

    print best_score, best_ratio


if __name__ == '__main__':
    main()

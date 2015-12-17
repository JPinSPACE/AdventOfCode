""" Solution to the second puzzle of Day 16 on adventofcode.com
"""
import os
import re

def main():
    """ These are some seriously delicious cookies
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    mfcsam = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
            }

    with open(file_path, 'r') as input_file:
        for count, line in enumerate(input_file):
            res = re.findall(r'(\w+)\: (\d+)', line)
            failed = False

            for piece in res:
                if piece[0] == 'cats' or piece[0] == 'trees':
                    if mfcsam[piece[0]] >= int(piece[1]):
                        failed = True
                        break
                elif piece[0] == 'pomeranians' or piece[0] == 'goldfish':
                    if mfcsam[piece[0]] <= int(piece[1]):
                        failed = True
                        break
                elif mfcsam[piece[0]] != int(piece[1]):
                    failed = True
                    break
            if failed:
                continue

            print count + 1



if __name__ == '__main__':
    main()

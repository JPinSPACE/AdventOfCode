""" Solution to the first puzzle of Day 19 on adventofcode.com
"""
import os

def main():
    """ Reindeer medicine is a hell of a drug
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    transforms = []
    molecule = ''

    with open(file_path, 'r') as input_file:
        for line in [ r_line.strip() for r_line in input_file ]:
            if '=>' in line:
                (atom, replacement) = line.split(' => ')
                transforms.append([atom, replacement])
            elif line != '':
                molecule = line

    results = {}
    for transform in transforms:
        (atom, replacement) = transform
        safed_mol = molecule

        while True:
            if atom not in safed_mol:
                break
            new_mol = safed_mol.replace(atom, replacement, 1)

            # replace the old atoms with a safe character
            safed_mol = safed_mol.replace(atom, '.', 1)

            # put the old atoms back in place
            new_mol = new_mol.replace('.', atom)
            results[new_mol] = True


    print len(results.keys())


if __name__ == '__main__':
    main()

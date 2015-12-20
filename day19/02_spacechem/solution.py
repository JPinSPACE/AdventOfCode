""" Solution to the second puzzle of Day 19 on adventofcode.com
"""
import os

def main():
    """ Spacechem medicine is a hell of a drug
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    transforms = []
    molecule = ''

    with open(file_path, 'r') as input_file:
        for line in [ r_line.strip() for r_line in input_file ]:
            if '=>' in line:
                transform = line.split(' => ')
                transforms.append([transform[0], transform[1]])
            elif line != '':
                molecule = line

    new_molecule =  molecule[:]
    transform_count = 0
    while True:
        super_break = False
        for size in reversed(range(0, len(molecule))):
            for start in range(len(molecule)-size+1):
                window = molecule[start:start+size+1]
                for transform in transforms:
                    if transform[1] == window:
                        new_molecule = molecule.replace(window, transform[0], 1)
                        transform_count += 1
                        super_break = True
                        break
                if super_break:
                    break
            if super_break:
                break

        if new_molecule == 'e':
            break

        molecule = new_molecule[:]

    print transform_count
    assert transform_count == 200


if __name__ == '__main__':
    main()

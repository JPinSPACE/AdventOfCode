""" Solution to the first puzzle of Day 18 on adventofcode.com
"""
import os
import copy

GRID_SIZE = 100
ITERATIONS = 100

def main():
    """ Goddamnit, Topaz
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')


    lights = [ [ 0 for _ in range(GRID_SIZE) ] for _ in range(GRID_SIZE) ]
    new_lights = [ [ 0 for _ in range(GRID_SIZE) ] for _ in range(GRID_SIZE) ]

    with open(file_path, 'r') as input_file:
        for row, line in enumerate([ r_line.strip() for r_line in input_file ]):
            for col, char in enumerate(line):
                lights[row][col] = 0 if char == '.' else 1

    for _ in range(ITERATIONS):
        for row in range(len(lights)):
            for col in range(len(lights[row])):
                neighbors = 0

                # check neighbors
                for row_near in [ -1, 0, 1 ]:
                    for col_near in [ -1, 0, 1 ]:
                        if row + row_near < 0 or \
                           col + col_near < 0 or \
                           row + row_near >= GRID_SIZE or \
                           col + col_near >= GRID_SIZE or \
                           (row_near == 0 and col_near == 0):
                            continue

                        neighbors += lights[row + row_near][col + col_near]

                new_lights[row][col] = 0
                if lights[row][col] == 0:
                    if neighbors == 3:
                        new_lights[row][col] = 1
                else:
                    if neighbors == 2 or neighbors == 3:
                        new_lights[row][col] = 1

        lights = copy.deepcopy(new_lights)

    on_lights = sum([ sum(row) for row in lights ])
    print "{} lights are on".format(on_lights)
    assert on_lights == 814


if __name__ == '__main__':
    main()

""" Solution to the first puzzle of Day 6 on adventofcode.com
"""
import os

def main():
    """ Read in light instructions and do them!
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    # This ridiculous nop multiplication are because pylint
    # complained I wasn't using those variables.. now I am.
    lights = [ [ 0*nop1*nop2 for nop1 in range(1000) ] for nop2 in range(1000)]

    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.split(' ')
            if line[0] == 'toggle':
                (start, stop) = (line[1].split(','),
                                 line[3].split(','))

                for l_x in range(int(start[0]), int(stop[0])+1):
                    for l_y in range(int(start[1]), int(stop[1])+1):
                        lights[l_x][l_y] = 0 if lights[l_x][l_y] else 1
            else:
                (start, stop) = (line[2].split(','),
                                 line[4].split(','))

                for l_x in range(int(start[0]), int(stop[0])+1):
                    for l_y in range(int(start[1]), int(stop[1])+1):
                        lights[l_x][l_y] = 0 if line[1] == 'off' else 1

    on_lights = 0
    for row in lights:
        on_lights += sum(row)

    print on_lights

    assert on_lights == 400410

if __name__ == '__main__':
    main()

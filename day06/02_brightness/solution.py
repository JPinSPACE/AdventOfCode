""" Solution to the second puzzle of Day 6 on adventofcode.com
"""
import os

def main():
    """ Read in light instructions and do them!
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    lights = [ [ 0*nop1*nop2 for nop1 in range(1000) ] for nop2 in range(1000)]

    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.split(' ')
            if line[0] == 'toggle':
                (start, stop) = (line[1].split(','),
                                 line[3].split(','))

                for l_x in range(int(start[0]), int(stop[0])+1):
                    for l_y in range(int(start[1]), int(stop[1])+1):
                        lights[l_x][l_y] += 2
            elif line[1] == 'off':
                (start, stop) = (line[2].split(','),
                                 line[4].split(','))

                for l_x in range(int(start[0]), int(stop[0])+1):
                    for l_y in range(int(start[1]), int(stop[1])+1):
                        lights[l_x][l_y] -= 1
                        if lights[l_x][l_y] < 0:
                            lights[l_x][l_y] = 0

            elif line[1] == 'on':
                (start, stop) = (line[2].split(','),
                                 line[4].split(','))

                for l_x in range(int(start[0]), int(stop[0])+1):
                    for l_y in range(int(start[1]), int(stop[1])+1):
                        lights[l_x][l_y] += 1

    on_lights = 0
    for row in lights:
        on_lights += sum(row)

    print on_lights

    assert on_lights == 15343601

if __name__ == '__main__':
    main()

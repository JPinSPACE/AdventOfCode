""" Solution to the first puzzle of Day 9 on adventofcode.com
"""
import os
from itertools import permutations

def main():
    """ Optimize Santa's route!
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    cities = {}

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            pieces = line.split(' ')
            (start, end, dist) = (pieces[0], pieces[2], pieces[4])

            if start not in cities:
                cities[start] = {}

            if end not in cities:
                cities[end] = {}

            if end not in cities[start]:
                cities[start][end] = int(dist)

            if start not in cities[end]:
                cities[end][start] = int(dist)

    best_route = None
    best_length = 99999999 # no cities on Jupiter

    for route in permutations(cities.keys()):
        length = 0

        for route_pos, start in enumerate(route[:-1]):
            length += cities[start][route[route_pos+1]]

        if length < best_length:
            best_route = route
            best_length = length

    print "{} = {}".format(' -> '.join(best_route), best_length)

    assert best_length == 207


if __name__ == '__main__':
    main()

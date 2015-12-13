""" Solution to the first puzzle of Day 13 on adventofcode.com
"""
import os
from itertools import permutations

def happiness(names, guests):
    """ How does one calculate happiness anyway?
    """
    total_happiness = 0
    for seat in range(len(names)):
        total_happiness += guests[names[seat]][names[(seat+1) % len(names)]]
        total_happiness += guests[names[seat]][names[(seat-1) % len(names)]]
    return total_happiness

def main():
    """ Calculate the optimal dinner table seating arrangement
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    guests = {}

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            pieces = line.split(' ')
            (name, target, sign, units) = (pieces[0],
                                           pieces[10][:-1],
                                           pieces[2],
                                           pieces[3]
                                          )
            sign = 1 if sign == 'gain' else -1

            if name not in guests:
                guests[name] = {}

            guests[name][target] = int(units) * sign

    most_happy = 0
    best_arrangement = None
    for guest_arrangement in permutations(guests.keys()):
        happy = happiness(guest_arrangement, guests)

        if happy > most_happy:
            most_happy = happy
            best_arrangement = guest_arrangement

    print most_happy, best_arrangement

    assert most_happy == 618


if __name__ == '__main__':
    main()


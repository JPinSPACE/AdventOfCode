""" Solution to the first puzzle of Day 14 on adventofcode.com
"""
import os

def main():
    """ These are some seriously fast reindeer
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    herd = {}

    with open(file_path, 'r') as input_file:
        for line in [ raw_line.strip() for raw_line in input_file ]:
            pieces = line.split(' ')

            herd[pieces[0]] = {
                               'speed': int(pieces[3]),
                               'duration': int(pieces[6]),
                               'rest_length': int(pieces[13]),
                               'time_since_rest': 0,
                               'distance_flown': 0
                              }

    # reindeer simulation loop
    for _ in range(2503):
        for name, reindeer in herd.iteritems():
            if reindeer['time_since_rest'] >= reindeer['duration']:
                reindeer['time_since_rest'] = reindeer['rest_length'] * -1
            elif reindeer['time_since_rest'] > -1:
                reindeer['distance_flown'] += reindeer['speed']

            reindeer['time_since_rest'] += 1


    for name, reindeer in herd.iteritems():
        print "{} - {} km".format(name, reindeer['distance_flown'])





if __name__ == '__main__':
    main()

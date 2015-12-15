""" Solution to the second puzzle of Day 14 on adventofcode.com
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
                               'distance_flown': 0,
                               'points': 0
                              }

    # reindeer simulation loop
    for _ in range(2503):
        fastest_names = []
        best_distance = 0

        for name, reindeer in herd.iteritems():
            if reindeer['time_since_rest'] >= reindeer['duration']:
                reindeer['time_since_rest'] = reindeer['rest_length'] * -1
            elif reindeer['time_since_rest'] > -1:
                reindeer['distance_flown'] += reindeer['speed']

            if reindeer['distance_flown'] >= best_distance:
                if reindeer['distance_flown'] > best_distance:
                    fastest_names = []
                best_distance = reindeer['distance_flown']
                fastest_names.append(name)

            reindeer['time_since_rest'] += 1

        for name in fastest_names:
            herd[name]['points'] += 1


    for name, reindeer in herd.iteritems():
        print "{} - {}".format(name, reindeer['points'])


if __name__ == '__main__':
    main()


#      {_} {_}        {_} {_}        {_} {_}        {_} {_}
#     '-=\'-=\       '-=\'-=\       '-=\'-=\       '-=\'-=\
#        \\__\\____(    \\__\\____(    \\__\\____(    \\__\\____(
#       _|/-_|/---\\_  _|/-_|/---\\_  _|/-_|/---\\_  _|/-_|/---\\_
#       \   \        \ \   \        \ \   \        \ \   \        \

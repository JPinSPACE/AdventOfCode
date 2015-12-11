""" Solution to the first puzzle of Day 10 on adventofcode.com
"""

def main():
    """ Look and say with the Elves
    """

    puz_input = '1321131112'
    puz_output = ''

    for count in range(40):
        pos = 0 * count # now pylint thinks I used 'count'
        while pos < len(puz_input):
            start = puz_input[pos]
            letter_count = 1

            pos += 1
            while pos < len(puz_input) and puz_input[pos] == start:
                letter_count += 1
                pos += 1

            puz_output += str(letter_count) + start

        puz_input = puz_output
        puz_output = ''

    print len(puz_input)

    assert len(puz_input) == 492982

if __name__ == '__main__':
    main()

""" Solution to the first puzzle of Day 4 on adventofcode.com
"""
import md5

def main():
    """ Let's calculate some AdventCoins
    """

    puzzle_input = 'yzbqklnj'

    count = 0

    while True:
        new_input = "%s%06d" % (puzzle_input, count)
        coin = md5.new(new_input)

        if coin.hexdigest()[:5] == "00000":
            break

        # Just in case this somehow doesn't find a coin
        if count >= 999999:
            break
        count += 1

    print "Found a coin. It took {} tries.".format(count)
    assert count == 282749


if __name__ == '__main__':
    main()

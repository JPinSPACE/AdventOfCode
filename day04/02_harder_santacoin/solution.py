""" Solution to the second puzzle of Day 4 on adventofcode.com
"""
import md5

def main():
    """ Let's calculate some harder AdventCoins
    """

    puzzle_input = 'yzbqklnj'

    count = 0

    while True:
        new_input = "%s%06d" % (puzzle_input, count)
        coin = md5.new(new_input)

        if coin.hexdigest()[:6] == "000000":
            break

        # Just in case this somehow doesn't find a coin
        if count >= 9999999:
            break
        count += 1

    print "Found a coin. It took {} tries.".format(count)
    assert count == 9962624


if __name__ == '__main__':
    main()

""" Solution to the first puzzle of Day 2 on adventofcode.com
"""

def calculate_package_area(package):
    """ Determine the amount of wrapping paper required to wrap a given package
        per the rules specified on adventofcode.com.
        Expected format: /^\d+x\d+x\d+$/
    """
    dimensions = [int(dim) for dim in package.split('x')]
    sides = [ dimensions[0]*dimensions[1],
              dimensions[0]*dimensions[2],
              dimensions[1]*dimensions[2]
            ]

    return 2 * sum(sides) + min(sides)


def main():
    """ Read in data from the elves and output the amount of wrapping
        paper they need.
    """
    paper_area = 0
    with open('input', 'r') as input_file:
        for line in input_file:
            paper_area += calculate_package_area(line.strip())

    print "{} square feet".format(paper_area)


if __name__ == '__main__':
    main()

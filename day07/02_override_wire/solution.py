""" Solution to the second puzzle of Day 7 on adventofcode.com
"""
import os

PARTS = {}
CACHE = {}

def compute(value):
    """ Recursion is dumb.
    """

    if value in CACHE:
        return CACHE[value]

    if value.isdigit():
        return int(value)

    value = PARTS[value]

    if 'NOT' in value:
        value_a = value.split(' ')[1]
        return ~ compute(value_a)

    try:
        (value_a, operation, value_b) = value.split(' ')

        computed_a = compute(value_a)
        CACHE[value_a] = computed_a

        computed_b = compute(value_b)
        CACHE[value_b] = computed_b

        if operation == 'AND':
            computed = compute(value_a) & compute(value_b)
        elif operation == 'OR':
            computed = compute(value_a) | compute(value_b)
        elif operation == 'LSHIFT':
            computed = compute(value_a) << compute(value_b)
        elif operation == 'RSHIFT':
            computed = compute(value_a) >> compute(value_b)
        else:
            print "Topaz lied!"

        return computed
    except ValueError:
        return compute(value)

def main():
    """ Read in circuit instructions and assemble them!
    """
    # pylint: disable=W0603
    global CACHE

    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()

            (operation, name) = line.split(' -> ')
            PARTS[name] = operation

    signal_a = compute('a')

    CACHE = {}

    PARTS['b'] = str(signal_a)

    solution = compute('a')
    print solution

    assert solution == 14710


if __name__ == '__main__':
    main()

""" Solution to the second puzzle of Day 1 on adventofcode.com
"""

def main():
    """ Determine when Santa entered the basement
    """
    floor = 0
    char_pos = 0
    with open('santa_input', 'r') as input_file:
        while True:
            char_pos += 1
            char = input_file.read(1)
            if not char:
                break

            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            elif char == '\n':
                continue
            else:
                print "Unexpected character: '{}'".format(char)

            if floor < 0:
                print "Santa entered the basement at " \
                      "character position: '{}'".format(char_pos)
                break

if __name__ == '__main__':
    main()

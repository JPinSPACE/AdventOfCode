# Solution to the first puzzle of Day 1 on adventofcode.com

floor = 0
with open('santa_input', 'r') as input_file:
    while True:
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

print "Santa is on floor: {}".format(floor)

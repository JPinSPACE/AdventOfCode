""" Solution to the first puzzle of Day 23 on adventofcode.com
"""
import os
import re

def main():
    """ This is a very advanced machine
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(basedir, 'input')

    insts = []

    with open(file_path, 'r') as input_file:
        for line in [ r_line.strip() for r_line in input_file ]:
            res = re.search(r'^(\w\w\w) (.*?)(?:, (.\d+))?$', line)
            (inst, reg, offset) = res.groups()

            if inst == 'jmp':
                offset = reg
                reg = None

            insts.append({ 'inst' : inst,
                              'reg' : reg,
                              'offset' : int(offset) if offset else None
                            })

    reg = {'a': 0, 'b': 0}


    inst_ptr = 0
    while inst_ptr < len(insts):
        inst = insts[inst_ptr]

        if inst['inst'] == 'inc':
            reg[inst['reg']] += 1

        elif inst['inst'] == 'tpl':
            reg[inst['reg']] *= 3

        elif inst['inst'] == 'hlf':
            reg[inst['reg']] = int(reg[inst['reg']] * 0.5)

        elif inst['inst'] == 'jmp':
            inst_ptr += inst['offset']
            continue

        elif inst['inst'] == 'jie':
            if reg[inst['reg']] % 2 == 0:
                inst_ptr += inst['offset']
                continue

        elif inst['inst'] == 'jio':
            if reg[inst['reg']] == 1:
                inst_ptr += inst['offset']
                continue

        else:
            print "ERROR. Unknown instruction", inst
            exit()

        inst_ptr += 1

    print reg




if __name__ == '__main__':
    main()

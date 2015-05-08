#! /usr/bin/python
# http://torso.me/chicken
# http://torso.me/chicken-spec
# https://github.com/igorw/chicken-php/blob/master/examples/count.cha
from __future__ import print_function

from shared import chickens, instruction_map


def main():
    try:
        for line in iter(raw_input, 'END'):
            line = line.strip()
            try:
                print(chickens(instruction_map.index(line)))
            except ValueError:
                print(chickens(int(line) + 10))
    except EOFError:
        pass


if __name__ == '__main__':
    main()

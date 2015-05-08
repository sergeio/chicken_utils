#! /usr/bin/python
from __future__ import print_function

from shared import instruction_map


def main():
    try:
        for line in iter(raw_input, 'END'):
            number = count_chickens(line)
            try:
                print(instruction_map[number])
            except IndexError:
                print(number - 10)
                # print(number - 10, repr(chr(number - 10)))
    except EOFError:
        pass


def count_chickens(text):
    count = 0
    while text is not None:
        if text.startswith('chicken'):
            text = text.replace('chicken', '', 1)
            text = text.lstrip()
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    main()

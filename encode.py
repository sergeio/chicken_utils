#!/usr/bin/python
from break_number import ascii_factors


def main():
    """Print Chicken machine instructinons to print whatever comes in STDIN."""
    print(chickenify(raw_input()))


def chickenify(text):
    """Turns text into many chickens!"""
    assert(len(text) > 0)
    output = add_letter(text[0], [])
    for char in text[1:]:
        output = add_letter(char, output)
        output.append(chickens(2))
    return '\n'.join(output)


def add_letter(letter, output):
    """Add chickens to `output` representing the character `letter`."""
    output = list(output)
    output = add_number(ord(letter), output)
    output.append(char())
    return output


def add_number(number, output):
    """Add `number` to `output`, factoring it to minimize chickens needed."""
    output = list(output)
    factors, offset = ascii_factors[number]
    if offset == 1:
        output.append(literal(1))
    for factor in factors:
        output.append(literal(factor))
    for factor in factors[1:]:
        output.append(multiply())
    if offset == 1:
        output.append(add())
    elif offset == -1:
        output.append(literal(1))
        output.append(subtract())
    return output


def chickens(num):
    """Returns string of `num` space-separated 'chicken' strings."""
    return ' '.join(['chicken'] * num)


def literal(num):
    return chickens(10 + num)


def add():
    return chickens(2)


def subtract():
    return chickens(3)


def char():
    return chickens(9)


def multiply():
    return chickens(4)


if __name__ == '__main__':
    main()

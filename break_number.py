from functools import update_wrapper

from factorization import factors


def main():
    """Print information about encoding all ascii codes in chicken."""
    for i, f in ascii_factors.iteritems():
        c = encoding_cost(*f)
        print(i, c, '*' * (c/2), frepr(f))


def frepr(factors_with_offset):
    """String representation of a ([factors], offset) object."""
    factors = '*'.join(map(str, factors_with_offset[0]))
    offset = factors_with_offset[1]
    if factors_with_offset[1] == 1:
        return factors + '+' + str(offset)
    elif factors_with_offset[1] == -1:
        return factors + '-' + str(-offset)
    else:
        return factors


def map_acii_to_factors_with_offset():
    """Map numbers to their cheapest representation when chicken-encoded."""
    INF = float('inf')
    factor_map = calculate_factors_for_all_ascii_codes()
    factor_map_offset = {1: ([1], 0)}
    for k, v in factor_map.iteritems():
        previous = encoding_cost(factor_map[k - 1], 1) if k > 2 else INF
        next_ = encoding_cost(factor_map[k + 1], -1) if k < 127 else INF
        no_change = encoding_cost(v, 0)
        min_cost = min(previous, next_, no_change)
        if min_cost == no_change:
            factor_map_offset[k] = v, 0
        elif min_cost == previous:
            factor_map_offset[k] = factor_map[k - 1], 1
        elif min_cost == next_:
            factor_map_offset[k] = factor_map[k + 1], -1
    return factor_map_offset


def calculate_factors_for_all_ascii_codes():
    """Factor ascii codes to minimize their chicken-encoded length."""
    return dict(
        (i, factors_with_minimum_encoding_cost(i)) for i in xrange(2, 128))


def factors_with_minimum_encoding_cost(number):
    """Find minimum-length factoring of number.

    Is it better to encode 126 as 126 or as 7*18 or as 7*3*6, or ...?

    Output is not guaranteed to be minimal, but is shorter than doing nothing.

    """
    divisors = factors(number)
    min_ = float('inf'), []
    for i in xrange(1, len(divisors) + 1):
        current_divisors = combine_into_n_factors(i, divisors)
        cost = encoding_cost(current_divisors, 0)
        min_ = min(min_, (cost, current_divisors))
    return min_[1]


def combine_into_n_factors(n, factors):
    """Given factors list, multiply some together until len(factors) == n."""
    if n < len(factors):
        new_factors = list(factors[1:])
        new_factors[0] = new_factors[0] * factors[0]
        new_factors.sort()
        return combine_into_n_factors(n, new_factors)
    else:
        return factors


def encoding_cost(factors, offset):
    """How many chickens are required to represent product(factors)+-offset?"""
    base = sum(f + 14 for f in factors) - 4
    if not offset:
        return base
    elif offset > 0:
        return base + 13
    else:
        return base + 14


ascii_factors = map_acii_to_factors_with_offset()


if __name__ == '__main__':
    main()

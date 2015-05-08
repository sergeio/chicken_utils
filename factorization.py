def factors(num):
    """Factor `num` into factors."""
    if num < 1:
        return None
    primes = generate_primes(num)
    non_unique_factors = []
    i = 0
    while i < len(primes):
        p = primes[i]
        if not num % p:
            num /= p
            non_unique_factors.append(p)
        else:
            i += 1
    return non_unique_factors


def divisible_by_primes(num, primes):
    """Is `num` divisible by any of [`primes`]?"""
    for p in primes:
        if not num % p:
            return True
    return False


def generate_primes(_max):
    """Generate primes up to a maximum."""
    primes = [2, 3]
    for i in xrange(5, _max + 1):
        if not divisible_by_primes(i, primes):
            primes.append(i)
    return primes

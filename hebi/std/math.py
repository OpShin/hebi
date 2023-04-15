""" An implementation of some math operations in opshin """


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


def sign(a: int) -> int:
    return -1 if a < 0 else 1


def unsigned_int_from_bytes_big(b: bytes) -> int:
    """Converts a bytestring into the corresponding integer, big/network byteorder, unsigned"""
    acc = 0
    for i in range(len(b)):
        acc = acc * 256 + b[i]
    return acc

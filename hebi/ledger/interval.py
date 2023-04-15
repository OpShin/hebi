from hebi.prelude import *


def compare(a: int, b: int) -> int:
    # a < b: 1
    # a == b: 0
    # a > b: -1
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def compare_extended_helper(time: ExtendedPOSIXTime) -> int:
    if isinstance(time, NegInfPOSIXTime):
        return -1
    elif isinstance(time, FinitePOSIXTime):
        return 0
    elif isinstance(time, PosInfPOSIXTime):
        return 1
    else:
        return 0


def compare_extended(a: ExtendedPOSIXTime, b: ExtendedPOSIXTime) -> int:
    # a < b: 1
    # a == b: 0
    # a > b: -1
    a_val = compare_extended_helper(a)
    b_val = compare_extended_helper(b)
    if a_val == 0 and b_val == 0:
        a_finite: FinitePOSIXTime = a
        b_finite: FinitePOSIXTime = b
        return compare(a_finite.time, b_finite.time)
    else:
        return compare(a_val, b_val)


def get_bool(b: BoolData) -> bool:
    if isinstance(b, TrueData):
        return True
    else:
        return False


def compare_upper_bound(a: UpperBoundPOSIXTime, b: UpperBoundPOSIXTime) -> int:
    # a < b: 1
    # a == b: 0
    # a > b: -1
    result = compare_extended(a.limit, b.limit)
    if result == 0:
        a_val = 1 if get_bool(a.closed) else 0
        b_val = 1 if get_bool(b.closed) else 0
        return compare(a_val, b_val)
    else:
        return result


def compare_lower_bound(a: LowerBoundPOSIXTime, b: LowerBoundPOSIXTime) -> int:
    # a < b: 1
    # a == b: 0
    # a > b: -1
    result = compare_extended(a.limit, b.limit)
    if result == 0:
        a_val = 1 if get_bool(a.closed) else 0
        b_val = 1 if get_bool(b.closed) else 0
        return compare(b_val, a_val)
    else:
        return result


def contains(a: POSIXTimeRange, b: POSIXTimeRange) -> bool:
    """Returns True if the interval `b` is entirely contained in `a`."""
    lower = compare_lower_bound(a.lower_bound, b.lower_bound)
    upper = compare_upper_bound(a.upper_bound, b.upper_bound)
    return (lower == 1 or lower == 0) and (upper == 0 or upper == -1)


def make_range(
    lower_bound: POSIXTime,
    upper_bound: POSIXTime,
) -> POSIXTimeRange:
    """
    Create a bounded interval from the given time `lower_bound` up to the given `upper_bound`, including the given time
    """
    return POSIXTimeRange(
        LowerBoundPOSIXTime(FinitePOSIXTime(lower_bound), TrueData()),
        UpperBoundPOSIXTime(FinitePOSIXTime(upper_bound), TrueData()),
    )


def make_from(lower_bound: POSIXTime) -> POSIXTimeRange:
    """Create a bounded interval from the given time `lower_bound` up to infinity, including the given time"""
    return POSIXTimeRange(
        LowerBoundPOSIXTime(FinitePOSIXTime(lower_bound), TrueData()),
        UpperBoundPOSIXTime(PosInfPOSIXTime(), TrueData()),
    )


def make_to(upper_bound: POSIXTime) -> POSIXTimeRange:
    """
    Create a bounded interval from negative infinity up to the given `upper_bound`, including the given time
    """
    return POSIXTimeRange(
        LowerBoundPOSIXTime(NegInfPOSIXTime(), TrueData()),
        UpperBoundPOSIXTime(FinitePOSIXTime(upper_bound), TrueData()),
    )

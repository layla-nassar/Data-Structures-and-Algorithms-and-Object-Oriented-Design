def has_any_higher_fast(L1, L2):
    """
    Returns True if any item in L1 is greater than every item in L2.
    Runs in linear time O(n1 + n2).
    """
    # Find the maximum value in L2
    max_in_L2 = max(L2) if L2 else None

    # Compare each item in L1 against the max value in L2
    for item1 in L1:
        if item1 > max_in_L2:
            return True

    return False
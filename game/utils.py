def all_equal(t):
    """
    True if all elements in a table are equal.
    """
    return not t[0] == ' ' and t[1:] == t[:-1]


def list_not_all_none(lst):
    for el in lst:
        if el is not None:
            return True
    return False

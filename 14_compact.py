from xmlrpc.client import FastParser


def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    out = []
    for elem in lst:
        if elem:
            out.append(elem)
    return out
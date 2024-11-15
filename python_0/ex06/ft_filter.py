"""
ft_filter(function or None, iterable) --> generator

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""


def ft_filter(function, iterable):
    """
    My function ft_filter
    """
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))

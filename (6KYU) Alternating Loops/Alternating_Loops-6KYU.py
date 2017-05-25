import itertools


def combine(*args):
    return filter(lambda x: x is not None, itertools.chain.from_iterable(itertools.izip_longest(*args)))


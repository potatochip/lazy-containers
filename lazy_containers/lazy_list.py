"""List-like data-type that automatically uses set where more efficient.

Includes all operations of both set and list so you don't have to brain.
"""
from collections.abc import MutableSequence, MutableSet
from collections import Counter


class OptimizeMeta(type):
    def __call__(self, *args, **kwargs):
        cls = super().__call__(self, *args, **kwargs)
        if kwargs.get('optimize_memory', False):
            setattr(cls, '__set_seq', property(lambda self: set(self.seq)))
        else:
            setattr(cls, '__set_seq', set(args[0]))
        return cls

    # TODO: need to modify setting to use appropriate method
    # TODO: need to catch seq and optimize_memory from both args and kwargs
    # TODO: LazyList subclass MutableSet as well


class LazyList(MutableSequence):#, MutableSet):  #, metaclass=OptimizeMeta):
    def __init__(self, seq, optimize_memory=False):
        self.__seq = seq
        self.__set = set(seq)
        self.__count = Counter(seq)  # trade off memory for time in del

    @property
    def seq(self):
        return self.__seq

    @seq.setter
    def seq(self, value):
        self.__seq = value
        self.__set = set(value)
        self.__count = Counter(value)

    @property
    def set(self):
        return self.__set

    def __repr__(self):
        return self.seq.__repr__()

    def __contains__(self, key):
        # better performance using set
        return key in self.set

    def __getitem__(self, item):
        return self.seq.__getitem__(item)

    def __setitem__(self, key, value):
        self.seq.__setitem__(key, value)
        self.__set.add(value)
        self.__count[value] += 1

    def __delitem__(self, key):
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or len(self)
            for idx in range(start, stop, key.step):
                self.__del(idx)
        else:
            self.__del(key)

    def __del(self, index):
        try:
            value = self.seq.pop(index)
            self.__count[value] -= 1
            if not self.__count:
                self.__set.remove(value)
        except IndexError:
            pass

    def __len__(self):
        return self.seq.__len__()

    def count(self, value):
        # better performance using internal count
        return self.__count[value]

    def insert(self, index, object):
        self.seq.insert(index, object)
        self.__set.add(object)
        self.__count[object] += 1

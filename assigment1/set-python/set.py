'''
A set implemntaion for theory of computaion course
'''


class Set:
    def __init__(self, *args):
        self._dict = {}
        for arg in args:
            self._add(arg)

    def __repr__(self):
        return 'Set({})'.format(', '.join(str(x) for x in self._dict))

    def extend(self, other):
        '''Add several items at once'''
        for x in other:
            self.add(x)

    def add(self, x):
        '''Add one item to the set'''
        self._dict[x] = True

    def remove(self, x):
        '''Remove one item from the set'''
        del self._dict[x]

    def contains(self, x):
        '''Check if the set contains an item'''
        return self._dict.has_key(x)

    __contains__ = contains

    def __iter__(self):
        ''' Support the 'for item in set:' protocol. '''
        return iter(self._dict.copy())

    def __len__(self):
        ''' Support len(set) '''
        return len(self._dict)

    def items(self):
        '''Return a list of items in the set in sorted if possible'''
        result = self._dict.keys()
        try:
            result.sort()
        except TypeError:
            pass
        return result

    def __copy__(self):
        ''' Return a shallow copy of the set '''
        return Set(self)

    def union(self, other):
        ''' Return the union of two sets '''
        result = Set(self)
        result.extend(other)
        return result

    def intersection(self, other):
        ''' Return the intersection of two sets '''
        result = Set()
        for x in self:
            if x in other:
                result.add(x)
        return result

    def isdisjoint(self, other):
        ''' Return True if the two sets have a null intersection '''
        return all(x not in other for x in self)

    def issubset(self, other):
        ''' Return True if the set is a subset of other '''
        return all(x in other for x in self)

    def difference(self, other):
        ''' Return the set difference of two sets '''
        result = Set(self)
        for x in other:
            result.remove(x)
        return result

import json

import numpy as np
np.random.seed(0)
class StrMixin:
    def __str__(self):
        return f"Data: {self.data}"


# Property mixin
class PropertyMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        print(type(value))
        if isinstance(value, (list, np.ndarray)):
            self._data = value
        else:
            raise ValueError("Data must be a list")


class FileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.data:
                for idx, elem in enumerate(row):
                    row[idx] = int(elem)
                f.write(str(row))
                f.write('\n')




class ArrayWithMixin(np.lib.mixins.NDArrayOperatorsMixin, StrMixin, FileMixin, PropertyMixin):
    def __init__(self, data):
        self.data = data

    _HANDLED_TYPES = (np.ndarray, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:

            if not isinstance(
                x, self._HANDLED_TYPES + (ArrayWithMixin,)
            ):
                return NotImplemented

        inputs = tuple(x.data if isinstance(x, ArrayWithMixin) else x
                    for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, ArrayWithMixin) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
dims =10
a = ArrayWithMixin(np.random.randint(0, 10, (dims, dims)))
b = ArrayWithMixin(np.random.randint(0, 10, (dims, dims)))


@classmethod
def load_from_file(cls, filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return cls(np.array(data))


c = a+b
c.save_to_file("matrix+.txt")
d = a*b
d.save_to_file("matrix*.txt")
e = a@b
e.save_to_file("matrix@.txt")

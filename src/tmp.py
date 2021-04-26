class SomenteUmaAtribuiçãoMixin():
    __slots__ = ()

    def __setitem__(self, k, v):
        if k in self:
            raise AttributeError
        super().__setitem__(k, v)


class SomenteUmaAtribuiçãoNoDict(SomenteUmaAtribuiçãoMixin, dict):
    ...


class SomenteUmaAtribuiçãoNoDict2(dict, SomenteUmaAtribuiçãoMixin):
    ...

def print_mro(obj):
    print(', '.join(str(m) for m in obj.__mro__))


print_mro(SomenteUmaAtribuiçãoNoDict)
print_mro(SomenteUmaAtribuiçãoNoDict2)
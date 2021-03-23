from weakref import WeakKeyDictionary
from dataclasses import dataclass


class Cpf:
    def __init__(self, value=None):
        self.value = value

    def __get__(self, instance, cls):
        return self if instance is None else instance.__dict__[self.value]

    def __set__(self, instance, value):
        if not self.rule(value):
            raise TypeError('Cpf inválido')
        instance.__dict__[self.value] = value

    def __delete__(self, instance):
        del instance.__dict__[self.value]

    def rule(self, valor):
        return valor


class Cpf2:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not self.rule(value):
            raise TypeError(f'Cpf inválido')
        self._values[instance] = value

    def rule(self, valor):
        return valor


# class Empregado:
#     cpf = Cpf

#     def __init__(self, nome, idade, cpf) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf

# @dataclass()
class Empregado:
    nome = str()
    idade = int()
    cpf: Cpf2 = Cpf2()
    rg: Cpf2 = Cpf2()
    def __init__(self, *args) -> None:
        self.nome, self.idade, self.cpf, self.rg = args
    # cpf: Cpf = Cpf()
    # rg: Cpf = Cpf()


emp = Empregado('Ralph', 37, '333', '222')
emp2 = Empregado('Bruna', 33, '555', '444')

print(emp.nome, emp.cpf, emp.rg)
print(emp2.nome, emp2.cpf, emp2.rg)

print('mudando cpf', emp.nome)
emp.cpf = '654'
print(emp.nome, emp.cpf, emp.rg)
print(emp2.nome, emp2.cpf, emp2.rg)

print('mudando rg', emp.nome)
emp.rg = '888'
print(emp.nome, emp.cpf, emp.rg)
print(emp2.nome, emp2.cpf, emp2.rg)

print('mudando cpf', emp2.nome)
emp2.cpf = '654'
print(emp.nome, emp.cpf, emp.rg)
print(emp2.nome, emp2.cpf, emp2.rg)

print('mudando rg', emp2.nome)
emp2.rg = '555'
print(emp.nome, emp.cpf, emp.rg)
print(emp2.nome, emp2.cpf, emp2.rg)

# print(emp.cpf, emp.rg)
# print(emp2.cpf, emp2.rg)

# emp.cpf = Cpf('')
# print(emp.cpf)

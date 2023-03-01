from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def fabrica_transporte(self):
        print("fabricando: ")
        ...

    def transporta(self):
        transporte = self.fabrica_transporte()
        transporte.transporta()  # type: ignore


class Tipo(ABC):
    @abstractmethod
    def transporta(self):
        ...

    @abstractmethod
    def no_transporte(self):
        ...


class Caminhão(Tipo):
    def transporta(self):
        print("transportar de caminhão")

    def no_transporte(self):
        print("siga bem irmão caminhoneiro")


class Trem(Tipo):
    def transporta(self):
        print("transportar de trem")

    def no_transporte(self):
        print("cuidado com os surfistas")


class TransporteCaminhão(Transporte):
    def fabrica_transporte(self):
        super().fabrica_transporte()
        return Caminhão()


class TransporteTrem(Transporte):
    def fabrica_transporte(self):
        super().fabrica_transporte()
        return Trem()


def print_mro(obj):
    print(', '.join(str(m) for m in obj.__mro__))


def main(transporte: Transporte):
    transporte.transporta()


if __name__ == "__main__":
    print_mro(TransporteTrem)
    print_mro(TransporteCaminhão)
    main(TransporteTrem())
    main(TransporteCaminhão())

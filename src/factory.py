from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def fabrica_transporte(self):
        print("fabricando: ")
        ...

    def transporta(self):
        transporte = self.fabrica_transporte()
        transporte.transporta()


class Tipo():
    @abstractmethod
    def transporta(self):
        ...

    @abstractmethod
    def no_transporte(self):
        ...


class TransporteCaminhão(Transporte):
    def fabrica_transporte(self):        
        return Caminhão()


class TransporteTrem(Transporte):
    def fabrica_transporte(self):
        return Trem()



class Caminhão(Tipo):
    def transporta(self):
        print("transportar de caminhão")

    def no_transporte(self):
        print("siga bem irmão caminhoneiro")


class Trem(Tipo):
    def transporta(self):
        print("transporte de trem")

    def no_transporte(self):
        print("cuidado com os surfistas")


def main(transporte: Transporte):
    transporte.transporta()


if __name__ == "__main__":
    main(TransporteTrem())
    main(TransporteCaminhão())
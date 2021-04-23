from functools import wra


class Transporte():
    def fabrica_transporte(self):
        print("fabricando: ")
        ...

    def transporta(self):
        transporte = self.fabrica_transporte()
        transporte.transporta()

a = sum([1, 2, 3])

class Tipo():
    def transporta(self):
        ...

    def no_transporte(self):
        ...


class TransporteCaminhão(Transporte):
    def fabrica_transporte(self):
        super().fabrica_transporte()
        return Caminhão()

class TransporteTrem(Transporte):
    def fabrica_transporte(self):
        super().fabrica_transporte()
        return Trem()


class Caminhão():
    def transporta(self):
        print("transportar de caminhão")

    def no_transporte(self):
        print("siga bem irmão caminhoneiro")


class Trem():
    def transporta(self):
        print("transportar de trem")

    def no_transporte(self):
        print("cuidado com os surfistas")


def main(transporte: Transporte):
    transporte.transporta()


if __name__ == "__main__":
    main(TransporteTrem())
    main(TransporteCaminhão())

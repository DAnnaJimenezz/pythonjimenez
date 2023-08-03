class Empresa:
    def __init__(self, NIT, contrato, nombreOperador, modalidadJuego):
        self.__NIT = NIT
        self.__contrato = contrato
        self.__nombreOperador = nombreOperador
        self.__modalidadJuego = modalidadJuego

    def getNIT (self):
        return self.__NIT

    def getDatos (self):
        return self.__NIT, self.__contrato, self.__nombreOperador, self.__modalidadJuego
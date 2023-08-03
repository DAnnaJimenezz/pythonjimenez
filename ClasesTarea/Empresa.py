class Empresa:
    def __init__(self, contrato,NIT,nombreOperador, modalidadJuego):
        self.__contrato = contrato
        self.__NIT = NIT
        self.__nombreOperador = nombreOperador
        self.__modalidadJuego = modalidadJuego

    def getContrato (self):
        return self.__contrato
    
    def getNIT (self):
        return self.__NIT
    
    def getNombreOperador (self):
        return self.__nombreOperador
    
    def modalidadJuego (self):
        return self.__modalidadJuego
    
    def getDatos (self):
        return self.__NIT, self.__contrato, self.__nombreOperador, self.__modalidadJuego
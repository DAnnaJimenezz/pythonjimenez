class Estudiante:
    def __init__(self,codIcfes, codDane, puntajeMatematicas, percentilLecturaCritica):
        self.__codIcfes = codIcfes
        self.__codDane = codDane
        self.__puntajeMatematicas = puntajeMatematicas
        self.__percentilLecturaCritica = percentilLecturaCritica
    
    def getCodDane(self):
        return self.__codDane
    
    def verDatos(self):
        return f"{self.__codIcfes} {self.__codDane} {self.__puntajeMatematicas} {self.__percentilLecturaCritica}"
    
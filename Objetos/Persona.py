class Persona:
    def __init__(self, nombre, documento):
        print (int(input("Ingrese un curso:")))
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
        
    def getNombre(self):
        return self.__nombre
    def getNombre(self, nombre):
        self.__nombre=nombre 
    def getDocumento(self):
        return self.__documento
    def getDocumento(self, documento):
        self.__documento=documento
    def getCursos(self):
        return self.__cursos
    def getCursos(self,cursos):
        self.__cursos=cursos
        
    def __init__(self, ciudad):
        self.__ciudad=ciudad
        
    def getCiudad(self):
        return self.__ciudad
    def getCiudad(self,ciudad):
        self.__ciudad=ciudad
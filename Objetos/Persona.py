curso=input("Ingrese el nombre del curso:")
class Persona:
    def __init__(self, nombre, documento,cursos):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=cursos
        
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre=nombre 

    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento=documento
    
    def getCursos(self):
        return self.__cursos
    def setCursos(self,cursos):
        self.__cursos=cursos
    
    def agregarCursos(self,curso):
        self.__curso.append(curso)
        
    def getDatos(self):
        return self.__nombre, self.__documento, self.__cursos


p=Persona('Ana', 53031992, [curso])
print(p.getNombre ())


p.getDatos()
print(p.getDatos())
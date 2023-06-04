class Persona:
    def __init__(self, nombre, documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]
        
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
    
    def agregarCursos(self):
        curso=input("Ingrese el nombre del curso:")
        self.cursos.append(curso)

    def getDatos(self):
        return f'{self.__nombre}, {self.__documento}'


p=Persona('Ana', 123,)
print(p.getNombre())
q=Persona('Pedro',321,)
print(q.getNombre())

p.getDatos()
print(p.getDatos())
q.getDatos()
print(q.getDatos())

p.agregarCursos()
print(p.getCursos())
q.agregarCursos()
print(q.getCursos())
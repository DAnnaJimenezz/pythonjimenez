class Persona:
    listaGeneral=[]
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
    
    def agregarCursos(self,curso):
        self.__cursos.append(curso)
        for i in self.__cursos:
            if i not in Persona.listaGeneral:
                Persona.listaGeneral.append(i)
            
    def getDatos(self):
        return self.__nombre, self.__documento, self.__cursos


p=Persona('Ana', 53031992)
print(p.getNombre ())

p.agregarCursos ('Matematicas')
p.agregarCursos ('Sociales')
p.agregarCursos ('Ingles')

q=Persona('Pedro', 1019988626)
print(q.getNombre ())

q.agregarCursos ('Matematicas')
q.agregarCursos ('Tecnologia')
q.agregarCursos ('Fisica')

print(Persona.listaGeneral)

p.getDatos()
print(p.getDatos())
q.getDatos()
print(q.getDatos())

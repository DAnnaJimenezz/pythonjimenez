class Empleado:
    suma=0
    contador=0
    def __init__ (self, nombre, cargo, salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        Empleado.suma+=salario
        Empleado.contador+=1

    def getNombre (self):
        return self.__nombre
    def setNombre (self, nombre):
        self.__nombre=nombre 

    def getCargo (self):
        return self.__cargo
    def setCargo (self, cargo):
        self.__cargo=cargo
        
    def getSalario (self):
        return self.__salario
    def setSalario (self,salario):
        self.__salario=salario

    def gananciaEmpleadoporHora (self):
        return self.__salario / (168 * 4)
    
    def salarioIPC (self, salario):
        if self.__salario == salario:
            return self.__salario * 0.1312 + salario
        if self.__salario == salario:
            return self.__salario * 0.1312 + salario
        if self.__salario == salario:
            return self.__salario * 0.1612 + salario
        
    def horasExtrasSalario (self, horas_extras):
        if horas_extras > 48:
            return f'Se esta excediendo al numero de horas extras'
        else:
            suma= 4833 * horas_extras
            self.__salario = self.__salario + suma
            return suma 
                
    def sumaSalarios(self, salario):
        Empleado.suma +=self.__salario
        self.__salario = salario 
    
    def promedioSalarios(self,salario):
        Empleado.suma / self.__salario
        self.__salario = salario
            
    def getDatos(self):
        return self.__nombre, self.__cargo, self.__salario
    


x=Empleado('Jorge', 'Jefe', 3000000 )
print(x.getNombre ())

y=Empleado('Milena', 'Secretaria', 1500000 )
print(y.getNombre ())

z=Empleado('Pilar', 'Aseadora', 1000000)
print(z.getNombre ())

x.getDatos()
print(x.getDatos())
y.getDatos()
print(y.getDatos())
z.getDatos()
print(z.getDatos()) 

print()

x.gananciaEmpleadoporHora()
print(f'El salario ganado por horas es:', (x.gananciaEmpleadoporHora()))
y.gananciaEmpleadoporHora()
print(f'El salario ganado por horas es:', (y.gananciaEmpleadoporHora()))
z.gananciaEmpleadoporHora()
print(f'El salario ganado por horas es:', (z.gananciaEmpleadoporHora()))

print()

x.salarioIPC(3000000)
print(f'El incremento del IPC es:', (x.salarioIPC(3000000)))
y.salarioIPC(1500000)
print(f'El incremento del IPC es:', (y.salarioIPC(1500000)))
z.salarioIPC(1000000)
print(f'El incremento del IPC es:', (z.salarioIPC(1000000)))

print()

print(f'La horas extras de Jorge son:', (x.horasExtrasSalario(7)))
print(f'La horas extras de Milena son:', (y.horasExtrasSalario(49)))
print(f'La horas extras de Pilar son:', (z.horasExtrasSalario(10)))

print()

sumaSalarios=Empleado.suma
print(f'La suma de los salarios es:' , (sumaSalarios))

print()

promedioSalarios=Empleado.contador
print(f'El promedio de los salarios es:', (Empleado.suma/ 3))
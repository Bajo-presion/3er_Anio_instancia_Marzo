import random
from Estadistica import *


#CLASE ESTUDIANTE - USADO PARA CREAR BASE DE DATOS

# Si bien su atributo tiene el nombre completo, el nombre de clase debe ser sencillo
class Estudiante():   # y único para poder acceder a el fácilmente   
    def __init__(self,  
                 nombre=None,
                 curso=None,
                 dni= None                 
                 ):


        self.nombre = nombre
        self.curso = curso
        self.dni = dni # En caso de que hiciera falta - preguntar cuando se toma contacto con ellos
        


    def mostrar_datos(self):
        return  "DATOS ESTUDIANTE: " + \
                "\nNOMBRE: " + str(self.nombre) + \
                " --- \tDNI: " + str(self.dni) + \
                "\nCURSO: " + str(self.curso)


    #GETTERS
    
    def getNombre(self):
        return self.nombre
    
    def getDni(self):
        return self.dni
    
    def getCurso(self):
        return self.curso



    #SETTERS

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDni(self, dni):
        self.dni = dni
    
    def setCurso(self, curso):
        self.curso = curso
    
   






class Estado_estudiante(): #AÚN NO FUE USADO
    def __init__(self, 
                nroLista = None,
                instancia=None, 
                previa=False, 
                aprobado=False,
                notaFinal= None, 
                faltaHacer= None, 
                ejercicios_faltantes = ['9)a)', '9)b)', '9)c)', '11)', '13)a)', '13)b)', '14)'],
                observaciones=None):

        self.nroLista = nroLista
        self.instancia = instancia # Marzo, Julio, Diciembre o Especiales
        self.previa = previa # Será necesario por si hace falta llenar planillas
        self.aprobado = aprobado 
        self.notaFinal = notaFinal
        self.faltaHacer = faltaHacer 
        self.ejercicios_faltantes = ejercicios_faltantes
        self.observaciones = observaciones


    def mostrar_datos_alumno(self):
        return  "DATOS ESTADO ESTUDIANTE: " + \
                "\nNRO LISTA: " + str(self.nroLista) + \
                "\nINSTANCIA: " + str(self.instancia) + \
                " --- \tPREVIA: " + str(self.previa) + \
                "\nAPROBADO: " + str(self.aprobado) + \
                " --- \tNOTA FINAL: " + str(self.notaFinal) + \
                "\nFALTA HACER: " + str(self.faltaHacer) + \
                " --- \tEJERCICIOS FALTANTES: " + str(self.ejercicios_faltantes) + \
                "\nOBSERVACIONES: " + str(self.observaciones)


    #GETTERS
    
    def getNroLista(self):
        return self.nroLista

    def getInstancia(self):
        return self.instancia
    
    def getPrevia(self):
        return self.previa
    
    def getAprobado(self):
        return self.aprobado
    
    def getNotaFinal(self):
        return self.notaFinal
    
    def getObservaciones(self):
        return self.observaciones
    
    def getFaltaHacer(self):
        return self.faltaHacer
    
    def getEjercicios_faltantes(self):
        return self.ejercicios_faltantes
    




    #SETTERS

    def setNroLista(self, nroLista):
        self.nroLista = nroLista
    
    def setInstancia(self, instancia):
        self.instancia = instancia
    
    def setPrevia(self, previa):
        self.previa = previa
    
    def setAprobado(self, aprobado):
        self.aprobado = aprobado

    def setNotaFinal(self, notaFinal):
        self.notaFinal = notaFinal

    def setObservaciones(self, observaciones):
        self.observaciones = observaciones

    def setFaltaHacer(self, faltaHacer):
        self.faltaHacer = faltaHacer

    def setEjercicios_faltantes(self, ejercicios_faltantes):
        self.ejercicios_faltantes = ejercicios_faltantes




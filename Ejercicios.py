from Estadistica import *



# 9) a) Se debe arrojar un número entero aleatorio entre 5 y 40 amperes de consumo
class Ejercicio_9_a():
    def __init__(self,  
                 completo= False, 
                 nota=None,
                 mensaje=None):
        
        self.completo = completo 
        self.nota = nota
        self.mensaje = mensaje
    
    #def enunciado(self): #Posee el enunciado que verán los estudiantes como consigna
    #    return "9)a) ¿Qué GROSOR de cable debés utilizar/comprar si el consumo de tu termotanque será de: " + \
    #            str(bajar base de datos) + " AMPERES?"


    def mostrar_datos_ejercicio(self):
        return "DATOS EJERCICIO 9) a):" + \
                "\n■ Aprogado: " + str(self.completo) + \
                "\n■ Nota: " + str(self.nota) + \
                "\n■ Mensaje: " + str(self.mensaje) 
        #Por si necesitás mostrar sus datos

   
    #VISUALIZADOR

    def visualizar (self):
        print("RESOLUCIÓN EJERCICIO 9) a):")
        print[("")]


    # GETTERS
    def getCompleto (self):
        return self.completo
    
    def getNota (self):
        return self.nota

    def getMensaje (self):
        return self.mensaje


    # SETTERS
    def setCompleto (self, completo):
        self.completo = completo

    def setNota (self, nota):
        self.nota = nota
    
    def setMensaje (self, mensaje):
        self.mensaje = mensaje




print("=====================================")


c = ListaEstudiante()


#b)	¿Si mi cable es de 4 mm, cuántos amperes soportará antes que comience a recalentarse?


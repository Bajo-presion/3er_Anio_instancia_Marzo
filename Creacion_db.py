#########################################################################################################
##################### CREACIÓN BASE DE DATOS Y RESGUARDO - Ejecutar solo una vez ########################
#########################################################################################################

import random
import psycopg2
import xlrd




#GENERACIÓN DE EJERCICIOS
class Alerta_ejercicios():
    
    #-------------------------
    #GENERACIÓN DATOS EJ: 9)a)
    # 9) a) Se debe arrojar un número entero aleatorio entre 5 y 40 amperes de consumo 
    
    def aleatorio_amper (self): #Genera un int simple tipo: 35
        
        return random.randint(5, 40) #El rango del aleatorio amperes



    #-------------------------
    #GENERACIÓN DATOS EJ: 9)b)
    #9) b)	Generar números aleatorios entre [1, 1.5, 2.5, 4, 6, 10]
    
    def aleatorio_cable (self): #Genera un int simple tipo: 4
        
        return random.choice([1, 1.5, 2.5, 4, 6, 10])



    #-------------------------
    #GENERACIÓN DATOS EJ: 9)c)
    #9) c) Generar 3 int aleatorios desde 400 c/u que en suma no pueden superar los 9200
    #PC= de 700 a 1500  ---------  Freezer= de 2000 a 4000  --------  Minicomponente = de 1000 a 3700
    
    def aleatorio_amperes(self): # Genera tupla de tres datos tipo (3, 15, 6)
        
        return random.randint(3, 7), random.randint(9, 18), random.randint(5, 17)



    #-------------------------
    #GENERACIÓN DATOS EJ: 11)
    #11) aleatorio entre 2000 y 9000
    
    def aleatorio_watts(self): #Genera un int simple tipo: 6930
        
        return random.randrange(2000, 9000, 10)




    #-------------------------
    
    #GENERACIÓN DATOS EJ: 13)a)
    #GENERACIÓN DATOS EJ: 13)b)
    #Dos números binarios de 8 carácteres
    
    def aleatorio_binario(self): #Genera algo tipo: ('00101000', '11100111')
        a = []
        b = []
        for i in range(8):
            a.append(random.choice(['0','1']))

        for i in range(8):
            b.append(random.choice(['0','1']))
        
        return "".join(a), "".join(b) #No puedo pasarlo a int o se borraran los 0 de la izq

        


    #-------------------------
    #GENERACIÓN DATOS EJ: 14)
    #Almacenamiento entre 4 y 4096 --> [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    
    def aleatorio_gigas(self): #Genera un int simple tipo: 64
        
        return random.choice([4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])






#CREACIÓN DE TABLA POR ALUMNO INDIVIDUALMENTE
class _Alerta_db_creacion_tabla():
    def __init__(self, nombre_estudiante=None):
        self.nombre_estudiante = nombre_estudiante
    
    #Creación de la tabla - llama a clase _Alerta_ejercicios y nombra sus encabezados por cada ej


    #Subiendo a base de datos


    #Generación de hoja excel resguardo (para resubir a db en  caso de backup)




#GENERACIÓN AUTOMÁTICA DE TODAS LAS TABLAS EN BASE A LISTA DE ALUMNOS, CURSO O PREVIA

class _Alerta_creacion_db_tablas ():
    def __init__(self, lista):
        self.lista = lista
    

    #Creación DB específica por cada lista alumnos



    #Llamada a la función _Alerta_db_creacion_tabla






#ESTA CLASE SUMARÁ O ELIMINARÁ A UN ESTUDIANTE DE UNA DB EXISTENTE (para realizar ajustes)
class _Alerta_db_modificar():
    def __init__(self, nombre_estudiante=None):
        self.nombre_estudiante = nombre_estudiante
    
    # Función para eliminar a un estudiante de una db


    #Función para agregar un estudiante a una db


    #Funcion para trasladar a un estudiante de una db a otra


#CREACIÓN DE TABLAS AUTOMÁTICAS - ORGANIZACIÓN POSTGRE POR DEFAULT
# cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'nombre_tabla'")

    



    




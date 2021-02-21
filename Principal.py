import psycopg2
import xlrd

from Creacion_db import *
import pandas as pd


# CON ESTE ARCHIVO CREAS CURSOS NUEVOS, CREAS TABLAS DE EJERCICIOS Y LAS LLENAS
#TAMBIEN PASAS TABLAS A EXCEL

#ABAJO DE TODO ESTÁN LOS CÓDIGOS Q LOS LANZAN



cursos = {} #En este diccionario se crearán los cursos/tabla con armar_tabla_curso()
            #Se podrá eventualmente agregar más elementos con la función agregar_estudiante()

class Principal():

    def armar_tabla_curso():

        print()
        print("########################################################################################")
        print("###############################   BIENVENIDO :)   ######################################")
        print("########################################################################################")
        print()

        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )

 
        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()


       
        listaTemporal = []
        #cursos = {}
        print("Termine todo el proceso hasta el final para que los datos se guarden correctamente.")
        print("__________________________________________________________________________________")
        print()
        
        while True:
            print("-- A CADA CURSO CREADO LE CORRESPONDE UNA NUEVA TABLA --\nLos nombres de tablas no admiten espacios, ni empezar con nros o mayúscula.\
                \nEmpiece siempre con un caracter en minúscula.\n")

            while True:
                #CURSO ------------------------
                
                curso = input("Formato definitivo a usar ejemplo: 'real_3ro_1ra'\n\
                    \nNUEVO CURSO A CREAR: ")

                try:
                    cursor.execute(f"SELECT * FROM {curso}")
                    print("________________________________________________________")
                    print()
                    print("---> Esa tabla ya existe. Intente con otra. <---")
                    print()

                except:
                    print("-------")
                    break


            while True:
                while True: 
                    #NOMBRE ------------------------
                    print()
                    nombre = input(f"Nombre del/a estudiante de {curso}: ")

                    nombreValidacion = ''.join(nombre.split()) #Quitando los espacios intermedios
                    nombreValidacion = ''.join(nombreValidacion.split(',')) #Quitando las comas

                    if nombreValidacion.isalpha() == False:
                        print()
                        print("---> Ingresó un nombre incorrecto. No ingrese números. <---")
                        print()
                    
                    else:
                        print("-------")
                        print()
                        break

                
                while True: 
                    #DNI ------------------------
                    
                    dni = input("Ingresá DNI(sin puntos) - No ingreses nada si deseás completar después.\nDNI: ")

                    dniValidacion = ''.join(dni.split('.'))

                    if dniValidacion.isdigit() == True:
                        print()
                        print("----------------------------------------------------")
                        break

                    elif dni == '':
                        dni = None
                        print()
                        print("----------------------------------------------------")
                        break

                    else:
                        print()
                        print("--> Ingresá solo números, sin puntos ni espacio <--")
                        print()



                #Agregando a la lista temporal
                listaTemporal.append([nombre, dni])



                while True:
                    opcion_estudiante= input(f"YA HAY {len(listaTemporal)} ESTUDIANTES EN EL CURSO: {curso}.\
                        \n----------------------------------------------------\
                        \n[1] - Agregar otro/a estudiante.\n[2] - Dejar de ingresar estudiantes para el curso {curso}.\
                        \nSU ELECCIÓN: " )
                    if opcion_estudiante != '1' and opcion_estudiante != '2':
                        print()
                        print("--->  Ingrese 1 o 2. No otro número  <---")
                        print()
                    else:
                        break

                if opcion_estudiante == '2':
                    # Creando el diccionario y agregando los datos de los estudiantes cargados
                    cursos.setdefault(curso, listaTemporal)
                    listaTemporal=[]
                    print()
                    print(f"Saliendo de la tabla del CURSO: {curso} ...")
                    print()
                    print("--------------------------------------------")
                    print()
                    break

                else:
                    print()
                    print(f"Procediendo a agregar otro estudiante de {curso}...")
                    print()
            


            while True:
                eleeccion_curso = input("[1] - AGREGAR OTRO CURSO.\n[2] - Dejar de ingresar cursos.\
                    \nSU ELECCIÓN: ") 
                if eleeccion_curso != '1' and eleeccion_curso != '2':
                    print("Ingrese 1 o 2. No otro número")
                else:
                    break

            if eleeccion_curso == '1':
                print()
                print("Procediendo a agregar otro curso.")
                print()


            if eleeccion_curso == '2':
                print()
                print("Saliendo del programa de creacion de tablas por curso.")
                print(f"Se crearon {len(list(cursos))} cursos(tablas)")
                print()
                
                break

        
        
        #FINALIZANDO EL WHILE - SUBIR A BASE DE DATOS:
       
        


        #Creando la tabla SEGÚN NUESTRO DICCIONARIO
        for cant_tablas in range(len(list(cursos))):  #Debe ir entre comillas dobles porque tiene números. Ej: 3ro 1ra
            cursor.execute (f"""CREATE TABLE "{list(cursos)[cant_tablas]}" (
                ID SERIAL PRIMARY KEY NOT NULL,
                Estudiante VARCHAR(100),
                DNI VARCHAR (50))""")




        #------------------------------------------------------------------------------------------------------------------------------
        #Luego de crear la tabla ya se puede
        def generar_headers(nombre_diccionario):                  # USANDO SCHEMA POR DEFAULT                             #La tabla ya recibe el nombre de cada key
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{list(nombre_diccionario)[0]}'")
                                                                                    # DENTRO DE SCHEMA USANDO PUBLIC POR DEFECTO 


            #Esto no crea tablas, solo necesitamos como parámetro a una sola, la primera al menos SOLO para sacar 
            # sus headers (lo que nos interesa)
            #FUNCIONA CON LISTA DE LISTAS DENTRO DEL KEY Y CON UNO O MÁS KEYS


            temporal = cursor.fetchall()
            headers = [] #Haremos una lista pulida de encabezados
            for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
                headers.append(temporal[i+1][0])
            headers= ', '.join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
            
            return headers
            #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)





        def generar_valores(cada_estudiante):

            values = []
            #Aquí tenés dos opciones o el DNI existe o es None.

            for i in range(len(cada_estudiante)): #Ver cuántos valores tiene cada tabla
                if cada_estudiante[i] == None:
                    values.append('Null') #En join se le quitan las comillas e ira null al final para SQL
                    
                
                else:
                    valor = "'" + cada_estudiante [i] + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    values.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            values = ", ".join(values) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            return values #Listo para usarse en sentencia SQL


        def crear_Tabla_enDB(nombre_diccionario):
            #Se creará y ejecutará una sintaxis SQL para subir a DB por cáda key creada en un diccionario según requerimiento de tabla
            
            for cadaTabla in range(len(list(nombre_diccionario))):
                for cada_estudiante in nombre_diccionario.get(list(nombre_diccionario)[cadaTabla]):
                    print(f"En la tabla: {list(nombre_diccionario)[cadaTabla]} se agregó {generar_valores(cada_estudiante)}")
                    cursor.execute(f"INSERT INTO {list(nombre_diccionario)[cadaTabla]} ({generar_headers(nombre_diccionario)}) VALUES ({generar_valores(cada_estudiante)})")
                print("-------")

        #------------------------------------------------------------------------------------------------------------------------------


        #EJECUTANDO FUNCIONES PARA CREAR LA BASE DE DATOS
        print("Generando headers")
        print(generar_headers(cursos))
        print()
        print("generando valores")
        print(generar_valores(cursos.get( list(cursos) [0] ) [0] ))
        print()

        crear_Tabla_enDB(cursos)
        print()
        print("Proceso terminado con éxito.")
        print("Hasta luego :)")
        print()
        



# Hacer un código para modificar nombre de tabla

#Hacer código bajar y subir a excel para resguardo

#Hacer código para modificar o agregar un valor de la tabla

#Hacer codigo para modificar tabla agregar o quitar estudiantes

'''
    def modificar_tabla(): 

        print("-------------------------------------------------------------------------------------")
        print("-------------------------  Hola. Modifiquemos una tabla  ----------------------------")
        print("-------------------------------------------------------------------------------------")
        print()
        print()
'''





#______________________________________________________________________________________________________________________

class Main_Ejerccios(): 

    




    def crear_tabla_ejercicios(nombre_tabla, tabla_foranea, id_tabla_foranea): #AJUSTAR SIEMPRE AL TIPO DE DATOS DE EJERCICIOS QUE NECESITES - LO MISMO EN CREACION_DB
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()
        

        #Cada dato sera único:
        #Tabla con id primary - ej_9_a (INT) - ej_9_b (INT) - ej_9_c1 (INT) - ej_9_c2 (INT) - ej_9_c3 (INT) -   
                             #- ej_11 (INT) - ej_13_a (VARCHAR binario8) - ej_13_b (VARCHAR binario8) - ej_14 (INT)  
                                                      # un binario de 8 cifras en str

        
        #Creando tabla automáticamente según cantidad de estudiantes de la tabla del curso, utilizando su clave primaria
        #Puse que todos sean varchar porque hay números con ceros adelante.. si necesito operarlos luego los paso a int
        cursor.execute(f"""CREATE TABLE {nombre_tabla}(
            ID SERIAL PRIMARY KEY NOT NULL,
            EJ_9_A VARCHAR(10),
            EJ_9_B VARCHAR(10),
            EJ_9_C1 VARCHAR(10),
            EJ_9_C2 VARCHAR(10),
            EJ_9_C3 VARCHAR(10),
            EJ_11 VARCHAR(10),
            EJ_13_A VARCHAR(10),
            EJ_13_B VARCHAR(10),
            EJ_14 VARCHAR(10),
            ID_ALUMNO INTEGER REFERENCES {tabla_foranea} ({id_tabla_foranea}))
        """) #CREAR LA FOREIGN KEY EN UNA SOLA LINEA ES MUCHO MÁS FÁCIL
        
        print(f"Creación de la tabla {nombre_tabla} terminado. Esta tabla referencia a la PK({id_tabla_foranea}) de la tabla {tabla_foranea}")




    def llenar_tabla_ejercicios(nombre_tabla, tabla_foranea):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()




        #Conocer cuantos encfabezados hay
        cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        temporal = cursor.fetchall()
        
        headers = [] #Haremos una lista pulida de encabezados
        for i in range(len(temporal)-1): #No se tomará el valor [0] SI USAS ID PK AUTOCOPMLETADO POR ESO EL -1 (AJUSTAR)
            headers.append(temporal[i+1][0])
        headers= ', '.join(headers) #Unimos todo separando por comas y espacio para hacer desaparecer comillas internas 
        
        #HEADERS LISTOS PARA USAR (CON ID AUTOCOMPLETADO - AJUSTAR QUITANDOLE EL -1 Y +1 SI NO HAY ID PK)

        estudiantes = 0


        #Conocer cantidad de registros(estudiantes) que hay en la tabla elegida
        cursor.execute(f"SELECT COUNT(*) FROM {tabla_foranea}")
        estudiantes = cursor.fetchall()[0][0] #Los [0][0] es para eliminar su tupla dentro de una lista así da solo el int


        values = []
        
        
        #Creando el objeto para operar la clase ejercicios del archivo Creacion_db
        ejercicios = Alerta_ejercicios()
            
        for cada_estudiante in range(estudiantes): #Se hara una tupla grande según sus atributos(columnas)
            
            #Agregando uno a uno los ejercicios
            values.append(ejercicios.aleatorio_amper())
            values.append(ejercicios.aleatorio_cable())
            tupla_temporal = ejercicios.aleatorio_amperes()
            lista_temporal = list(tupla_temporal)
            values = values + lista_temporal
            values.append(ejercicios.aleatorio_watts())
            tupla_temporal2 = ejercicios.aleatorio_binario()
            lista_temporal = list(tupla_temporal2)
            values = values + lista_temporal
            values.append(ejercicios.aleatorio_gigas())
            values.append(cada_estudiante +1) #El id de lista estudiantes empieza por el 1

                        
            
            #Formatearemos la lista para la sintaxis SQL - 
            
            valores_SQL = []
            #CUANDO SE LLENA VALORES EN SQL SIEMPRE LOS STR LLEVAN COMILLA, LOS INT NO!
            for cada_dato in range(len(values)):
                
                if values[cada_dato] == None:
                    valores_SQL.append('Null') #En join se le quitan las comillas e ira null al final para SQL
                
                        #COMO TENES BINARIOS MEJOR QUE TODO SEA STR - LUEGO LO PASAS A INT CUANDO HAGA FALTA OPERAR

                else:
                    valor = "'" + str(values[cada_dato]) + "'"   # ES NECESARIO SOBRECOMILLAR LOS STR 
                    valores_SQL.append(valor) #En este caso ambos son str sí o sí para esta tabla (Ajustar en tablas distintas)

            valores_SQL = ", ".join(valores_SQL) #CON ESTE JOIN DESAPARECERAN LAS COMILLAS DEL INT Y LA COMILLA EXTRA DEL STR

            #Listo para usarse en sentencia SQL


            #CARGANDO LA TABLA CON CADA REGISTRO A LA VEZ

            cursor.execute(f"INSERT INTO {nombre_tabla} ({headers}) VALUES({valores_SQL})")

            #Proceso finalizado
            values = [] #Hay que reiniciar el valor inicial de valores para que no se sume valores sobre otros
            print(f"Llenado de la tabla {nombre_tabla} terminado.")


class Resguardo ():

    def pasar_a_excel(nombre_tabla, nombre_archivo_xlsx):
        #Conectando
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'instanciaMarzo',
            port = 5432,
            user = 'postgres',
            password = 'postgres'
        )


        conn.autocommit = True  

        #Cursor
        cursor = conn.cursor()
        print("================================")

        #conocer encabezados
        cursor.execute(f"SELECT column_name FROM information_schema.columns \
            WHERE table_schema = 'public' AND table_name = '{nombre_tabla}'")
        encabezados_puros = cursor.fetchall()
        
        encabezados = []
        for i in encabezados_puros: #Debo quitarles sus corchetes y parentesis
            encabezados.append(i[0])


        #Conocer cantidad de encabezados
        cant_encabezados = len(encabezados)

        #Conocer cantidad de registros
        cursor.execute(f"SELECT COUNT(*) FROM {nombre_tabla}")
        cant_filas = cursor.fetchall()

        # Crear el diccionario para subir a excel, cada key es encabezado columna 
        # y sus values los valores, los valores de toda la columna

        dic_para_excel = {} #Creando el diccionario de columnas que usaremos para subir al excel

        #Codigo para reutilizar
        #Llenando el diccionario con cualquiera fuera las columnas que tenga.
        for atributo in range(cant_encabezados):
            dic_para_excel.setdefault(encabezados[atributo], [])

        #Llenado de ese diccionario con append... cada key es encabezado de CADA COLUMNA
        for fila in range(cant_filas[0][0]): #[0][0] para quitarle su corchete y parentesis
            for columna in range(len(encabezados)):
                cursor.execute(f"SELECT * FROM {nombre_tabla} WHERE id='{fila+1}'")
                estudiante = cursor.fetchall()
                estudiante =  estudiante[0] #Debo quitarle el [] o saldra del rango luego

                #Agregando uno a uno en cada iteración
                dic_para_excel.get(list(dic_para_excel)[columna]).append(estudiante[columna])
                
        #Del la BD se pasa al data frame y del data frame al excel.. siempre el data frame de intermedio
        data_frame = pd.DataFrame(dic_para_excel, columns= (list(dic_para_excel)))
                    #pd es panda.. lo importe al panda como as pd


        
        # Eliminá el archivo excel si vas a quitar este comentario
        #print(r'nombre_archivo_xlsx')

        # Probemos ahora sin quitarle los índices
        
        
        ######################################################
        ########  SEGURIDAD - SEGURIDAD - SEGURIDAD  #########
        ######################################################
        
        print("SEGURIDAD: VERI SI ESTÁ COMENTADO EL GUARDADO PARA QUE NO SOBREESCRIBAS ALGÚN EXCEL EXISTENTE")
        #data_frame.to_excel(f'Resguardo\{nombre_archivo_xlsx}', index=False, header=True)
        print("Ver si está comentado. Si no lo está, verás que no se creó el archivo")




#ESTE CÓDIGO PASA UNA TABLA DE BASE DE DATOS A UN EXCEL#
#Resguardo.pasar_a_excel('ejer_previas_marzo2021_tecno', 'exel_tabla_ejercicios_previa.xlsx')


        
#HABILITÁ ESTE CÓDIGO PARA CREAR UN NUEVO CURSO/TABLA
#Principal.armar_tabla_curso()



        
#Crear luego un Principal para elegir siempre si crear mas tablas de curso o lo q fuera

#PRIMERO SE CREA LA TABLA EJERCICIO
#Crear la tabla - automatizalo xq no sabés cuantas instancias de exámenes habrá (tabla nueva, tabla foranea, referencia PK foranea)
#Main_Ejerccios.crear_tabla_ejercicios('ejer_previas_marzo2021_tecno', 'real_previas_marzo2021_tecnologia','id')


#LUEGO SE LA LLENA la tabla de ejercicio
#Llenar la tabla según cantidad de alumnos de la tabla foreign
#Main_Ejerccios.llenar_tabla_ejercicios('ejer_previas_marzo2021_tecno', 'real_previas_marzo2021_tecnologia')




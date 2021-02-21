
class ListaEstudiante():
    def __init__(self,
                curso = None,
                año = None,
                cantidad = 0,
                cant_aprobados=0,
                porcen_aprobados= 0,
                cant_desaprobados= 0,
                porcen_desaprobados= 0):

        self.curso = curso
        self.año = año
        self.cantidad = cantidad
        self.cant_aprobados = cant_aprobados
        self.porcen_aprobados = porcen_aprobados
        self.cant_desaprobados = cant_desaprobados
        self.porcen_desaprobados = porcen_desaprobados



    #GETTERS
    def getCurso(self):
        return self.curso

    def getAño(self):
        return self.año
    
    def getCantidad(self):
        return self.cantidad
    
    def getCant_aprobados(self):
        return self.cant_aprobados
    
    def getPorcen_aprobados(self):
        return self.porcen_aprobados
    
    def getCant_desaprobados(self):
        return self.cant_desaprobados

    def getPorcen_desaprobados(self):
        return self.porcen_desaprobados




    #SETTERS

    def setCurso(self, curso):
        self.curso = curso
    
    def setAño(self, año):
        self.año = año
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad
    
    def setCant_aprobados(self, cant_aprobados):
        self.cant_aprobados = cant_aprobados
    
    def setPorcen_aprobados(self, curso):
        self.porcen_aprobados = porcen_aprobados
    
    def setCant_desaprobados(self, cant_desaprobados):
        self.cant_desaprobados = cant_desaprobados
    
    def setPorcen_desaprobados(self, porcen_desaprobados):
        self.porcen_desaprobados = porcen_desaprobados
    

    #Tanto cantidad de estudiantes como estudiantes 
    #son datos que ingresan desde el extrerior
    

    #Cálculo de porcentaje de aprobados


    #Cálculo de porcentaje de desaprobados



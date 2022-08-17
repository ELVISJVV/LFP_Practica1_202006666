class Curso:

    def __init__(self, codigo, nombre, prerrequisitos, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisitos = prerrequisitos
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    
    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre

    def getPrerrequisitos(self):
        return self.prerrequisitos
    
    def getObligatorio(self):
        return self.obligatorio

    def getSemestre(self):
        return self.semestre

    def getCreditos(self):
        return self.creditos
    
    def getEstado(self):
        return self.estado


    def setNombre(self, nombre):
        self.nombre = nombre
    
    def selfPrerrequisitos(self, prerrequisitos):
        self.prerrequisitos = prerrequisitos

    def setObligatorio(self, obligatorio):
        self.obligatorio = obligatorio
    
    def setSemestre(self, semestre):
        self.semestre = semestre
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setCreditos(self, creditos):
        self.creditos = creditos
    
    def setEstado(self, estado):
        self.estado = estado

cursos=[]



from tkinter import messagebox

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
    
    def setPrerrequisitos(self, prerrequisitos):
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

def Lectura(ruta):
        try:
            objeto = open(ruta,'r+',encoding='utf-8')
            lineas = objeto.readlines()
            objeto.close()
        except:
            titulo = "Error"
            mensaje = 'Ha ocurrido algún error con el archivo.\n Intenta ingresar otro archivo'
            messagebox.showerror(titulo, mensaje)
        
        for linea in lineas:
            pos=-1
            try:
            
                data = linea.split(',') # Devuelve una lista
                curso = Curso(data[0], data[1], data[2], data[3], data[4],data[5],data[6].rstrip('\n'))
            except:
                continue
            # cursos.append(curso)
            for dato in cursos:
                if curso.getCodigo()==dato.getCodigo():
                 pos = cursos.index(dato)
            if pos!=-1:
                cursos.pop(pos)
            cursos.append(curso)
        titulo = "Agregar Cursos"
        mensaje = 'Se han agregado los cursos'
        messagebox.showinfo(titulo, mensaje)
        
            
        
        return cursos

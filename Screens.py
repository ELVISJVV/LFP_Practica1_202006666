from re import T
from  tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as FileDialog
from curso import *


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass





# Main Screen
def ventana_principal():
    root= tk.Tk()
    root.title('Ventana Principal')
    root.geometry('700x800+600+120')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = FirstScreen(root = root)
    
    app.mainloop()

class FirstScreen(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=700, height=800)
        self.root = root
        self.pack(padx=30,pady=20)
        self.config( bg='#a6bdae')
        
        self.Ventana()

    def Ventana(self):
        self.label_curso= tk.Label(self,text="Lab. Lenguajes Formales y de Programación B+")
        self.label_curso.config( font=('Times New Roman',13), fg='white', bg='#00251a', width=50)
        self.label_curso.place(x=25,y=50)

        self.label_curso= tk.Label(self,text="Elvis Joseph Vásquez Villatoro")
        self.label_curso.config( font=('Times New Roman',13), fg='white', bg='#00251a', width=50)
        self.label_curso.place(x=25,y=100)
        
        self.label_curso= tk.Label(self,text="Carné: 202006666")
        self.label_curso.config( font=('Times New Roman',13), fg='white', bg='#00251a', width=50)
        self.label_curso.place(x=25,y=150)

        
        
        


        Button(self, text="Cargar Archivo", command=self.cargar_archivo , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=275)
        Button(self, text="Gestionar Cursos",command=self.ir_gestionar , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=350)
        Button(self, text="Conteo de Créditos" ,command=self.ir_conteo, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=425)
        Button(self, text="Salir", command=self.salir , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=500)
    
    
    def cargar_archivo(self):
        self.root.destroy()
        ventana_cargar_archivo()
    def salir(self):
        self.root.destroy()
    def ir_gestionar(self):
        self.root.destroy()
        ventana_gestionar_cursos()
    def ir_conteo(self):
        self.root.destroy()
        ventana_conteo_creditos()


    
# Ventana Cagar Archivo
def ventana_cargar_archivo():
    root= tk.Tk()
    root.title('Cargar Archivo')
    root.geometry('900x400+500+200')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = CargarArchivo(root = root)
    
    app.mainloop()


class CargarArchivo(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=400)
        self.root = root
        self.pack(padx=25,pady=20)
        self.config( bg='#a6bdae')
        
        self.Ventana()

    def Ventana(self):
        self.lable_ruta=tk.Label(self,text="Ruta")
        self.lable_ruta.config(font=('Times New Roman',15), fg='white', bg='#00251a', width=15)
        self.lable_ruta.place(x=80, y=50)
        
        ingresar_ruta =tk.StringVar()
        ruta= ttk.Entry(self,textvariable=ingresar_ruta).place(x=80,y=120, width=540,height=35)

        Button(self, text="Seleccionar" ,command= lambda:Lectura(ingresar_ruta.get()), font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=250)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=250)
        
        Button(self, text="Buscar", command= lambda: ingresar_ruta.set(self.abrir()),font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=639, y=120)
        
        


    def regresar(self):
        self.root.destroy()
        ventana_principal()
        
    
    def abrir(*args):
        Fichero=FileDialog.askopenfilename(title="Selecciona el archivo")
        a=Fichero
        # print(a)
        return a

# Ventana Gestionar Cursos
def ventana_gestionar_cursos():
    root= tk.Tk()
    root.title('Gestionar Cursos')
    root.geometry('600x600+670+180')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = GestionarCursos(root = root)
    
    app.mainloop()

class GestionarCursos(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=600, height=600)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()


    def Ventana(self):
        
        Button(self, text="Listar Cursos",command=self.listar_cursos, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=50)
        Button(self, text="Mostrar Curso" ,command=self.mostrar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=125)
        Button(self, text="Agregar Curso" ,  command=self.agregar_curso ,font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=200)
        Button(self, text="Editar Curso" ,command=self.editar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=275)
        Button(self, text="Eliminar Curso",command=self.eliminar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=350)
        Button(self, text="Regresar", command=self.regresar , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=425)

        
    
    
    
    def regresar(self):
        self.root.destroy()
        ventana_principal()
    def agregar_curso(self):
        self.root.destroy()
        ventana_agreagar_curso()
    def mostrar_curso(self):
        self.root.destroy()
        ventana_mostrar_curso()
    def eliminar_curso(self):
        self.root.destroy()
        ventana_eliminar_curso()
    def editar_curso(self):
        self.root.destroy()
        ventana_editar_curso()
    def listar_cursos(self):
        self.root.destroy()
        ventana_listar_cursos()

# Ventana agregar curso
def ventana_agreagar_curso():
    root= tk.Tk()
    root.title('Agregar Curso')
    root.geometry('900x700+500+100')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = AgregarCurso(root = root)
    
    app.mainloop()



class AgregarCurso(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=700)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()

    def Ventana(self):
        
        Label(self, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        


        self.tk_codigo =tk.StringVar()
        self.tk_nombre =tk.StringVar()
        self.tk_prerrequisitos =tk.StringVar()
        self.tk_obligatorio =tk.StringVar()
        self.tk_semeste =tk.StringVar()
        self.tk_creditos =tk.StringVar()
        self.tk_estado=tk.StringVar()



        self.codigo= ttk.Entry(self,textvariable=self.tk_codigo).place(x=325,y=50, width=500,height=35)
        self.nombre= ttk.Entry(self,textvariable=self.tk_nombre).place(x=325,y=120, width=500,height=35)
        self.prerrequisito= ttk.Entry(self,textvariable=self.tk_prerrequisitos).place(x=325,y=190, width=500,height=35)
        self.obligatorio= ttk.Entry(self,textvariable=self.tk_obligatorio).place(x=325,y=260, width=500,height=35)
        self.semestre= ttk.Entry(self,textvariable=self.tk_semeste).place(x=325,y=330, width=500,height=35)
        self.creditos= ttk.Entry(self,textvariable=self.tk_creditos).place(x=325,y=400, width=500,height=35)
        self.estado= ttk.Entry(self,textvariable=self.tk_estado).place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Agregar" ,command=self.agregar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        
        


    def agregar(self):
        
        curso=Curso(self.tk_codigo.get(),self.tk_nombre.get(),self.tk_prerrequisitos.get(),
        self.tk_obligatorio.get(),self.tk_semeste.get(),self.tk_creditos.get(),self.tk_estado.get())
        

        
        pos=-1
        
        
        codigo=self.tk_codigo.get()
        if codigo.isspace() == True or len(codigo)==0:
            titulo = "Agregar Curso"
            mensaje = 'No se llenaron los campos correctamente'
            messagebox.showerror(titulo, mensaje)
        else:
            for dato in cursos:
                # print(dato.getCodigo())
                if codigo==dato.getCodigo():
                    pos = cursos.index(dato)
            if pos!=-1:
                cursos.pop(pos)

            cursos.append(curso)
            titulo = "Agregar Curso"
            mensaje = 'Se ha agregado el curso'
            messagebox.showinfo(titulo, mensaje)
            self.tk_codigo.set('')
            self.tk_nombre.set('')
            self.tk_prerrequisitos.set('')
            self.tk_obligatorio.set('')
            self.tk_semeste.set('')
            self.tk_creditos.set('')
            self.tk_estado.set('')


        

    def regresar(self):
         self.root.destroy()
         ventana_gestionar_cursos()
    
#Ventana mostrar Curso
def ventana_mostrar_curso():
    root= tk.Tk()
    root.title('Mostrar Curso')
    root.geometry('900x700+500+100')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = MostrarCurso(root = root)
    
    app.mainloop()



class MostrarCurso(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=700)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()


    def Ventana(self):
        
        Label(self, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        

        self.tk_codigo =tk.StringVar()
        self.tk_nombre =tk.StringVar()
        self.tk_prerrequisitos =tk.StringVar()
        self.tk_obligatorio =tk.StringVar()
        self.tk_semeste =tk.StringVar()
        self.tk_creditos =tk.StringVar()
        self.tk_estado=tk.StringVar()

        
        self.codigo= ttk.Entry(self,textvariable=self.tk_codigo).place(x=325,y=50, width=500,height=35)
        self.nombre= ttk.Entry(self,textvariable=self.tk_nombre,state='disabled').place(x=325,y=120, width=500,height=35)
        self.prerrequisito= ttk.Entry(self,textvariable=self.tk_prerrequisitos,state='disabled').place(x=325,y=190, width=500,height=35)
        self.obligatorio= ttk.Entry(self,textvariable=self.tk_obligatorio,state='disabled').place(x=325,y=260, width=500,height=35)
        self.semestre= ttk.Entry(self,textvariable=self.tk_semeste,state='disabled').place(x=325,y=330, width=500,height=35)
        self.creditos= ttk.Entry(self,textvariable=self.tk_creditos,state='disabled').place(x=325,y=400, width=500,height=35)
        self.estado= ttk.Entry(self,textvariable=self.tk_estado,state='disabled').place(x=325,y=470, width=500,height=35)

        
        

        Button(self, text="Mostrar" , command=self.mostrar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
       
    
    def mostrar(self):
        pos = -1
        
        codigo=self.tk_codigo.get()

        for dato in cursos:
            # print(dato.getCodigo())
            if codigo==dato.getCodigo():
                pos = cursos.index(dato)
        
        if pos==-1:
            titulo = "Mostrar Curso"
            mensaje = 'No se ha encontrado el curso'
            messagebox.showerror(titulo, mensaje)
        else:
            self.tk_nombre.set(cursos[pos].getNombre())
            self.tk_codigo.set(cursos[pos].getCodigo())
            
            self.tk_prerrequisitos.set(cursos[pos].getPrerrequisitos())
            self.tk_obligatorio.set(cursos[pos].getObligatorio())
            self.tk_semeste.set(cursos[pos].getSemestre())
            self.tk_creditos.set(cursos[pos].getCreditos())
            self.tk_estado.set(cursos[pos].getEstado())
            


        

    def regresar(self):
         self.root.destroy()
         ventana_gestionar_cursos()

# Ventana Eliminar Curso
def ventana_eliminar_curso():
    root= tk.Tk()
    root.title('Eliminar Curso')
    root.geometry('900x700+500+100')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = EliminarCurso(root = root)
    
    app.mainloop()



class EliminarCurso(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=700)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()
    

    def Ventana(self):
        
        Label(self, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        


        self.tk_codigo =tk.StringVar()
        self.tk_nombre =tk.StringVar()
        self.tk_prerrequisitos =tk.StringVar()
        self.tk_obligatorio =tk.StringVar()
        self.tk_semeste =tk.StringVar()
        self.tk_creditos =tk.StringVar()
        self.tk_estado=tk.StringVar()

        self.codigo= ttk.Entry(self,textvariable=self.tk_codigo).place(x=325,y=50, width=200,height=35)
        self.nombre= ttk.Entry(self,textvariable=self.tk_nombre, state='disabled').place(x=325,y=120, width=500,height=35)
        self.prerrequisito= ttk.Entry(self,textvariable=self.tk_prerrequisitos, state='disabled').place(x=325,y=190, width=500,height=35)
        self.obligatorio= ttk.Entry(self,textvariable=self.tk_obligatorio, state='disabled').place(x=325,y=260, width=500,height=35)
        self.semestre= ttk.Entry(self,textvariable=self.tk_semeste, state='disabled').place(x=325,y=330, width=500,height=35)
        self.creditos= ttk.Entry(self,textvariable=self.tk_creditos, state='disabled').place(x=325,y=400, width=500,height=35)
        self.estado= ttk.Entry(self,textvariable=self.tk_estado, state='disabled').place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Buscar" ,command=self.mostrar, font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self, text="Eliminar" ,command=self.elimnar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        
    def mostrar(self):
        pos = -1
        
        codigo=self.tk_codigo.get()

        for dato in cursos:
            
            if codigo==dato.getCodigo():
                pos = cursos.index(dato)
        
        if pos==-1:
            titulo = "Buscar Curso"
            mensaje = 'No se ha encontrado el curso'
            messagebox.showerror(titulo, mensaje)
            self.tk_codigo.set('')
            
            
        else:
            self.tk_nombre.set(cursos[pos].getNombre())
            self.tk_codigo.set(cursos[pos].getCodigo())
            
            self.tk_prerrequisitos.set(cursos[pos].getPrerrequisitos())
            self.tk_obligatorio.set(cursos[pos].getObligatorio())
            self.tk_semeste.set(cursos[pos].getSemestre())
            self.tk_creditos.set(cursos[pos].getCreditos())
            self.tk_estado.set(cursos[pos].getEstado())

    def elimnar(self):
        pos = -1
        
        codigo=self.tk_codigo.get()

        for dato in cursos:
            # print(dato.getCodigo())
            if codigo==dato.getCodigo():
                pos = cursos.index(dato)
        if pos!=-1:
            cursos.pop(pos)
            titulo = "Eliminar Curso"
            mensaje = 'Se ha eliminado el curso'
            messagebox.showinfo(titulo, mensaje)
            self.tk_codigo.set('')
            self.tk_nombre.set('')
            self.tk_prerrequisitos.set('')
            self.tk_obligatorio.set('')
            self.tk_semeste.set('')
            self.tk_creditos.set('')
            self.tk_estado.set('')
        else:
            titulo = "Buscar Curso"
            mensaje = 'No se ha encontrado el curso'
            messagebox.showerror(titulo, mensaje)


    def regresar(self):
         self.root.destroy()
         ventana_gestionar_cursos()
    
# Ventana Editar Curso

def ventana_editar_curso():
    root= tk.Tk()
    root.title('Editar Curso')
    root.geometry('900x700+500+100')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = EditarCurso(root = root)
    
    app.mainloop()



class EditarCurso(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=700)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()
        self.deshabilitar()

    
    def Ventana(self):
        Label(self, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        

        self.tk_codigo =tk.StringVar()
        self.tk_nombre =tk.StringVar()
        self.tk_prerrequisitos =tk.StringVar()
        self.tk_obligatorio =tk.StringVar()
        self.tk_semeste =tk.StringVar()
        self.tk_creditos =tk.StringVar()
        self.tk_estado=tk.StringVar()

        self.codigo= ttk.Entry(self,textvariable=self.tk_codigo)
        self.codigo.place(x=325,y=50, width=200,height=35)
        self.nombre= ttk.Entry(self,textvariable=self.tk_nombre)
        self.nombre.place(x=325,y=120, width=500,height=35)
        self.prerrequisito= ttk.Entry(self,textvariable=self.tk_prerrequisitos)
        self.prerrequisito.place(x=325,y=190, width=500,height=35)
        self.obligatorio= ttk.Entry(self,textvariable=self.tk_obligatorio)
        self.obligatorio.place(x=325,y=260, width=500,height=35)
        self.semestre= ttk.Entry(self,textvariable=self.tk_semeste)
        self.semestre.place(x=325,y=330, width=500,height=35)
        self.creditos= ttk.Entry(self,textvariable=self.tk_creditos)
        self.creditos.place(x=325,y=400, width=500,height=35)
        self.estado= ttk.Entry(self,textvariable=self.tk_estado)
        self.estado.place(x=325,y=470, width=500,height=35)
        


       

        Button(self, text="Buscar" ,command=self.buscar, font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self, text="Editar" ,command=self.editar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        
    def buscar(self):
        pos = -1
        
        codigo=self.tk_codigo.get()

        for dato in cursos:
           
            if codigo==dato.getCodigo():
                pos = cursos.index(dato)
        
        if pos==-1:
            titulo = "Buscar Curso"
            mensaje = 'No se ha encontrado el curso'
            messagebox.showerror(titulo, mensaje)
            self.tk_codigo.set('')
            
            
        else:
            
            
            self.tk_nombre.set(cursos[pos].getNombre())
            self.tk_codigo.set(cursos[pos].getCodigo())
            self.tk_prerrequisitos.set(cursos[pos].getPrerrequisitos())
            self.tk_obligatorio.set(cursos[pos].getObligatorio())
            self.tk_semeste.set(cursos[pos].getSemestre())
            self.tk_creditos.set(cursos[pos].getCreditos())
            self.tk_estado.set(cursos[pos].getEstado())

            self.nombre.config(state='normal')
            self.prerrequisito.config(state='normal')
            self.obligatorio.config(state='normal')
            self.semestre.config(state='normal')
            self.creditos.config(state='normal')
            self.estado.config(state='normal')


    def editar(self):
        pos = -1
        
        codigo=self.tk_codigo.get()

        for dato in cursos:
           
            if codigo==dato.getCodigo():
                pos = cursos.index(dato)
        
        if pos==-1:
            titulo = "Editar Curso"
            mensaje = 'No se ha encontrado el curso'
            messagebox.showerror(titulo, mensaje)
            self.tk_codigo.set('')
            
            
        else:
            cursos[pos].setNombre(self.tk_nombre.get())
            cursos[pos].setPrerrequisitos(self.tk_prerrequisitos.get())
            cursos[pos].setObligatorio(self.tk_obligatorio.get())
            cursos[pos].setSemestre(self.tk_semeste.get())
            cursos[pos].setCreditos(self.tk_creditos.get())
            cursos[pos].setEstado(self.tk_estado.get())
            
            self.tk_nombre.set('')
            self.tk_codigo.set('')
            self.tk_prerrequisitos.set('')
            self.tk_obligatorio.set('')
            self.tk_semeste.set('')
            self.tk_creditos.set('')
            self.tk_estado.set('')      
            self.deshabilitar()
            titulo = "Editar Curso"
            mensaje = 'Se ha editado el curso'
            messagebox.showinfo(titulo, mensaje)




    def deshabilitar(self):
        self.nombre.configure(state='disabled')
        self.prerrequisito.configure(state='disabled')
        self.obligatorio.configure(state='disabled')
        self.semestre.configure(state='disabled')
        self.creditos.configure(state='disabled')
        self.estado.configure(state='disabled')
            
    
    
    def regresar(self):
         self.root.destroy()
         ventana_gestionar_cursos()

#   Ventana Listar Cursos
def ventana_listar_cursos():
    root= tk.Tk()
    root.title('Listar Cursos')
    root.geometry('+400+250')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = ListarCurso(root = root)
    
    app.mainloop()



class ListarCurso(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1400, height=600)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()



    def Ventana(self):
        
        
        tabla = ttk.Treeview(self, columns=('#0','#1','#2','#3','#4','#5'), height=13)

        style = ttk.Style()
        style.configure(
            'Treeview',
            background = '#e6ceff',
            foreground = 'black',
            rowheight = 25,
            fielbackground = '#e6ceff'
        )
        style.map(
            'Treeview',
            background = [('selected', '#6746c3')]
        )
        tabla.grid(row=0, column=0, columnspan=3)
        scroll =ttk.Scrollbar(self,   orient = 'vertica', command= tabla.yview)
        scroll.grid(row =0, column=6, sticky='nse')
        tabla.configure(yscrollcommand=scroll.set)

        
        tabla.column('#0', width = 110, anchor=CENTER)
        tabla.column('#1', width = 240, anchor = CENTER)
        tabla.column('#2', width = 170, anchor = CENTER)
        tabla.column('#3', width = 120, anchor = CENTER)
        tabla.column('#4', width = 120, anchor = CENTER)
        tabla.column('#5', width = 120, anchor = CENTER)
        tabla.column('#6', width = 120, anchor = CENTER)

       

        tabla.heading('#0',text='Código')
        tabla.heading('#1',text='Nombre')   
        tabla.heading('#2',text='Prerrequisitos')
        tabla.heading('#3',text='Obligatorio')
        tabla.heading('#4',text='Semestre')
        tabla.heading('#5',text='Créditos')
        tabla.heading('#6',text='Estado')
        ## AQUI SE MANDA A LLAMAR A LA FUNCION QUE NOS DEVUELVE TODOS LOS CURSOS
        for dato in cursos:
            tabla.insert("",END, text=dato.getCodigo(), values=(dato.getNombre(),dato.getPrerrequisitos(),
            dato.getObligatorio(),dato.getSemestre(),dato.getCreditos(),dato.getEstado()))
        
        

        boton_salir = tk.Button(self,text="Regresar" ,command=self.regresar)
        boton_salir.config(width=20, font=('Arial', 12,"bold"), fg= "#000000", bg='#c7cc00',cursor='hand2')
        boton_salir.grid(row=4, column=2,padx=10, pady=10)
        
            
    def regresar(self):
         self.root.destroy()
         ventana_gestionar_cursos()


# Ventana Conteo de Creditos
def ventana_conteo_creditos():
    root= tk.Tk()
    root.title('Conteo de Creditos')
    root.geometry('800x850+500+90')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = ConteoCreditos(root = root)
    
    
    app.mainloop()



class ConteoCreditos(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=800, height=850)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()

    
    def Ventana(self):
        Label(self, text="Créditos aprobados:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Créditos cursando:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Créditos pendientes:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Créditos aprobados:", font=('Times New Roman',15), fg='white', bg='#294d40', width=15).place(x=80, y=540)
        Label(self, text="Créditos asignados:", font=('Times New Roman',15), fg='white', bg='#294d40', width=15).place(x=80, y=590)
        Label(self, text="Créditos pendientes:", font=('Times New Roman',15), fg='white', bg='#294d40', width=15).place(x=80, y=640)
        Label(self, text="Créditos hasta semestre N:", font=('Times New Roman',15), fg='white', bg='#00251a', width=25).place(x=80, y=280)
        Label(self, text="Créditos del semestre:", font=('Times New Roman',15), fg='white', bg='#00251a', width=20).place(x=260, y=430)
        Label(self, text="Semestre:", font=('Times New Roman',15), fg='white', bg='#54afdc', width=10).place(x=80, y=340)
        Label(self, text="Semestre:", font=('Times New Roman',15), fg='white', bg='#54afdc', width=10).place(x=80, y=490)
        
        
        self.creditos_aprobados = tk.StringVar()
        self.funcion_creditos_aprobados()
        self.label_aprobados = tk.Label(self, textvariable=self.creditos_aprobados,state='disabled')
        self.label_aprobados.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_aprobados.place(x=325,y=50)

        self.creditos_cursando = tk.StringVar()
        self.funcion_creditos_cursando()
        self.label_cursando = tk.Label(self, textvariable=self.creditos_cursando,state='disabled')
        self.label_cursando.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_cursando.place(x=325,y=120)

        self.creditos_pendientes = tk.StringVar()
        self.funcion_creditos_pendientes()
        self.label_pendiente = tk.Label(self, textvariable=self.creditos_pendientes,state='disabled')
        self.label_pendiente.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_pendiente.place(x=325,y=190)

        self.Str_creditos_hasta = tk.StringVar()
        self.Str_creditos_hasta .set('0')
        self.label_creditos_hasta = tk.Label(self, textvariable=self.Str_creditos_hasta,state='disabled')
        self.label_creditos_hasta.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_creditos_hasta.place(x=500,y=280)


        self.creditos_aprobados2 = tk.StringVar()
        self.creditos_aprobados2.set("0 ")
        self.label_aprobados2 = tk.Label(self, textvariable=self.creditos_aprobados2,state='disabled')
        self.label_aprobados2.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_aprobados2.place(x=325,y=540)

        self.creditos_cursando2 = tk.StringVar()
        self.creditos_cursando2.set("0 ")
        self.label_cursando2 = tk.Label(self, textvariable=self.creditos_cursando2,state='disabled')
        self.label_cursando2.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_cursando2.place(x=325,y=590)

        self.creditos_pendientes2 = tk.StringVar()
        self.creditos_pendientes2.set("0 ")
        self.label_pendiente2 = tk.Label(self, textvariable=self.creditos_pendientes2,state='disabled')
        self.label_pendiente2.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        self.label_pendiente2.place(x=325,y=640)

        # self.creditos_del_semestre = tk.StringVar()
        # self.creditos_del_semestre.set("77 ")
        # self.label_cdelsemestre = tk.Label(self, textvariable=self.creditos_del_semestre,state='disabled')
        # self.label_cdelsemestre.config(bg="#a6bdae",font=('Times New Roman',15,'bold'), fg='black')
        # self.label_cdelsemestre.place(x=500,y=430)


        self.str_creditos_n=tk.StringVar()
        self.creditos_hastasemsetre= Spinbox(self, textvariable=self.str_creditos_n, from_=1,to=10,state='readonly',wrap=True)
        self.creditos_hastasemsetre.configure(font=('Times New Roman',15),width=10)
        self.creditos_hastasemsetre.place(x=300,y=340)

        self.str_creditos_del_semestre=tk.StringVar()
        self.creditos_delsemsetre= Spinbox(self, textvariable=self.str_creditos_del_semestre, from_=1,to=10,state='readonly',wrap=True)
        self.creditos_delsemsetre.configure(font=('Times New Roman',15),width=10)
        self.creditos_delsemsetre.place(x=300,y=490)
        


        
        Button(self, text="Contar"  ,command=self.funcion_creditos_hastaN, font=('Times New Roman',12), fg='#000000', bg='#14fc1c', width=15, cursor='hand2' ).place(x=500, y=340)
        Button(self, text="Contar"  ,command=self.funcion_creditos_semestre, font=('Times New Roman',12), fg='#000000', bg='#14fc1c', width=15, cursor='hand2' ).place(x=500, y=490)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=17, cursor='hand2' ).place(x=430, y=700)
        
    
    def funcion_creditos_aprobados(self):
        try:
            suma=0
            for dato in cursos:
                if 0==int(dato.getEstado()):

                    suma += int(dato.getCreditos())

            self.creditos_aprobados.set(suma)
        except:
            pass
    
    def funcion_creditos_cursando(self):
        try:
            contador= 0
            suma=0
            for dato in cursos:
                if 1==int(dato.getEstado()):
                    contador = contador + 1
                    suma += int(dato.getCreditos())

            self.creditos_cursando.set(suma)
        except:
            pass
    
    def funcion_creditos_pendientes(self):
        try:
            suma=0
            for dato in cursos:
                if -1==int(dato.getEstado()) and int(dato.getObligatorio())==1:

                    suma += int(dato.getCreditos())

            self.creditos_pendientes.set(suma)
        except:
            pass

    def funcion_creditos_hastaN(self):
        
        try:
            n=self.str_creditos_n.get()

            suma=0
            for dato in cursos:
                if  int(dato.getObligatorio())==1 and int(dato.getSemestre())<=int(n):

                    suma += int(dato.getCreditos())

            self.Str_creditos_hasta.set(suma)
        except:
            pass

    def funcion_creditos_semestre(self):
        
        try:
            semestre=self.str_creditos_del_semestre.get()

            suma_aprobados=0
            suma_pendientes=0
            suma_asignados=0
            for dato in cursos:
                if  int(dato.getEstado())==0 and int(dato.getSemestre())==int(semestre):
                    suma_aprobados += int(dato.getCreditos())
                elif  int(dato.getEstado())==-1 and int(dato.getSemestre())==int(semestre):
                    suma_pendientes += int(dato.getCreditos())
                elif  int(dato.getEstado())==1 and int(dato.getSemestre())==int(semestre):
                    suma_asignados += int(dato.getCreditos()) 

            self.creditos_aprobados2.set(suma_aprobados)
            self.creditos_cursando2.set(suma_asignados)
            self.creditos_pendientes2.set(suma_pendientes)
        except:
            pass

    def regresar(self):
         self.root.destroy()
         ventana_principal()
    
# funcion para colocar icono


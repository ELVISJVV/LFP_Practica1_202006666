from faulthandler import disable
from  tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# Main Screen
class FirstScreen():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Pantalla Principal')
        self.ventana.geometry('700x800+600+120')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    def Ventana(self):
        self.frame = Frame(height=900, width=800)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Lab. Lenguajes Formales y de Programación B+", font=('Times New Roman',13), fg='white', bg='#00251a', width=50).place(x=30, y=50)
        Label(self.frame, text="Elvis Joseph Vásquez Villatoro ", font=('Times New Roman',13), fg='white', bg='#00251a', width=50).place(x=30, y=100)
        Label(self.frame, text="Carné: 202006666 ", font=('Times New Roman',13), fg='white', bg='#00251a', width=50).place(x=30, y=150)
        Button(self.frame, text="Cargar Archivo", command=self.cargar_archivo , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=275)
        Button(self.frame, text="Gestionar Cursos",command=self.ir_gestionar , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=350)
        Button(self.frame, text="Conteo de Créditos" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=425)
        Button(self.frame, text="Salir", command=self.salir , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=180, y=500)
        self.frame.mainloop()
    
    
    def cargar_archivo(self):
        self.ventana.destroy()
        VCargarArchivo()
    def salir(self):
        self.ventana.destroy()
    def ir_gestionar(self):
        self.ventana.destroy()
        GestionarCursos()

# Ventana Cagar Archivo
class VCargarArchivo():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Cargar Archivo')
        self.ventana.geometry('900x400+500+200')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(height=400, width=900)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Ruta", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        
        Button(self.frame, text="Seleccionar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=250)
        Button(self.frame, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=250)
        # Button(self.frame, text="Buscar",  font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=120)
        ingresar_ruta =tk.StringVar()
        ruta= ttk.Entry(self.frame,textvariable=ingresar_ruta).place(x=80,y=120, width=700,height=35)
        
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         FirstScreen()

# Ventana Gestionar Cursos
class GestionarCursos():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Gestionar Cursos')
        self.ventana.geometry('600x600+670+180')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(height=600, width=600)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Button(self.frame, text="Listar Cursos", font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=50)
        Button(self.frame, text="Mostrar Curso" ,command=self.mostrar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=125)
        Button(self.frame, text="Agregar Curso" ,  command=self.agregar_curso ,font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=200)
        Button(self.frame, text="Editar Curso" ,command=self.editar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=275)
        Button(self.frame, text="Eliminar Curso",command=self.eliminar_curso, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=350)
        Button(self.frame, text="Regresar", command=self.regresar , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=425)

        self.frame.mainloop()
    
    
    
    def regresar(self):
        self.ventana.destroy()
        FirstScreen()
    def agregar_curso(self):
        self.ventana.destroy()
        AgregarCurso()
    def mostrar_curso(self):
        self.ventana.destroy()
        MostrarCurso()
    def eliminar_curso(self):
        self.ventana.destroy()
        EliminarCurso()
    def editar_curso(self):
        self.ventana.destroy()
        EditarCurso()


# Ventana agregar curso
class AgregarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Agregar Curso')
        self.ventana.geometry('900x700+500+100')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(width= 900, height=700)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self.frame, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self.frame, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self.frame, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self.frame, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self.frame, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self.frame, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self.frame).place(x=325,y=50, width=500,height=35)
        nombre= ttk.Entry(self.frame).place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self.frame).place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self.frame).place(x=325,y=260, width=500,height=35)
        semestre= ttk.Entry(self.frame).place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self.frame).place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self.frame).place(x=325,y=470, width=500,height=35)
        

        Button(self.frame, text="Agregar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self.frame, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        # Button(self.frame, text="Buscar",  font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=120)
        
        
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         GestionarCursos()
    
#Ventana mostrar Curso
class MostrarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Mostrar Curso')
        self.ventana.geometry('900x700+500+100')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(width= 900, height=700)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self.frame, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self.frame, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self.frame, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self.frame, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self.frame, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self.frame, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self.frame).place(x=325,y=50, width=500,height=35)
        nombre= ttk.Entry(self.frame, state='disabled').place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self.frame, state='disabled').place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self.frame, state='disabled').place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self.frame, state='disabled').place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self.frame, state='disabled').place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self.frame, state='disabled').place(x=325,y=470, width=500,height=35)
        

        Button(self.frame, text="Mostrar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self.frame, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        # Button(self.frame, text="Buscar",  font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=120)
        
        
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         GestionarCursos()

# Ventana Eliminar Curso
class EliminarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Eliminar Curso')
        self.ventana.geometry('900x700+500+100')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(width= 900, height=700)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self.frame, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self.frame, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self.frame, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self.frame, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self.frame, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self.frame, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self.frame).place(x=325,y=50, width=200,height=35)
        nombre= ttk.Entry(self.frame, state='disabled').place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self.frame, state='disabled').place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self.frame, state='disabled').place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self.frame, state='disabled').place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self.frame, state='disabled').place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self.frame, state='disabled').place(x=325,y=470, width=500,height=35)
        

        Button(self.frame, text="Buscar" , font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self.frame, text="Eliminar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self.frame, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        # Button(self.frame, text="Buscar",  font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=120)
        
        
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         GestionarCursos()
    
# Ventana Editar Curso
class EditarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Editar Curso')
        self.ventana.geometry('900x700+500+100')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(width= 900, height=700)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        Label(self.frame, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self.frame, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self.frame, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self.frame, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self.frame, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self.frame, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self.frame, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self.frame).place(x=325,y=50, width=200,height=35)
        nombre= ttk.Entry(self.frame).place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self.frame).place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self.frame).place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self.frame).place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self.frame).place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self.frame).place(x=325,y=470, width=500,height=35)
        

        Button(self.frame, text="Buscar" , font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self.frame, text="Editar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self.frame, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        # Button(self.frame, text="Buscar",  font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=120)
        
        
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         GestionarCursos()
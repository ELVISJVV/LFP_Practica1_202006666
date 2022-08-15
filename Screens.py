
from ast import arg
from runpy import run_path
from  tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as FileDialog
from turtle import width

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
        
        Button(self.frame, text="Buscar", command= self.abrir,font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=639, y=120)
        
        # fichero=FileDialog.askopenfilename()
        ingresar_ruta =tk.StringVar()
        ruta= ttk.Entry(self.frame,textvariable=ingresar_ruta).place(x=80,y=120, width=540,height=35)
        
        
        

        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         FirstScreen()

    def abrir(self):
        Fichero=FileDialog.askopenfilename()
        fichero=Fichero
        self.ruta.set(fichero)


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
        Button(self.frame, text="Listar Cursos",command=self.listar_cursos, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=130, y=50)
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
    def listar_cursos(self):
        self.ventana.destroy()
        ListarCurso()

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

#   Ventana Listar Cursos
class ListarCurso():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False,False)
        self.ventana.title('Listar Cursos')
        self.ventana.geometry('+400+250')
        self.ventana.configure(bg='#20001a')
        self.Ventana()

    

    def Ventana(self):
        self.frame = Frame(width= 1400, height=600)
        self.frame.config(bg='#a6bdae')
        self.frame.pack(padx=25, pady=20)
        
        tabla = ttk.Treeview(self.frame, columns=('#0','#1','#2','#3','#4','#5'), height=13)

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
        scroll =ttk.Scrollbar(self.frame,   orient = 'vertica', command= tabla.yview)
        scroll.grid(row =0, column=6, sticky='nse')
        tabla.configure(yscrollcommand=scroll.set)

        
        tabla.column('#0', width = 150, anchor=CENTER)
        tabla.column('#1', width = 150, anchor = CENTER)
        tabla.column('#2', width = 150, anchor = CENTER)
        tabla.column('#3', width = 150, anchor = CENTER)
        tabla.column('#4', width = 150, anchor = CENTER)
        tabla.column('#5', width = 150, anchor = CENTER)
        tabla.column('#6', width = 150, anchor = CENTER)

       

        tabla.heading('#0',text='Código')
        tabla.heading('#1',text='Nombre')   
        tabla.heading('#2',text='Prerrequisitos')
        tabla.heading('#3',text='Obligatorio')
        tabla.heading('#4',text='Semesttre')
        tabla.heading('#5',text='Créditos')
        tabla.heading('#6',text='Estado')
        ## AQUI SE MANDA A LLAMAR A LA FUNCION QUE NOS DEVUELVE TODOS LOS CURSOS
        
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 1', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))
        tabla.insert("",END, text='Carne 132323', values=('Nombre 1', 'Apellido 1', 'Edad 1','-1','si','Mate'))

        boton_salir = tk.Button(self.frame,text="Regresar" ,command=self.regresar)
        boton_salir.config(width=20, font=('Arial', 12,"bold"), fg= "#000000", bg='#c7cc00',cursor='hand2')
        boton_salir.grid(row=4, column=2,padx=10, pady=10)
        


        self.frame.mainloop()
    
    def regresar(self):
         self.ventana.destroy()
         GestionarCursos()
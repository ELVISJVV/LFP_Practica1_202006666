
from ast import arg

from  tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as FileDialog


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
        
        Button(self, text="Seleccionar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=250)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=250)
        
        Button(self, text="Buscar", command= lambda: ingresar_ruta.set(self.abrir()),font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=639, y=120)
        
        
        ingresar_ruta =tk.StringVar()
        ruta= ttk.Entry(self,textvariable=ingresar_ruta).place(x=80,y=120, width=540,height=35)

    def regresar(self):
        self.root.destroy()
        ventana_principal()
        
    
    def abrir(*args):
        Fichero=FileDialog.askopenfilename(title="Selecciona el archivo")
        a=Fichero
        print(a)
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
        
        codigo= ttk.Entry(self).place(x=325,y=50, width=500,height=35)
        nombre= ttk.Entry(self).place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self).place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self).place(x=325,y=260, width=500,height=35)
        semestre= ttk.Entry(self).place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self).place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self).place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Agregar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        
        


        
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
        
        codigo= ttk.Entry(self).place(x=325,y=50, width=500,height=35)
        nombre= ttk.Entry(self, state='disabled').place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self, state='disabled').place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self, state='disabled').place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self, state='disabled').place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self, state='disabled').place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self, state='disabled').place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Mostrar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
       
    
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
        
        codigo= ttk.Entry(self).place(x=325,y=50, width=200,height=35)
        nombre= ttk.Entry(self, state='disabled').place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self, state='disabled').place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self, state='disabled').place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self, state='disabled').place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self, state='disabled').place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self, state='disabled').place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Buscar" , font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self, text="Eliminar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        
    
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

    
    def Ventana(self):
        Label(self, text="Código", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Prerrequisitos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Obligatorio", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self).place(x=325,y=50, width=200,height=35)
        nombre= ttk.Entry(self).place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self).place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self).place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self).place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self).place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self).place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Buscar" , font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self, text="Editar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        

    
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
    root.geometry('900x700+500+100')
    root.configure(bg='#20001a')
    root.resizable(0,0)
    app = ConteoCreditos(root = root)
    
    app.mainloop()



class ConteoCreditos(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=900, height=700)
        self.root = root
        self.pack()
        self.config( bg='#a6bdae')
        self.pack(padx=25,pady=20)
        self.Ventana()

    
    def Ventana(self):
        Label(self, text="Créditos aprobados:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=50)
        Label(self, text="Nombre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=120)
        Label(self, text="Créditos cursando:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=190)
        Label(self, text="Créditos pendientes:", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=260)
        Label(self, text="Semestre", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=330)
        Label(self, text="Créditos", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=400)
        Label(self, text="Estado", font=('Times New Roman',15), fg='white', bg='#00251a', width=15).place(x=80, y=470)
        
        codigo= ttk.Entry(self).place(x=325,y=50, width=200,height=35)
        nombre= ttk.Entry(self).place(x=325,y=120, width=500,height=35)
        prerrequisito= ttk.Entry(self).place(x=325,y=190, width=500,height=35)
        obligatorio= ttk.Entry(self).place(x=325,y=260, width=500,height=35)
        
        semestre= ttk.Entry(self).place(x=325,y=330, width=500,height=35)
        creditos= ttk.Entry(self).place(x=325,y=400, width=500,height=35)
        estado= ttk.Entry(self).place(x=325,y=470, width=500,height=35)
        

        Button(self, text="Buscar" , font=('Times New Roman',12), fg='#000000', bg='#c7cc00', width=15, cursor='hand2' ).place(x=600, y=50)
        Button(self, text="Editar" , font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=100, y=550)
        Button(self, text="Regresar",  command = self.regresar, font=('Times New Roman',15), fg='#000000', bg='#c7cc00', width=20, cursor='hand2' ).place(x=500, y=550)
        

    
    def regresar(self):
         self.root.destroy()
         ventana_principal()

ventana_principal()

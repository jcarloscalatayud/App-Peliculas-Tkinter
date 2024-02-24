import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    
    menu_inicio.add_command(label='Crear Registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)   
    # Agregamos los otros menus
    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    
    menu_consultas.add_command(label='Por genero')
    
    barra_menu.add_cascade(label='Configuracion')
    
    # Agregamos opcion ayuda al menu principal
    menu_ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)
    
    menu_ayuda.add_command(label='Acerca de...')
    

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg='Tan')
        # A continuacion se define id_pelicula para el boton editar
        self.id_pelicula = None
    
        
        # Construimos los lebel
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'), bg='Tan')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'), bg='Tan')
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font=('Arial', 12, 'bold'), bg='Tan')
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        
        # Definimos los textbox o entry
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
        
        # Definimos botones
        self.boton_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),fg='#DAD5D6', bg='#158645', cursor='hand2',
                                activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)
        
        # Boton Guardar
        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),fg='#DAD5D6', bg='#1658A2', cursor='hand2',
                                activebackground='#3586DF')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)
        
        # Boton Cancelar
        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),fg='#DAD5D6', bg='#BD152E', cursor='hand2',
                                activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
        
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
    
    def deshabilitar_campos(self):
        self.id_pelicula = None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')    
        
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        
    def guardar_datos(self):
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()
        )
        
        # Condicion si el guardar es con id o sin id de pelicula
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)
            
        self.tabla_peliculas() # actualiza la grilla 
        
        self.deshabilitar_campos()
        
    def tabla_peliculas(self):
        # Recuperar la lista de peliculas
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')
        
        # Scrollbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical',
                                    command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')
        
        # Insertar la lista en la grilla
        for p in self.lista_peliculas:
            self.tabla.insert('',0,text=p[0], values=(p[1], p[2], p[3]))
        
        # Botones debajo de la tabla
        # Boton Editar
        self.boton_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#158645',
                                 cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)
        
        # Boton Eliminar
        self.boton_eliminar = tk.Button(self, text='Eliminar', command=self.elimnar_datos)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg='#BD152E',
                                   cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
        
    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            
            # Habilitamos campos
            self.habilitar_campos()
            
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
            
    def elimnar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            
            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            titulo = 'Eliminar un Registro'
            mensaje = 'Na ha seleccionado registro'
            messagebox.showerror(titulo, mensaje)
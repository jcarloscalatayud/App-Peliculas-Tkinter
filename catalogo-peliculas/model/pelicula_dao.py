from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
        )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear tabla'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
    
def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar tabla'
        mensaje = 'Se borro la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar tabla'
        mensaje = 'La tabla no existe'
        messagebox.showerror(titulo, mensaje)
        
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self) -> str:
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
def guardar(pelicula):
    conexion = ConexionDB()
    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion a la base de datos'
        mensaje = 'La tabla peliculas no esta creada en la base de datos.'
        messagebox.showerror(titulo, mensaje)
        
def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'
    try: 
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion a la tabla de datos'
        mensaje = 'Crear la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
        
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas
    SET nombre='{pelicula.nombre}', duracion='{pelicula.duracion}',
    genero='{pelicula.genero}'
    WHERE id_pelicula='{id_pelicula}'
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se pudo editar este registro'
        messagebox.showerror(titulo, mensaje)
        
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
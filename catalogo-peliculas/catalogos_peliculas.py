import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0) # El tamaño se adaptara al frame
    
    barra_menu(root)
   
    
    app = Frame(root=root)
    # Creacion de frame
    #frame = tk.Frame(root)
    #frame.pack()
    #frame.config(width=480, height=320, bg='Tan')
    #root.mainloop() # siempre al final
    app.mainloop()
    
if __name__ == '__main__':
    main()
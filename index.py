from cProfile import label
from cgitb import text
import this
from tkinter import ttk
from tkinter import *

import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window 
        self.wind.title("product application")

        #how to create a frame container
        frame = LabelFrame(self.wind, text = 'Registre un nuevo empleado ')
        frame.grid(row = 0, column= 0, columnspan = 3, pady = 20)

        #name input
        Label(frame, text= 'Nombres: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid( row = 1, column = 1)

        #lastname input
        Label(frame, text= 'Apellidos: ').grid(row = 2, column = 0)
        self.lastname = Entry(frame)
        self.lastname.grid( row = 2, column = 1)

        #Identification document input
        Label(frame, text= 'Documento de identificacion: ').grid(row = 3, column = 0)
        self.lastname = Entry(frame)
        self.lastname.grid( row = 3, column = 1)

        #days input
        Label(frame, text= 'Dias trabajados: ').grid(row = 4, column = 0)
        self.days = Entry(frame)
        self.days.grid( row = 4, column = 1)

        #salary input
        Label(frame, text= 'Salario: ').grid(row = 5, column = 0)
        self.salary = Entry(frame)
        self.salary.grid( row = 5, column = 1)

        #ExtraHour input
        Label(frame, text= 'Horas extra laboradas: ').grid(row = 6, column = 0)
        self.hour = Entry(frame)
        self.hour.grid( row = 6, column = 1)

        #Button add employee
        ttk.Button(frame, text = 'Guardar empleado').grid(row=7, columnspan=2, column=0, sticky=W + E)

        # table
        self.tree = ttk.Treeview(height=10, columns= ('#0','#1','#2','#3','#4','#5''#6'))
        self.tree.grid(row= 9, column=0, columnspan=2)
        self.tree.heading('#0', text='Id', anchor= CENTER)
        self.tree.heading('#1', text='Nombres', anchor= CENTER)
        self.tree.heading('#2', text='Apellidos', anchor= CENTER)
        self.tree.heading('#3', text='Documento de identificacion', anchor= CENTER)
        self.tree.heading('#4', text='Dias trabajados', anchor= CENTER)
        self.tree.heading('#5', text='Salario', anchor= CENTER)
        self.tree.heading('#6', text='Horas extra', anchor= CENTER)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db.name) as conn:
            cursor = conn.cursor(
            cursor.execute(query, parameters)
            ) 





if __name__ == '__main__':
    Window = Tk()
    application = Product(Window)
    Window.mainloop()
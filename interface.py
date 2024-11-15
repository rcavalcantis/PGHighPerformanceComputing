import tkinter
from tkinter import Label

principal = tkinter.Tk()

etiqueta = Label(principal, text='Etiqueta: ')
etiqueta.grid(row=0, column=0)

entrada = tkinter.Entry(principal)
entrada.grid(row=0, column=1)

botao = tkinter.Button(principal, text='OK')
botao.grid(row=0, column=2)

principal.mainloop()
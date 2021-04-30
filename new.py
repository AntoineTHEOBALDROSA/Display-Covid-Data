from tkinter import * 
from PIL import ImageTk, Image
import os
import tkinter as tk
import time

def afficherGraphiqueTkinter():
    img = PhotoImage(file="test2.png")
    canvas = Canvas(root, width=500, height=500)
    canvas.create_image(500, 500, image=img)
    canvas.grid(row=4,column=0)


root = Tk()

root.geometry("720x480")

debutLabel = Label(root, text="Date début (ex : 2021-01-01)")
finLabel = Label(root, text="Date fin (ex : 2021-04-24)")
departementLabel = Label(root, text="Département (ex : 57)")

entryDebut = Entry(root, width=30)
entryFin = Entry(root, width=30)
entryDepartement = Entry(root, width=30)

validerButton = Button(root, text=('Valider'),command=afficherGraphiqueTkinter)
quitterButton = Button(root, text='Quitter', command=root.destroy)

debutLabel.grid(row=0, column=0, padx=(20, 0))
finLabel.grid(row=1, column=0, padx=(20, 0))
departementLabel.grid(row=2, column=0, padx=(20, 0))
entryDebut.grid(row=0, column=1, padx=(40, 0))
entryFin.grid(row=1, column=1, padx=(40, 0))
entryDepartement.grid(row=2, column=1,padx=(40, 0))
validerButton.grid(row=3, column=1, padx=(40, 0))
quitterButton.grid(row=3, column=0, padx=(20, 0))

graphiqueImageOpened = ImageTk.PhotoImage(Image.open("test.png"))
labelImageGraphique = Label(image=graphiqueImageOpened)
labelImageGraphique.grid(row=4,column=0,padx=100,columnspan=2)

root.mainloop()
# Partie 5) Reprise de la question 1 de la partie 4
from tkinter import * 
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import random
import os

# FONCTIONS

def csv2liste(fichiercsv):
    '''
    entrée(s) : fichier .csv
    sortie : liste de liste
    fonction : transforme un fichier .csv en liste de liste.
    La liste principale contient, sous la forme de liste, chaque ligne du fichier .csv
    '''
    csv_file = open(fichiercsv, "r")
    liste=[]
    for ligne in csv_file:
        ligne = ligne.rstrip()
        donnees=ligne.split(';')
        liste.append(donnees)
    csv_file.close()
    return liste

def recupererEntryTkinter():
    '''
    entrée(s):
    sortie: lance la fonction main()
    fonction : récupère le texte des entry tkinter et le lance la fonction principale grâce aux informations récupérées dans les entrées
    '''
    dateDebutEntree = entryDebut.get()
    dateFinEntree = entryFin.get()
    dateDepartementEntree = entryDepartement.get()
    # lance la fonction principale
    main(dateDepartementEntree,dateDebutEntree,dateFinEntree)

def recupererDonnesDansCSV(departement,debut,fin):
    '''
    entrée(s): département, date de début, date de fin -> chaine de caractère
    sortie: graphique via matplotlib, et si l'utilisateur le choisit, un fichier au formant jpg du graphique
    fonction : récupère dans un fichier csv, via les informations d'entrée de la fonction, le nombre de dose 1 et 2 administrées dans tel département entre tel et tel date
    '''
    
    fichierLocal = csv2liste(os.path.join('fichiers .csv',"vacsi-a-dep-2021-04-25-19h10.csv"))[1:]
    global dateDose,nbVaccinesDose1,nbVaccinesDose2,departementGlobal,debutGlobal,finGlobal
    dateDose = []
    nbVaccinesDose1 = []
    nbVaccinesDose2 = []
    suisJeDansLintervalleDeTemps = 0
    departementGlobal = departement
    debutGlobal = debut
    finGlobal = fin
 
    for ligne in fichierLocal:
        if ligne[1] == "0" and ligne[0] == departement:
            if ligne[2] == debut:
                suisJeDansLintervalleDeTemps = 1
            
            if suisJeDansLintervalleDeTemps == 1:
                dateDose.append(ligne[2])
                nbVaccinesDose1.append(int(ligne[-2]))
                nbVaccinesDose2.append(int(ligne[-1]))
            
            if ligne[2] == fin:
                suisJeDansLintervalleDeTemps = 0
 
    return dateDose,nbVaccinesDose1,nbVaccinesDose2
 
def genererImage(listeDate, listeVaccinDose1, listeVaccinDose2):
    '''
    entrée(s): listeDate,listeVaccinDose1,listeVaccinDose2 -> liste
    sortie: graphiqur matplotlib
    fonction : transforme une liste de données en graphique (via le module matplotlib)
    '''
    global randomFileName
    randomFileName = str(random.randint(1,2**20))
 
    plt.figure()
    plt.plot(listeDate, listeVaccinDose1, label="Dose 1")
    plt.plot(dateDose, listeVaccinDose2, label="Dose 2")
    plt.title(f'nombre de vaccinés\ndepartement {departementGlobal} du {debutGlobal} au {finGlobal}')
    plt.legend()
    plt.savefig(os.path.join("imageMatPlotLib",randomFileName))
 
def afficherGraphiqueTkinter(randomFileName):
    '''
    entrée(s): randomFileName -> chaine de caractere
    sortie: 
    fonction : affiche le nouveau graphique sur la fenetre tkinter
    '''
    graphiqueImageOpened = Image.open(os.path.join("imageMatPlotLib",randomFileName+".png"))
    render = ImageTk.PhotoImage(graphiqueImageOpened)
    labelImageGraphique = Label(root, image=render)
    labelImageGraphique.image = render
    labelImageGraphique.grid_forget()
    labelImageGraphique.grid(row=4,column=0,padx=100,columnspan=2)

def main(departement,debut,fin):
    '''
    entrée(s): departement, debut, fin -> chaine de caractere
    sortie: fenetre tkinter qui est mise à jour
    fonction : transforme un departement, une date de debut et une date de fin en graphique qui apparaît sur matplotlib
    en gros c'est la fonction principale 
    '''
    recupererDonnesDansCSV(departement,debut,fin)
    genererImage(dateDose, nbVaccinesDose1, nbVaccinesDose2)
    afficherGraphiqueTkinter(randomFileName)
    return 


# FENETRE TKINTER

root = Tk()

root.geometry("720x480")

debutLabel = Label(root, text="Date début (ex : 2021-01-01)")
finLabel = Label(root, text="Date fin (ex : 2021-04-24)")
departementLabel = Label(root, text="Département (ex : 57)")

entryDebut = Entry(root, width=30)
entryFin = Entry(root, width=30)
entryDepartement = Entry(root, width=30)

validerButton = Button(root, text='Valider',command=recupererEntryTkinter)
quitterButton = Button(root, text='Quitter', command=root.destroy)

debutLabel.grid(row=0, column=0, padx=(20, 0))
finLabel.grid(row=1, column=0, padx=(20, 0))
departementLabel.grid(row=2, column=0, padx=(20, 0))
entryDebut.grid(row=0, column=1, padx=(40, 0))
entryFin.grid(row=1, column=1, padx=(40, 0))
entryDepartement.grid(row=2, column=1,padx=(40, 0))
validerButton.grid(row=3, column=1, padx=(40, 0))
quitterButton.grid(row=3, column=0, padx=(20, 0))


entryDebut.insert(0,"2021-01-01")
entryFin.insert(0,"2021-04-24")
entryDepartement.insert(0,"57")

root.mainloop()
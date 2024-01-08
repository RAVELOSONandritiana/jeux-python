from tkinter import *
from tkinter import filedialog
import os
def parcourir_fichier():
	texte = "RIP"
	fichier = filedialog.asksaveasfile(mode="w",defaultextension=".txt")

def recuperation():
	chemin_obtenu = chemin.get()
	extension_obtenu = ext.get()
	cpt = extension_obtenu.count(".")
	if cpt == 0 and len(extension_obtenu)>0:
		extension_obtenu = "."+extension_obtenu
	if len(extension_obtenu)==0:
		extension_obtenu=".RIP"
	liste_fichier = os.listdir(chemin_obtenu)
	for fichier in liste_fichier:
		old_name = os.path.join(chemin_obtenu,fichier)
		name_modify = old_name+extension_obtenu
		new_name = os.path.join(name_modify)
		os.rename(old_name,new_name)
def depannage():
	chemin_obtenu = chemin.get()
	extension_obtenu = ext.get()
	if len(extension_obtenu)==0:extension_obtenu="RIP"
	liste_fichier = os.listdir(chemin_obtenu)
	for fichier in liste_fichier:
		old_name = os.path.join(chemin_obtenu,fichier)
		name_modify = fichier.replace(extension_obtenu,"")
		new_name = os.path.join(chemin_obtenu,name_modify)
		os.rename(old_name,new_name)
def appel_destructeur():
	recuperation()
def appel_constructeur():
	depannage()
def appel_destructeur_clavier(event):
	recuperation()
def appel_constructeur_clavier(event):
	depannage()

fen = Tk()
fen.geometry("400x400")
fen.title("hgb virus")
fen.resizable(False,False)
menuBar = Menu(fen)
menuFichier = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="options",menu=menuFichier)
menuFichier.add_command(label="parcourir",command=parcourir_fichier)
menuFichier.add_command(label="quitter",command=fen.destroy)
#############################################
# Chargement des images pour les background #
#############################################
image_font = PhotoImage(file = "photos/logo.png")
image_font = image_font.subsample(5)
can = Canvas(fen,height=400,width=400,bg="grey")
can.pack()

des = can.create_text(340,100,text="bgh",font=("arial",50))
mas = can.create_text(60,100,text="hgb",font=("arial",50))
im = can.create_image(200,100,image=image_font)

can2 = Canvas(can,height=200,width=400,bg="black")
can2.place(x=0,y=200)

txt_part = can2.create_text(120,50,text="Repertoire : ",fill="green",font=("Helvetica",20,"italic"))
chemin = Entry(can2,font=("Helvetica",12,"italic"),width=19)
chemin.place(x=210,y=42)

txt_extension = can2.create_text(120,100,text="Extension : ",fill="green",font=("Helvetica",20,"italic"))
ext = Entry(can2,font=("Helvetica",12,"italic"),width=19)
ext.place(x=210,y=88)

but_destruction = Button(can2,text="Detruire",bg="red",fg="blue",font=("Helvetica",15),width=15,command=appel_destructeur)
but_restauration = Button(can2,text="Depanner",bg="green",fg="blue",font=("Helvetica",15),width=15,command=appel_constructeur)

but_destruction.place(x=20,y=150)
but_restauration.place(x=210,y=150)
can.bind_all("<Up>",appel_destructeur_clavier)
can.bind_all("<Down>",appel_constructeur_clavier)


fen.config(menu=menuBar)
fen.mainloop()

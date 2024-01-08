from tkinter import *
from tkinter import filedialog
import os
def prompt():
	chaine = "cmd"
	os.system(chaine)
def save_file():
	chaineEntier = txt.get("1.0",END)
	fichier = filedialog.asksaveasfile(mode="w",defaultextension=".py")
	if fichier is not None:
		fichier.write(chaineEntier)
		fichier.close()
fen = Tk()
fen.geometry("600x600")
fen.title("IDE Python")
menuBar = Menu(fen)
menuFichier = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="fichier",menu = menuFichier)
menuFichier.add_command(label="new file")
menuFichier.add_command(label="save",command=save_file)
menuFichier.add_command(label="run treminal",command=prompt)
menuQuitter = Menu(menuBar,tearoff=1)
menuBar.add_cascade(label="quitter",menu = menuQuitter)
menuQuitter.add_cascade(label="quitter",command=fen.destroy)

can = Canvas(fen,height=600,width=600,bg="blue")
can.pack(side="left")

txt = Text(can,font=("",10),fg="blue",bg="grey",height=590,width=590)
txt.pack(fill="both",expand=True)
txt.pack(side="left",fill="both",expand=True)
fen.config(menu = menuBar)
fen.mainloop()

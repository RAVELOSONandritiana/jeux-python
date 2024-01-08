from tkinter import *
import subprocess
def creer_battery():
    global color
    percentage = subprocess.check_output(["acpi"])
    charge = str(percentage).split(",")[1].replace("%","").replace("\\n","").replace("\'","")
    action_sur_batterie = str(percentage.split()[2]).replace("\'","").replace("b","").replace(",","")
    couleur_back = "blue"
    if action_sur_batterie == "Charging":
        couleur_back = "green"
    can.create_rectangle(10,10,90,210,fill="grey")
    for i in range(11-int(charge)//10-1,11):
        hauteur = i*20-10
        can.create_rectangle(10,hauteur,90,hauteur+20,fill=couleur_back)
    can.create_text(50,100,text=charge,font=("",15))
    can.after(100,creer_battery)
fen = Tk()
color = ["red","green"]
fen.geometry("100x220")
fen.resizable(False,False)
can = Canvas(fen,height=220,width=100,bg="black")
can.pack()
creer_battery()
fen.mainloop()

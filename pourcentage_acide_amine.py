from collections import *
acide = ["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
acide_simple = set(acide)
l = []
for i in acide_simple:
    nb = acide.count(i)
    l.append([i,nb])
taille = len(acide)
for i in l:
    print(i[0],(i[1]*100)/taille,sep=" : ")
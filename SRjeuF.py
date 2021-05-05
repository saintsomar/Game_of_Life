from tkinter import *
import random
import copy
import time


#Creating Tkinter interface
WindowConf="950x800"
root = Tk()
root.title("SR01_Jeu_de_la_vie:_Florent/Ramos")
root.geometry(WindowConf)
root.resizable(0,0)

#creating grid (canvas)
game = Canvas(root, bg="white", height=800,width=800)
game.pack(side=LEFT)
game.pack()

#creating control frame
controlframe=Frame(root, bg='grey85')
controlframe.pack(side=RIGHT, fill=Y)
#exit button
sortir= Button(controlframe,fg='steelblue' , text= "Quitter", command= root.destroy,font='Helvetica')
sortir.pack(side = BOTTOM, fill = X)
#control slides vitesse
timescale = Scale(controlframe, from_ = 1, to = 100, orient = HORIZONTAL, label='Vitesse',
                  fg='steelblue')
timescale.pack(side=BOTTOM, fill = X, padx=15)
timescale.set(5)
#control slide %vie
lifescale = Scale(controlframe, from_ = 1, to =100 , orient = HORIZONTAL, label ='% de vie',
                  fg='steelblue')
lifescale.pack(side=BOTTOM, fill = X, padx=15)
lifescale.set(20)
#control slide size
gridsize = Scale(controlframe, from_ = 1, to =100 , orient = HORIZONTAL, label ='Taille de la grille',
                  fg='steelblue')
gridsize.pack(side=BOTTOM, fill = X, padx=15)
gridsize.set(30)
#-----------------------------------------------------------------------------------------------
#fonctions de lalgorithme
#-----------------------------------------------------------------------------------------------
grid_value=gridsize.get()
# M =30x30 cells by default
M = [[0]*grid_value]*grid_value
flag = 0

def nb_voisin(M, i, j):
    nb_voisin = 0
    for k in range(i-1, i+2, 1):
        if M[(k+grid_value)%(grid_value)][(j-1+grid_value)%grid_value] != 0:
            nb_voisin += 1
        if M[(k+grid_value)%(grid_value)][(j+1)%grid_value] != 0:
            nb_voisin += 1
        if ((k+grid_value)%grid_value) != i:
            if M[(k+grid_value)%grid_value][j] != 0:
                nb_voisin += 1
    return nb_voisin

def jeu_de_vie():
    global M
    N=copy.deepcopy(M)
    voisin = 0
    for i in range(grid_value):
        for j in range(grid_value):
            voisin = nb_voisin(M, i, j)
            if (voisin < 2 or voisin > 3) and N[i][j]:
                N[i][j] = 0
            elif voisin == 3 and not N[i][j]:
                N[i][j] = 1
    M = copy.deepcopy(N)


def afficher():
    x=0
    y=0
    global grid_value
    for i in range(grid_value):
        for j in range(grid_value):
            if (M[i][j]==1):
                couleur = "red"
            else:
                couleur = "white"
            rectanglecan = game.create_rectangle(x, y, x+(800/grid_value), y+(800/grid_value), width=1, fill=couleur)
            x=x+(800/grid_value)
        x=0
        y=y+(800/grid_value)

def simulate():
    global flag
    vit=1010-(timescale.get()*10)
    if flag ==1:
        game.delete("all")
        jeu_de_vie()
        afficher()
        game.after(vit, simulate)

def onstart():
    global flag
    flag = 1
    simulate()

def onstop():
    global flag
    flag = 0

def onlaunch():
    global M
    global grid_value
    game.delete("all")
    grid_value=gridsize.get()
    life_value=(grid_value*grid_value)*int(lifescale.get())*0.01
    counter=0
    M = [[0 for j in range(grid_value)] for i in range(grid_value)]
    for i in range(grid_value):
        for j in range(grid_value):
            if counter >= life_value:
                break
            M[i][j] = random.randint(0,1)
            if M[i][j]:
                counter+=1

    afficher()

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#control buttons
start= Button(controlframe, fg='steelblue', text= "Lancer", command= onstart ,font='Helvetica', width=15)
start.pack(side = TOP, fill = X)
stop= Button(controlframe, fg='steelblue', text= "Arreter", command= onstop, font='Helvetica')
stop.pack(side = TOP, fill = X)
launch= Button(controlframe,fg='steelblue' , text= "Initialiser", command=onlaunch,font='Helvetica')
launch.pack(side = TOP, fill = X)
if 1: print("si")
afficher()
root.mainloop()

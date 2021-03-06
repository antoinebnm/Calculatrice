# TK_SILENCE_DEPRECATION : supprimer le message d'erreur
TK_SILENCE_DEPRECATION=1

# Importation des librairies
from tkinter import *
import tkinter.messagebox as alert
from math import *

# Initialisation des variables
numbers = list(range(10))
debug = False
nbrx = ["", "0", "", ""]
index = 2
char_limit = 8


##########################################################
#                                                        #
#                 Fonctions Principales                  #
#                                                        #
##########################################################

# Affichage

def display(mode, num="", ope=""):
    if mode == "get":
        nbrx[3] = result.get()
    elif mode == "set":
        sign.set(str(ope))
        result.set(str(num))
    return nbrx[3]

# Menu

def docs():
    return

def help_keyboard():
    return

def error(msg):
    alert.showerror("Erreur :", msg)
    return

# Boutons Clavier Calculatrice : __main__

def button_pressed(button):
    button_type = "not defined"
    # Test : bouton 'chiffre'
    for selector in numbers:
        if str(selector) == str(button):
            button_type = "number"
            number(button)
    # Test : bouton .
    if button == ".":
        button_type = "point"
        add_point()
    # Test : bouton +, -, x, ÷
    elif button == "+" or button == "-" or button == "x" or button == "÷":
        button_type = "basic-operation"
        operation(button)
    # Test : bouton ±
    elif button == "±":
        print(button)
        button_type = "opposite"
        pm()
    # Test : bouton =
    elif button == "=":
        button_type = "calculate"
        operation(button)
    # Test : bouton √
    elif button == "√":
        button_type = "square root"
        rc()
    # Test : bouton x²
    elif button == "x²":
        button_type = "square"
        car()
    # Test : bouton %
    elif button == "%":
        button_type = "percent"
        percentage()
    # Test : bouton C
    elif button == "C":
        button_type = "clear-all"
        clear()
    # Test : bouton CE
    elif button == "CE":
        button_type = "delete"
        delete()
    # Fin de la fontion
    if debug == True: print("Type of the button pressed : {}".format(button_type))
    return


# Touches Clavier d'ordi : __main__

def key_pressed(key):
    global debug
    global char_limit
    key_type = "not defined"
    # Test : touche 'chiffre'
    for selector in numbers:
        if str(selector) == str(key.char):
            key_type = "number"
            number(key.char)
    if str(key.char) == "c" or str(key.char) == "C":
        key_type = "clear-all"
        clear()
    elif str(key.char) == "@":
        key_type = "dev key"
        if debug == True:
            debug = False
            print("Debug : False")
        else:
            debug = True
            print("Debug : True")
    elif str(key.char) == "i":
        key_type = "dev key"
        if debug == True:
            print(index)
    elif str(key.char) == "l":
        key_type = "dev key"
        print(char_limit)
    # Fin de la fonction
    if debug == True: print("Type of the key pressed : {}".format(key_type))
    return


##########################################################
#                                                        #
#                  Fonctions Appelées                    #
#                                                        #
##########################################################

# number : incrémentation de nombres sur l'écran
def number(button):
    global char_limit
    ope = sign.get()
    input_string = display("get")
    input_list = list(input_string)
    # point detection
    if input_list[0] == "-":
        char_limit = 9
    for selector in input_list:
        if str(selector) == ".":
            if debug == True: print("Point detected : chara limit = 9")
            if input_list[0] == "-":
                char_limit = 10
            else:
                char_limit = 9
    if input_string == "0":
        display("set", button, ope)
    elif int(len(input_list))>=int(char_limit):
        error("Limite de charactère atteinte")
        if debug == True: print("Limite de charactère atteinte")
    else:
        display("set", str(input_string) + str(button), ope)
    input_string = display("get")
    input_list = list(input_string)
    if debug == True: print("input_string="+str(input_string),"\n","input_list="+str(input_list),"\n","len(input_list)="+str(len(input_list)))
    return

# addpoint : ajout d'un point après le dernier chiffre
def add_point():
    global char_limit
    ope = sign.get()
    point_placed = False
    input_string = display("get")
    input_list = list(input_string)
    # point detection
    for selector in input_list:
        if str(selector) == ".":
            error("Un point est déjà placé")
            if debug == True: print("Erreur : un point est déjà placé")
            point_placed = True
    if point_placed != True:
        if len(input_list) == char_limit:
            return
        else:
            display("set", str(input_string) + ".", ope)
    return

# operation : tri des opérations
def operation(button):
    global index
    if index == 1:
        index = 2
    else:
        index = 1
    nbrx[index] = display("get")
    if debug == True: print(nbrx[index],"\n",nbrx[1],"\n",nbrx[2])
    if button == "=":
        ope = sign.get()
        calculate(ope)
        return
    elif button == "+":
        ope = "+"
    elif button == "-":
        ope = "-"
    elif button == "x" or button == "*":
        ope = "*"
    elif button == "÷" or button == "/":
        ope = "/"
    display("set", "0", ope)
    return

# pm(arg) : fonction plus ou moins
def pm():
    display("set", eval(str(display("get")) + "*-1"))
    return

# calculate : calculer
def calculate(ope):
    global index
    if ope != "":
        resultat = eval(str(nbrx[1]) + str(ope) + str(nbrx[2]))
    else:
        resultat = nbrx[2]
        #error_msg = "Nombre ou sign opératoire manquant."
        #error(error_msg)
    ope = ""
    index = 2
    display("set", resultat)
    return

# clear : effacer l'écran
def clear():
    ope = ""
    display("set", "0", ope)
    return

# delete : supprimer le dernier caractère
def delete():
    input_string = display("get")
    input_list = list(input_string)
    display("set", str(list(input_list.pop(-1))))
    return

# car : carré du nombre
def car():
    nbrx[1] = display("get")
    display("set", eval(nbrx[1] + "** 2"))
    return

# rc : racine carrée du nombre
def rc():
    nbrx[1] = display("get")
    #On vérifie que le nombre peut être mis à la racine carré
    if float(nbrx[1])<0.0:
        error("Racine carré d'un nombre négatif impossible !")
    else:
        display("set", sqrt(nbrx[1]))
    return

# percentage : pourcentage du nombre 
def percentage():
    nbrx[1] = display("get")
    display("set", str(nbrx[1])/100)
    return

##########################################################
#                                                        #
#                       Interface                        #
#                                                        #
##########################################################

# Variable pour définir le clavier
## numbers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ; other_actions = ['CE', 'C', '=', 'Rep', '.', '±']
## basic_operations = ['+', '-', '÷', 'x'] ; advanced_operations = ['x²', '√', '%', 'trig'] 
cal_keybord = [["%","√","x²","Rép"],["CE","C","trig","÷"],["7","8","9","x"],["4","5","6","+"],["1","2","3","-"],["±","0",".","="]]

# Création de l'interface (dimensions de la fenêtre, titre, couleur et clavier)
window=Tk()
# Dimensions de la fenêtre
window.geometry("300x400")
window.resizable(width=False, height=False)
window.withdraw()
# Titre
window.title("Calculatrice Équipe BKRS")
# Couleur
#base_color = "#00ffc3"
# Clavier
## Cadre du résultat
frame_result = Frame(window)
frame_result.grid(column = 0,row = 0,sticky=E)
## Résultat
result = StringVar()
lbl_result = Label(frame_result, textvariable=result,font=("Courier", 20))
## Set du résultat à '0'
result.set("0")
lbl_result.grid(column = 0,row = 0,sticky=E)
## Cadre du signe
frame_sign = Frame(window)
frame_sign.grid(column = 0,row = 0,sticky=W)
## Signe
sign = StringVar()
Label(frame_sign, textvariable=sign,font=("Courier", 20)).pack(side=LEFT, padx=10)
## Set du signe à ' '
sign.set("")
## Reste du clavier
frame_padding = Frame(window,height=30)
frame_padding.grid(column = 0,row = 2)
frame_padding = Frame(window,height=30)
frame_padding.grid(column = 0,row = 4)
frame_chiffres = Frame(window)
frame_chiffres.grid(column = 0,row = 5,sticky=S)
lst_btn_cal_keybord = []

# Boucle for : mise en place du clavier
lig = 0
for l in cal_keybord:
    lig_btn_chiffres = []
    col = 0
    for c in l:
        b = Button(frame_chiffres, width=3,text=c,font=("Courier", 20),command=lambda button = c: button_pressed(button))
        lig_btn_chiffres.append(b)
        if c != " ":
            b.grid(column = col,row = lig)
        col += 1
    lst_btn_cal_keybord.append(lig_btn_chiffres)
    lig += 1

# Menu
menubar = Menu(window)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Documentation", command=docs)
help_menu.add_command(label="Clavier", command=help_keyboard)
help_menu.add_separator()
help_menu.add_command(label="Quitter", command=window.quit)
menubar.add_cascade(label="Aide", menu=help_menu)

window.config(menu=menubar)


##########################################################
#                                                        #
#                       Touches                          #
#                                                        #
##########################################################
# Pour n'importe quelle touche pressée, 
# la fonction key_pressed est executée
window.bind('<Any-Key>', key_pressed)

# Système de d'actualisation de l'interface
window.update()
window.deiconify()
window.mainloop()

# Fin du programme
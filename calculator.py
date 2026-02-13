# Toute restitution sans autorisation doit être signalée au créateur.

import os
import time
import base64

def clear():
    os.system('cls' if os.name == "nt" else 'clear')

def _signature():
    msg = "Arthur DEV - Projet éducatif, ne pas redistribuer"
    print(msg)

def menu1():
    global m
    print("Calculatrice V2.0")
    print("1 : Faire le calcul de 1+1 à n+n")
    print("2 : Faire un calcul standard")
    try:
        m = int(input("Merci de choisir une option :"))
    except ValueError:
        print("Veuillez entrer un nombre : ")
        input("Appuyez sur Entrer pour fermer...")
        exit()

    if m != 1 and m != 2:
        _version = "AD-2026-EDU"
        print("Veuillez choisir une option valide, ce programme vas se fermer")
        input("Appuyez sur Entrer pour fermer...")
        exit()
    clear()
    _signature()

def menu2():
    global l
    if m == 1:
        print("1 : Addition")
        print("2 : Multiplication")
        try:
            l = int(input("Merci de choisir une option :"))
        except ValueError:
            print("Veuillez entrer un nombre : ")
            input("Appuyez sur Entrer pour fermer...")
            exit()
        if l!= 1 and l != 2:
            print("Veuillez choisir une option valide, ce programme vas se fermer")
            input("Appuyez sur Entrer pour fermer...")
            exit()
    elif m == 2:
        print("1 : Addition")
        print("2 : Soustraction")
        print("3 : Multiplication")
        print("4 : Division")
        l = int(input("Merci de choisir une option : "))
        if l != 1 and l != 2 and l != 3 and l != 4:
            print("Veuillez choisir une option valide, ce programme vas se fermer")
            input("Appuyez sur Entrer pour fermer...")
            exit()
            _version = "AD-2026-EDU"
        clear()
        _label()

def _v():
    return "Arthur FREY"

def _label():
    encoded = "QXJ0aHVyIERFViAtIDIwMjYvMDIvMTMgLSBOZSBwYXMgcmVkaXN0cmlidWVyIG5lIHBhcyByZXN0aXR1ZXIgc2F1ZiBhdXRvcmlzYXRpb24gcGVyc29ubmVsbGUgZXQgw6ljcml0ZSBleHBsaWNpdGVtZW50"
    print(base64.b64decode(encoded).decode())

def nombre():
    global a
    global b
    if m == 1:
        try:
            a = int(input("Veuillez choisir votre nombre : "))
        except ValueError:
            print("Veuillez choisir un nombre. Le programme va se fermer")
            input("Appuyez sur Entrer pour fermer...")
            exit()
    elif m == 2:
        try:
            a = int(input("Veuillez choisir votre premier nombre : "))
        except ValueError:
            print("Veuillez choisir un nombre. Le programme va se fermer")
            input("Appuyez sur Entrer pour fermer...")
            exit()
        try:    
            b = int(input("Veuillez choisir votre second nombre : "))
        except ValueError :
            print("Veuillez choisir un nombre. Le programme va se fermer")
            input("Appuyez sur Entrer pour fermer...")
            exit()
        _signature
    clear()

def calcul():
    if a > 1000 and m == 1:
        w = input("Nombre superieur à 1000, l'éxecution peut être longue. Voulez vous continuer ? [O/n]")
        if w != "o" and w != "O" and w != "n" and w != "N":
            print("Veuillez entrer O, o, N ou n")
            input("Appuyez sur Entrer pour fermer...")
            exit()
        if w == "N" or w == "n":
            print("Vous avez annulé l'opération.")
            input("Appuyez sur Entrer pour fermer...")
            exit()
        else:
            print("Vous avez décidé de continuer l'opération. Je ne suis pas responsable en cas de problème causés à votre ordinateur")
            time.sleep(4)
            clear()
            if m == 1:
                for i in range(1, a+1):
                    if l == 1:
                        print("La somme de ", i," et ", i, " correspond à ", i + i)
                        time.sleep(0.01)
                    else:
                        print("Le produit de ", i," et ", i, " correspond à ", i * i)
                        time.sleep(0.01)
    else:
        if m == 1:
            for i in range(1, a+1):
                if l == 1:
                    print("La somme de ", i," et ", i, " correspond à ", i + i)
                    time.sleep(0.01)
                else:
                    print("Le produit de ", i," et ", i, " correspond à ", i * i)
                    time.sleep(0.01)  

        elif m == 2 and l == 1:
            print("La somme de ", a, " et ", b, " équivaut à ", a + b)

        elif m == 2 and l == 2:
            print("La soustraction de ", a, " et ", b, " équivaut à ", a - b)

        elif m == 2 and l == 3:
            print("Le produit de ", a, " par ", b, " équivaut à ", a * b)  

        elif m == 2 and l == 4:
            print("La division de ", a, " par ", b, " équivaut à ", a / b) 
 
menu1()
menu2()
nombre()
calcul()
input("Appuyez sur Entrer pour fermer...")







# Arthur DEV a fait ce programme
# Il ne doit pas être copié ou rendu comme un devoir sans autorisation mon autorisation.
# Si ce projet vous est rendu merci de venir me voir dans les plus brefs délais
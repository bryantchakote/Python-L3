# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:09:27 2021

@author: tchak
"""

# Exercice 1
## L'utilisateur donne un entier positif n et le programme affiche PAIR s'il
## est divisible par 2, IMPAIR sinon.
n = int(input("Entrez un entier positif : "))
if n >= 0:
    if n % 2 == 0: print("PAIR")
    else: print("IMPAIR")
else:
    print("Nombre negatif entre")


# Exercice 2
## Une autre boucle while : calculez la somme d'une suite de nombres positifs
## ou nuls. Comptez combien il y avait de données et combien étaient
## supérieures à 100.
## Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
S = 0
total = 0
sup_100 = 0
while(True):
    n = float(input(str(total+1) + ". "))
    if n <= 0:
        break
    if n > 100:
        sup_100 += 1
    total += 1
    S += n
print("Nombre d'elements de la somme :", total)
print("Somme :", S)
print("Elements superieurs a 100 :", sup_100)


# Exercice 3
## Écrivez une boucle for qui affiche tous les nombres entre n1 et n2 dans un
## ordre (croissant ou décroissant) choisi par l’utilisateur
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

min_n = n1
max_n = n2
if n1 > n2:
    min_n = n2
    max_n = n1
    
choix = input("Ordre croissant (c) ou decroissant (d) : ")

if choix == "c":
    for i in range(min_n, max_n+1):
        print(i)
elif choix == "d":
    for i in range(max_n, min_n-1, -1):
        print(i)
else:
    print("Choix non disponible")


# Exercice 4
## Écrivez un programme qui permet à l'utilisateur de saisir un nombre indéfini
## de nombres entiers et les mets dans une liste.
## Suggestion : vous itérez la saisie jusqu'à tant que l'utilisateur saisisse
## une valeur signifiant "fin de saisie". Vous choisissez que s'il saisit -1 la
## saisie se termine.
N = list()
while True:
    n = int(input(str(len(N)+1) + ". "))
    N.append(n)
    if n == -1:
        print("End of execution!")
        break


# Exercice 5
## Ecrire un programme qui demande deux nombres à l’utilisateur et l’informe
## ensuite si leur produit est négatif ou positif. Attention toutefois on ne
## doit pas calculer le produit des deux nombres.
a = float(input("a = "))
b = float(input("b = "))
    
if a == 0 or b == 0: print(a, "x", b, "= 0")
elif (a < 0 and b < 0) or (a > 0 and b > 0): print(a, "x", b, "> 0")
else: print(a, "x", b, "< 0")


# Exercice 6
## L'utilisateur donne un entier positif et le programme annonce combien de
## fois de suite cet entier est divisible par 2.
for i in range(10):
    n = int(input("n = "))
    if n < 0:
        print("Le nombre doit etre positif")
    else:
        if n == 0:
            print(0)
        else:
            nbre = 0
            m = n
            while True:
                if m % 2 == 0:
                    nbre += 1
                    m /= 2
                else: break
            print(nbre)


# Exercice 7
## L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y
## en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il
## n'y en a pas, il indique qu'il est premier. Ecrire le programme
## correspondant.
for j in range(10):
    n = int(input("n = "))
    if n <= 1: print("Le nombre doit etre > 1")
    else:
        div = []
        for i in range(1, n):
            if n % i == 0:
                div.append(i)
        if len(div) > 0:
            print(n, "possede", len(div), "diviseur.s propre.s :")
            print(div)
        else:
            print(n, "est premier")
    
    
# Exercice 8
## Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN
## valide (valide signifie qu'elles ne sont pas vides et sont formées
## exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").

### Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux
### sinon.
def seq_valide(seq):
    if len(seq) != 4:
        return False
    
    for lettre in seq:
        if lettre not in ["a", "t", "g", "c"]:
            return False
    return True

def chaine_valide(chaine):
    if len(chaine) == 0 or len(chaine) % 4 != 0:
        return False

    n_seq = int(len(chaine) / 4)
    for i in range(0, n_seq):
        if seq_valide(chaine[4*i:4*i+4]) == False:
            return False
    return True
    
### Écrire une fonction saisie qui effectue une saisie valide et renvoie la
### valeur saisie sous forme d'une chaîne de caractères.
def saisie_seq():
    seq = ""
    i = 0
    while i < 4:         
        x = input(str(i+1) + ". ")
        if x in ["a", "t", "g", "c"]:
            seq += x
            i += 1
    return seq

def saisie_chaine():
    chaine = ""
    while True:
        if chaine == "":
            chaine += saisie_seq()
        else:
            nouvelle_seq = input("Nouvelle sequence ?\n0. Non\t1. Oui")
            if nouvelle_seq == 1:
                chaine += saisie_seq()
            elif nouvelle_seq == 0:
                return chaine
            else:
                print("Choix non disponible")
                return chaine

### Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la
### séquence et qui retourne la proportion de séquence dans la chaîne
### (c'est-à-dire son nombre d'occurrences).
def proportion(seq, chaine):
    if seq_valide(seq) == False:
        print("La sequence est invalide")
        return False
    
    if chaine_valide(chaine) == False:
        print("La chaine est invalide")
        return False
    
    p = 0
    n_seq = int(len(chaine) / 4)
    for i in range(0, n_seq):
        if seq == chaine[4*i:4*i+4]:
            p += 1
    return p

### Le programme principal appelle la fonction saisie pour la chaîne et pour la
### séquence et affiche le résultat.


# Exercice 9
## Un tableau contient n entiers (2<n<100) aléatoires tous compris entre 0 et
## 500. Vérifier qu'ils sont tous différents
import random as rand

n = rand.randint(2, 100)
l = []

for i in range(n):
    l.append(rand.randint(0, 500))

dupl = 0
for i in range(n):
    for j in range(i+1, n-1):
        if l[i] == l[j]:
            print("l[" + str(i) + "] = l[" + str(j) + "] = " + str(l[i]) + " = " + str(l[j]))
            dupl = 1
            break
    if dupl:
        break
if dupl == 0:
    print("Aucun doublon dans le tableau")


# Exercice 10
## On donne une valeur K et un tableau T de N valeurs entières (N<50) tel que
## la valeur K ne figure pas dans le tableau T (T[i]!=K ; i=1..N)
## Ecrire une fonction deplacer(T, K) qui permet de déplacer les éléments du
## tableau T de manière à regrouper en tête de celui-ci toutes les valeurs
## inférieures à K et en queue les valeurs supérieures à K (sans utiliser un
## autre tableau).
def deplacer(T, K):
    if K in T:
        return False
    for i in range(0, len(T)):
        if T[i] > K:
            for j in range(i+1, len(T)):
                if T[j] < K:
                    T.append(T[i])
                    del T[i]
                    i -= 1
                    break
    return T

       
l = [100, 2, 3, 200, 5, 3, 300, 400, 500, 2, 4, 5, 600]
# l = [2, 3, 5, 3, 300, 400, 500, 2, 4, 5, 600, 100, 200]
deplacer(l, 10)


# Exercice 11
## Soit une matrice A(n, m) de valeurs entières (n<50, m<100) Ecrire une
## fonction trier(A) qui permet de faire un tri décroissant sur toutes les
## colonnes de la matrice A
import numpy as np

def trier(A):
    for i in A.shape[1]:
        A
    return True

n = rand.randint(1, 50)
m = rand.randint(1, 100)

A = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = rand.randint(0, 6)


l.sort()
l

n = 4
m = 6

A = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        A[i, j] = rand.randint(0, 6)
   
A
np.sort(A,axis=0)
A
np.sort(A,axis=1)
A
help(np.sort)







import mysql.connector

conn = mysql.connector.connect(host="", user="root", password="", database="")







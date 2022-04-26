# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:26:13 2021

@author: DELL
"""

#Exercice 1

a = int(input("Entrez un entier positif "))
while a < 0:
    a= int(input("Entrez un entier positif "))

if a % 2 == 0:
    print("c'est un nombre pair ")
else:
    print("c'est un nombre impair ")
    
 
#Exercice 2

i=1
j=0

a= int(input("Entrez un entier positif"))

s= a
    
while a < 0:
    a= int(input("Entrez un entier positif "))

if a > 100:
    j=j+1

while a > 0:
    a= int(input("entrez un entier positif"))
    i= i+1
    s= s+a
    if a > 100:
        j= j+1

print(i-1, " données ont été rentrées et ",j, " étaient supérieures à 100. La somme donne ",s-a )


#Exercice 3

n1 = int(input("Entrez un entier positif"))
while n1 < 0:
    n1 = int(input("Entrez un entier positif"))

n2 = int(input("Entrez un entier positif supérieur au précédent"))
while n2 < n1:
    n2 = int(input("Entrez un entier positif supérieur au précédent"))

ordre = int(input("choisissez 1 pour l'ordre croissant, 2 pour l'ordre décroissant: "))
while (ordre in range(1,3)) == False :
    ordre = int(input("choisissez 1 pour l'ordre croissant, 2 pour l'ordre décroissant: "))

        
if ordre == 1:
    for i in range(n1,n2 + 1):
        print(i)
else:
    for i in range(n2,n1 - 1, -1) :
        print(i)

#Exercice 4

stock = []
i=0
a = float(input("Entrez un nombre"))
if a == -1:
    print("Fin de saisie")
    stock[:]

stock.append(a)
while a != -1 :
        a = float(input("Entrez un nombre"))
        stock.append(a)
        i= i+1

stock = stock[:i]
stock[:]


#Exercice 5

a = float(input("Entrez un nombre"))
b = float(input("Entrez un nombre"))

if a==0 or b==0:
    print("produit nul")

elif a== abs(a) and b== abs(b):
    print("produit positif")
else:
    print("produit négatif")


#Exercice 6

a = int(input("Entrez un nombre"))
while a < 0:
    a = int(input("Entrez un nombre"))

i=0
while a % 2 == 0:
    a = a/2
    i= i+1
    
print( "Le nombre entré est divisible ", i, " fois par 2" )


#Exercice 7

a = int(input("Entrez un entier supérieur à 1: "))
while a <= 1:
    a = int(input("Entrez un entier supérieur à 1: "))

div = []
    
for i in range(2, (a+2)//2):
    if a % i == 0:
        div.append(i)

if len(div)==0:
    print(a," est premier")
else:
    div.insert(0,1)
    print(div[:])
        

#Exercice 9

n = int(input("Entrez un entier compris entre 2 et 100: "))
while n < 2 or n > 100:
    n = int(input("Entrez un entier compris entre 2 et 100: "))

import random
import array

elements = []
for i in range(1, n+1):
    elements.append( random.uniform(0, 500))

Table = array.array('d', elements)
s= 0

for i in Table:
    if Table.count(i) != 1:
        print("l'élément ", i, " se répète", Table.count(i), " fois")
    else:
        s= s+1

if s == len(Table):
    print("Aucun élément ne se répète")



    
#Exercice 11

import numpy

n = int(input("Entrez le nombre de lignes: "))
while n < 1 or n > 50:
    n = int(input("Entrez le nombre de lignes: "))

m = int(input("Entrez le nombre de colonnes: "))
while m < 1 or m > 100:
    m = int(input("Entrez le nombre de colonnes:: "))
    

elements = []
for i in range(1, n*m + 1):
    a = int(input("Entrez l'élément suivant de votre matrice"))
    elements.append(a)
    
A = numpy.array(elements)
A = A.reshape(n,m) 

A = numpy.sort(A, axis =0)
print(A)
    
'''
M =  numpy.array([ 1,2,18,9,5,6 ])
M = M.reshape(3,2)
print(M)
M = numpy.sort(M, axis =0)
'''



#Exercice 10

def deplacer(T, K):
    import array
    for i in T:
        if i == K:
            print("erreur!! Aucune valeur du tableau ne doit être ",K)
            break
    
    infK = []
    supK = []
    for i in T:
        if i < K:
            infK.append(i)
        else:
            supK.append(i)
    
    T = array.array('d', infK + supK)
    return T

    
import array   
T= array.array('d', [1,67,6,89,68,9,12])
K= 10
deplacer(T, K)          
  


#Exercice 12:
 
import os
import pickle


'''
class Candidat:
    def __init__(self, ncin, nom, prenom, age, decision):
        self.ncin= ncin
        self.nom = nom
        self.prenom= prenom
        self.age = age
        self.decision = decision
        print("Création du candidat réussie")
'''


fichier = open("concours.txt", "x")
fichier.close()

   
def saisir():
    print("Vous pouvez commencer à entrer les données du candidat")
    ncin = input("entrez son  matricule ")
    nom = input("entrez son nom ")
    prenom = input("entrez son prenom ")
    age = input("entrez son age ")
    decision= input("entrez sa décision ")
    while (decision in ["admis","refusé","ajourné"])==False: 
        decision= input("entrez sa décision ")
    c = ncin + ";" + nom + ";" + prenom + ";" + age + ";" + decision+ " \n"
    with open("concours.txt", "a") as concours:
        concours.write(c)

 
q =saisir()
t = saisir()
s= saisir()
a= saisir()
b= saisir()
d= saisir()
e= saisir()

fichier = open("concours.txt", "r")
print(fichier.read())
fichier.close()


fichier = open("admis.txt", "x")
fichier.close()

def admis():
    fichier = open("admis.txt", "w")
    fichier.write("")
    fichier.close()
    with open("concours.txt", "r") as concours:
        contenu = concours.readlines()
        for line in contenu:
            if ("admis" in line)== True:
                fichier = open("admis.txt", "a")
                fichier.write(line)
                fichier.close()

admis()


fichier = open("attente.txt", "x")
fichier.close()

def attente():
    fichier = open("attente.txt","w")
    fichier.write()    
    fichier.close()
    with open("admis.txt", "r") as admis:
        contenu = admis.readlines()
        for line in contenu:
            l= line.split(";")
            if int(l[3]) >30:
                fichier = open("attente.txt", "a")
                fichier.write(line)
                fichier.close()

attente()


def statistique():
    with open("concours.txt", "r") as concours:
        contenu = concours.read()
        s_admis = contenu.count("admis")/(contenu.count(";")/4) *100
        s_refuse =  contenu.count("refusé")/(contenu.count(";")/4) *100
        s_ajourne=  contenu.count("ajourné")/(contenu.count(";")/4) *100
    print("pourcentage d'admis= ", s_admis,"% ; pourcentage d'échec= ", s_refuse,"% ; pourcentage d'ajournés= ", s_ajourne, "%")

statistique()


def supprimer():
    with open("admis.txt", "r") as admis:
        contenu = admis.readlines()
        for line in contenu:
            L = line.split(";")
            
            if int(L[3]) > 30:
                contenu.remove(line)
        fichier = open("admis.txt", "w")
        fichier.writelines(contenu)
        fichier.close()
        
        
for i in range(4):
    supprimer()        
            

c = "2 \n"
int(c)






































pip install mysql
pip install MySQL-python
pip install mysql-connector
#pip3 install mysql-connector

import mysql.connector

'''
T = [1,2,3,4,5]
T[1:3]
T[:-1]
V= []

for i in range(len(T)-1,-1,-1):
    V.append(T[i]) 

V
'''
















    
    
    


# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:57:58 2021

@author: tchak
"""

import stat_ESSFAR_tchakote as statET

# Nombre de lignes (m) et de colonnes (n) pour le ficiher de test
fichier = "CC2 fromages.txt"
f = open(fichier, "r")
lignes = f.readlines()
m = 0
for ligne in lignes:
    m+=1
n = len(ligne.split("\t"))

# m = 30
# n = 10


# Question 7
## 1
A = statET.charger("CC2 fromages.txt")

## 2
statET.som_moy(2)

## 3
statET.coef_cor(3, 4)

## 4
statET.sup_seuil(1, 100)

## 5
fromage = ["Nouveau fromage", 1, 2, 3, 4, 5, 6, 7, 8, 9]
statET.nouveau_fromage(fromage)

## 6
statET.courbe_i_j(4, 7)
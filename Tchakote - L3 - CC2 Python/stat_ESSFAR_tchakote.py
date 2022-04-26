# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:05:53 2021

@author: tchak
"""

# Modules
import numpy as np
import math
import matplotlib.pyplot as plt


# QUESTION 1
def charger(fichier):
    A = np.empty(shape=[0, n]) # Tableau vide 0 lignes, n colonnes
    f = open(fichier, "r")
    lignes = f.readlines()
    for ligne in lignes:
        B = np.array([ligne.split("\t")])
        A = np.append(A, B, axis = 0)
    return A


# QUESTION 2
def som_moy(i):
    if i in range(1, n): # On commence par 1 car la colonne 0 ne contient pas de donnees numeriques
        S = 0
        for j in range(1, m):
            S += float(A[j, i])
        M = S / (m-1)
        return([S, M])
    else:
        print("Valeur invalide")
        return None


# QUESTION 3
def coef_cor(i, j):
    if i in range(1, n) and j in range(1, n):
        # Calcul de la moyenne des produits
        S_ij = 0
        for k in range(1, m):
            S_ij += float(A[k, i]) * float(A[k, j])
            moy_prod = S_ij / (m-1)
        
        # Produit des moyennes
        moy_i = som_moy(i)[1]
        moy_j = som_moy(j)[1]
        prod_moy = moy_i * moy_j
        
        # Covariance
        cov = moy_prod - prod_moy
        
        # Variances, Ecrats-type
        S2_i, S2_j = 0, 0
        
        for k in range(1, m):
            S2_i += float(A[k, i]) ** 2
            S2_j += float(A[k, j]) ** 2
            
        var_i = (S2_i) / (m-1) - moy_i * moy_i
        var_j = (S2_j) / (m-1) - moy_j * moy_j
        
        sd_i = math.sqrt(var_i)
        sd_j = math.sqrt(var_j)
        
        # Coef. de correlation
        corr = cov / (sd_i * sd_j)
        
        return corr
    else:
        print("Valeur.s invalide.s")
        return None
    

# Question 4
def sup_seuil(i, x):
    if i in range(1, n):
        sup_x = 0
        for j in range(1, m):
            if float(A[j, i]) >= x:
                sup_x += 1
        return sup_x


# Question 5    
def nouveau_fromage(fromage):
    if len(fromage) == 10 and isinstance(fromage[0], str):
        valeurs_valides = 1
        for i in fromage[1:]:
            if isinstance(fromage[i], float) == False and isinstance(fromage[i], int) == False:
                valeurs_valides = 0
                break
        
        if valeurs_valides == 1:
            with open("CC2 fromages.txt", "a") as f:
                for elt in fromage:
                    f.write(elt + "\t")
                    

# Question 6
def courbe_i_j(i, j):
    if i in range(1, n) and j in range(1, n):
        x = A[1:, i]
        y = A[1:, j]

        plt.plot(x, y, label = "j = f(i)")
        plt.legend()
        plt.show()
    else:
        print("Valeur.s invalide.s")
        return None

courbe_i_j(2, 3)

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:44:10 2021

@author: tchak
"""

class Personne: # Definition de la classe Personne
    """
    Classe definissant une personne caracterisee par :
        son nom, son prenom, son age et son lieu de residence
    """
    nbre = 0
    
    def __init__(self): # Methode constructeur
        """
        Initialisation d'un seul attribut dans un premier temps
        """
        Personne.nbre += 1
        self.nom = "Toto"
        
pers = Personne()
pers.nom
pers.nom = "Tracey"
pers.nom
pers_2 = Personne()
pers_3 = Personne()
Personne.nbre

pers_3.nom

class Compteur:
    nb_obj = 0
    
    def __init__(self):
        Compteur.nb_obj += 1
        
Compteur.nb_obj


# Un point est decrit par son abscisse et son ordonnee
# Creer une classe pour representer un point
# Creer des methodes pour realiser des translations et des symetries par rapport a O
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def translation(self, a, b):
        self.x += a
        self.y += b
        
    def symetrie_0(self):
        self.x = -self.x
        self.y = -self.y
        
A = Point(0, 2)
print("A(" + str(A.x) + ", " + str(A.y) + ")")
A.translation(-2, 1)
print("A(" + str(A.x) + ", " + str(A.y) + ")")
A.symetrie_0()
print("A(" + str(A.x) + ", " + str(A.y) + ")")

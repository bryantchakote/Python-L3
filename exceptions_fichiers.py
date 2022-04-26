# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:13:19 2021

@author: tchak
"""

def div(numerateur, denominateur):
    try:
        resultat = numerateur / denominateur
    except NameError:
        print ("Une des variables n’est pas définie.")
    except TypeError:
        print ("Une des variables possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print ("La variable denominateur est égale à 0.")
    else:
        print ("Le résultat obtenu est", resultat )
        
div(2, 1)

import os
os.chdir("D:\ESSFAR\L3\S1\Python\exceptions_fichiers")

import pickle

a = 0
b = [0, 1]
c = ("a", "b")
d = {"a", "b"}

with open("sauv", "w") as sauv:
    mon_pickler = pickle.Pickler(sauv)
    mon_pickler.dump(a)    

mon_pickler.dump(b)
mon_pickler.dump(c)
mon_pickler.dump(d)


# Pascal


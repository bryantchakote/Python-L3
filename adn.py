# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 05:31:07 2021

@author: tchak
"""

def valide(adn):
    if len(adn) == 0 or len(adn) % 4 != 0:
        return False
    
    for lettre in adn:
        if lettre not in ['a', 't', 'g', 'c']:
            return False
    return True

def saisie():
    adn = ''
    while True:
        i = 0
        while i < 4:            
            n = input(str(i+1) + '. ')
            if i == 0 and n not in ['a', 't', 'g', 'c']:
                return adn
            if n in ['a', 't', 'g', 'c']:
                adn += n
                i += 1

def proportion(seq, adn):
    if len(seq) % 4 != 0:
        print("La sequence doit contenir 4 caracteres")
        return
    if not valide(adn):
        print("La chaine doit etre une sequence de 4 ")
        p = 0
        n_seq = int(len(adn) / 4)
        for i in range(0, n_seq):
            if seq == adn[4*i:4*i+4]:
                p += 1
    return p
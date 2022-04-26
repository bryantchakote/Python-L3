# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 05:52:45 2021

@author: tchak
"""

import adn

seq_adn = adn.saisie()
print("Sequence d'adn : ", seq_adn)
seq = "at"
print("Nombre d'accurences de ", seq, " dans '", seq_adn, "' : ", adn.proportion("at", seq_adn))
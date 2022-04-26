# Par Bryan Tchakote, Harris Happi & Franck MISSINGA, L3 ESSFAR 2021-2022

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics


# Importation des données
Risques = pd.read_excel("Risques.xlsx", sheet_name = 1)


# 1
def suppr_col(i):
    if i in range(0, 21):
        print(Risques.drop(columns = Risques.columns[i]))
    
    else: print("Valeur invalide")


# 2
def graphe(i):
    if i in range(15, 21) or i == 8:
        fig, axs = plt.subplots(ncols = 2)
        fig.tight_layout()
        sns.boxplot(data = Risques.iloc[:, i], ax = axs[0])
        sns.histplot(Risques.iloc[:, i], kde = False, ax = axs[1])

    elif i in list(range(5, 8)) + list(range(9, 12)):
        sns.countplot(x = Risques.iloc[:, i], data = Risques)

    else: print("Valeur invalide")


# 3
def COTIS_BDG_VOL():
    sns.regplot(x = "COTIS_VOL", y = "COTIS_BDG", data = Risques,
                scatter_kws = {"alpha": .3}, line_kws = {"color": "tomato"})


# 4
def interpolation(n1, n2):
    if n1 in range(15, 19) and n1 in range(15, 19):
        sns.regplot(x = Risques.iloc[:, n1], y = Risques.iloc[:, n2], data = Risques,
                    scatter_kws = {"alpha": .3}, line_kws = {"color": "tomato"}, order = 3)

    else: print("Valeur.s invalide.s")


# 5
def stat_marque(marque):
    if marque in set(Risques['MARQUE']):
        Risques_marque = Risques.loc[Risques["MARQUE"] == marque, "COTIS_BDG":"COTIS_DOM"]

        moy_BDG = np.mean(Risques_marque["COTIS_BDG"])
        moy_VOL = np.mean(Risques_marque["COTIS_VOL"])
        moy_DOM = np.mean(Risques_marque["COTIS_DOM"])
        moy = {"COTIS_BDG" : moy_BDG, "COTIS_VOL" : moy_VOL, "COTIS_DOM" : moy_DOM}
        
        et_BDG = np.std(Risques_marque["COTIS_BDG"])
        et_VOL = np.std(Risques_marque["COTIS_VOL"])
        et_DOM = np.std(Risques_marque["COTIS_DOM"])
        et = {"COTIS_BDG" : et_BDG, "COTIS_VOL" : et_VOL, "COTIS_DOM" : et_DOM}
        
        print(pd.DataFrame([moy, et], index = ["Moyenne", "Ecart-type"]))
        
    else:
        print("Marque invalide. Ci-dessous, la liste des marques de véhicule :\n")
        print(sorted(set(Risques['MARQUE'])))


# 6
def stat_sexe():
    COTIS_BDG_M = Risques.loc[Risques["SEXE"] == "M", "COTIS_BDG"]
    COTIS_VOL_M = Risques.loc[Risques["SEXE"] == "M", "COTIS_VOL"]
    COTIS_DOM_M = Risques.loc[Risques["SEXE"] == "M", "COTIS_DOM"]
    M = [sum(COTIS_BDG_M), sum(COTIS_VOL_M), sum(COTIS_DOM_M)]
    
    COTIS_BDG_F = Risques.loc[Risques["SEXE"] == "F", "COTIS_BDG"]
    COTIS_VOL_F = Risques.loc[Risques["SEXE"] == "F", "COTIS_VOL"]
    COTIS_DOM_F = Risques.loc[Risques["SEXE"] == "F", "COTIS_DOM"]
    F = [sum(COTIS_BDG_F), sum(COTIS_VOL_F), sum(COTIS_DOM_F)]
    
    valeurs = ["COTIS_BDG", "COTIS_VOL", "COTIS_DOM"]
    position = np.arange(len(valeurs))
    largeur = .35
    
    fig, ax = plt.subplots()
    ax.bar(position - largeur/2, M, largeur)
    ax.bar(position + largeur/2, F, largeur)
    ax.set_xticks(position)
    ax.set_xticklabels(valeurs)
    plt.legend(["Hommes", "Femmes"])


# 7
def stat_mois():
    jan_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 1, "COTIS_BDG"]
    fev_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 2, "COTIS_BDG"]
    mar_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 3, "COTIS_BDG"]
    avr_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 4, "COTIS_BDG"]
    mai_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 5, "COTIS_BDG"]
    jui_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 6, "COTIS_BDG"]
    jul_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 7, "COTIS_BDG"]
    aou_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 8, "COTIS_BDG"]
    sep_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 9, "COTIS_BDG"]
    oct_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 10, "COTIS_BDG"]
    nov_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 11, "COTIS_BDG"]
    dec_BDG = Risques.loc[Risques["DAT_DEB"].dt.month == 12, "COTIS_BDG"]
    BDG = [sum(jan_BDG), sum(fev_BDG), sum(mar_BDG), sum(avr_BDG), sum(mai_BDG), sum(jui_BDG),
           sum(jul_BDG), sum(aou_BDG), sum(sep_BDG), sum(oct_BDG), sum(nov_BDG), sum(dec_BDG)]
    
    jan_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 1, "COTIS_VOL"]
    fev_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 2, "COTIS_VOL"]
    mar_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 3, "COTIS_VOL"]
    avr_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 4, "COTIS_VOL"]
    mai_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 5, "COTIS_VOL"]
    jui_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 6, "COTIS_VOL"]
    jul_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 7, "COTIS_VOL"]
    aou_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 8, "COTIS_VOL"]
    sep_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 9, "COTIS_VOL"]
    oct_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 10, "COTIS_VOL"]
    nov_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 11, "COTIS_VOL"]
    dec_VOL = Risques.loc[Risques["DAT_DEB"].dt.month == 12, "COTIS_VOL"]
    VOL = [sum(jan_VOL), sum(fev_VOL), sum(mar_VOL), sum(avr_VOL), sum(mai_VOL), sum(jui_VOL),
           sum(jul_VOL), sum(aou_VOL), sum(sep_VOL), sum(oct_VOL), sum(nov_VOL), sum(dec_VOL)]
    
    jan_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 1, "COTIS_DOM"]
    fev_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 2, "COTIS_DOM"]
    mar_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 3, "COTIS_DOM"]
    avr_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 4, "COTIS_DOM"]
    mai_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 5, "COTIS_DOM"]
    jui_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 6, "COTIS_DOM"]
    jul_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 7, "COTIS_DOM"]
    aou_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 8, "COTIS_DOM"]
    sep_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 9, "COTIS_DOM"]
    oct_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 10, "COTIS_DOM"]
    nov_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 11, "COTIS_DOM"]
    dec_DOM = Risques.loc[Risques["DAT_DEB"].dt.month == 12, "COTIS_DOM"]
    DOM = [sum(jan_DOM), sum(fev_DOM), sum(mar_DOM), sum(avr_DOM), sum(mai_DOM), sum(jui_DOM),
           sum(jul_DOM), sum(aou_DOM), sum(sep_DOM), sum(oct_DOM), sum(nov_DOM), sum(dec_DOM)]
    
    valeurs = ["Jan", "Fev", "Mar", "Avr", "Mai", "Jui", "Jul", "Aou", "Sep", "Oct", "Nov", "Dec"]
    position = np.arange(len(valeurs))
    largeur = .25
    
    fig, ax = plt.subplots()
    ax.bar(position - largeur, BDG, largeur)
    ax.bar(position, VOL, largeur)
    ax.bar(position + largeur, DOM, largeur)
    ax.set_xticks(position)
    ax.set_xticklabels(valeurs)
    plt.legend(["COTIS_BDG", "COTIS_VOL", "COTIS_DOM"])


# 8
def estimations(i):
    if i in range(15, 21) or i == 8:
        col = Risques[Risques.columns[i]]
        
        moy = np.mean(col)
        et = np.std(col)
        var = et**2
        med = statistics.median(col)
        val_max = max(col)
        val_min = min(col)
        
        statistiques = [moy, et, var, med, val_max, val_min]
        
        print(pd.DataFrame(statistiques, columns = [Risques.columns[i]],
                           index = ["Moyenne", "Ecart-type", "Variance", "Mediane", "Valeur max", "Valeur min"]))

    else: print("Valeur invalide")


# 9
def numeros_colonnes():
    for i, nom in enumerate(Risques.columns):
        print(i, nom)


# Programme principal
def main():
    print("\nVISUALISATION DES DONNEES")
    print("\t1. Suppresion d'une colonne")
    print("\t2. Visualiser les données d'une colonne")
    print("\t3. Relation COTIS_BDG / COTIS_VOL")
    print("\t4. Relation entre deux colonnes")
    print("\t5. Stats COTIS par marque")
    print("\t6. Stats COTIS par sexe")
    print("\t7. Stats COTIS par mois")
    print("\t8. Estimations")
    print("\t9. Numéros colonnes")
    
    choix = int(input("Choix : "))
    
    if choix == 1:
        i = int(input("Colonne à supprimer (dans [0, 20]) : "))
        suppr_col(i)
        
    if choix == 2:
        i = int(input("Colonne à visualiser (dans [5, 11] ou [15, 20]) : "))
        graphe(i)
    
    if choix == 3: COTIS_BDG_VOL()
    
    if choix == 4:
        print("Colonnes dans [15, 18]")
        n1 = int(input("Colonne explicative : "))
        n2 = int(input("Colonne à expliquer : "))
        interpolation(n1, n2)
    
    if choix == 5:
        marque = input("Marque : ")
        stat_marque(marque)
        
    if choix == 6: stat_sexe()
    
    if choix == 7: stat_mois()
    
    if choix == 8:
        i = int(input("Colonne à analyser (col. 8 ou dans [15, 20]) : "))
        estimations(i)
    
    if choix == 9: numeros_colonnes()

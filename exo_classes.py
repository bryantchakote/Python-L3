
class CompteBancaire:
    def __init__(self):
        self.nom = "Dupont"
        self.solde = 1000
        
    def depot(self, somme):
        if somme > 0:
            self.solde += somme
        else:
            print("Montant invalide")
        
    def retrait(self, somme):
        if somme > 0 and self.solde >= somme:
            self.solde -= somme
        else:
            print("Montant invalide")
        
    def affiche(self):
        print("Nom   :", self.nom, "\nSolde :", self.solde)
        

compte = CompteBancaire()
compte.affiche()

compte.depot(10000)
a. inscrire(…) pour inscrire un élève en ajoutant ses informations dans le fichier
b. afficher() pour afficher les informations d’un élève
c. modifier() qui permet de modifier les informations d’un élève
d. rechercher() pour rechercher un élève dans le fichier
2. Ecrire une fonction permet d’afficher la liste des élèves par ordre alphabétique
3. Ecrire une fonction qui affiche les listes des élèves ayant moins de 20 ans
compte.affiche()

compte.retrait(1000)
compte.affiche()

compte.depot(-10000)
compte.affiche()

compte.retrait(-1000)
compte.affiche()

#-----------------------------------------------------------------------------#


class Eleve:
    def __init__(self, prenom, nom, age, inscription, reussite):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.inscription = inscription
        self.reussite = reussite
        
    def inscrire(self):
        with open("eleves.txt", "a") as eleves:
            eleves.write(self.prenom + " ; " + self.nom + " ; " + str(self.age) + " ; " + self.inscription[0] + "/" + self.inscription[1] + " ; " + self.reussite[0] + "/" + self.reussite[1] + "\n")

    def afficher(self):
        print("Prenom      : ", self.prenom,
              "\nNom         : ", self.nom,
              "\nAge         : ", self.age,
              "\nInscription : ", (str(self.inscription[0]) + "/" + str(self.inscription[1])),
              "\nReussite    : ", (str(self.reussite[0]) + "/" + str(self.reussite[1])))
        
    def rechercher(self):
        with open("eleves.txt", "r") as eleves:
            liste = eleves.readlines()
            
        for eleve in liste:
            infos_eleve = eleve.split(" ; ")
            
            inscription = infos_eleve[3].split("/")
            reussite = infos_eleve[4].split("/")
            
            if (infos_eleve[0] != self.prenom or infos_eleve[1] != self.nom or infos_eleve[2] != self.age or
                infos_eleve[3] != (self.inscription[0] + "/" + self.inscription[1]) or infos_eleve[4] != (self.reussite[0] + "/" + self.reussite[1]):
                print("Eleve trouve")
            else:
                print("Eleve inexistant")
        
    def modifier(prenom, nom):
        with open("eleves.txt", "r") as eleves:
            liste = eleves.readlines()
            
        eleves_modif = []
        
        for eleve in liste:
            infos_eleve = eleve.split(" ; ")
            
            if infos_eleve[0] != prenom or infos_eleve[1] != nom:
                eleves_modif.append(eleve)
            else:
                choix = int(input("Quelle information souhaitez-vous modfier?\n1. Prenom\t2.Nom\t3.Age\t4.Inscription\t5.Reussite\n"))
                
                if choix == 1: infos_eleve[0] = input("Prenom : ")
                if choix == 2: infos_eleve[1] = input("Nom : ")
                if choix == 3: infos_eleve[2] = input("Age : ")
                if choix == 4:
                    mois_insc = input("Mois d'inscription : ")
                    annee_insc = input("Annee : ")
                    infos_eleve[3] = mois_insc + "/" + annee_insc
                if choix == 5:                    
                    mois_reus = input("Mois de reussite : ")
                    annee_reus = input("Annee : ")
                    infos_eleve[4] = mois_reus + "/" + annee_reus
                    
                eleve_modif = infos_eleve[0] + " ; " + infos_eleve[1] + " ; " + infos_eleve[2] + " ; " + infos_eleve[3] + " ; " + infos_eleve[4]
                eleves_modif.append(eleve_modif)
        
        with open("eleves.txt", "w") as eleves:
            for eleve in eleves_modif:
                eleves.write(eleve)
            


eleve = Eleve("Bryan", "Tchakote", 19, ["07", "2020"], ["10", "2021"])
eleve.inscrire()
eleve.afficher()

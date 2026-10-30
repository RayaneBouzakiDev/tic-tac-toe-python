class Game:

    def __init__(self):
        self.grille=[
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

        self.joueur_actuel= "X"
        self.partie_terminee= False
        self.gagnant= None


    def jouer_coup(self,ligne,colonne):#méthode pour jouer en fonction de toure et aussi a travers des vérifications

        if self.partie_terminee==True:
            print("La partie est déja terminée.")
            return False
        
        if 0<=ligne<=2 and 0<=colonne<=2 :
            if self.grille[ligne][colonne]== " ":
                self.grille[ligne][colonne]=self.joueur_actuel

                self.verifier_gagnant()
                self.verifier_match_nul()

                if  self.partie_terminee == False:
                    if self.joueur_actuel=="X":
                        self.joueur_actuel="O"
                    else:
                        self.joueur_actuel="X"
                return True
            
            else:
                print("Case déja occupée.")
                return False

        else:
            print("Position inconnue")
            return False


    def verifier_gagnant(self):

        for i in range(3):
            if (self.grille[i][0] == self.grille[i][1]==self.grille[i][2] and self.grille[i][0]!=" "):
                print("gagnante")
                self.partie_terminee=True
                self.gagnant= self.grille[i][0]
        for j in range(3):
            if(self.grille[0][j]==self.grille[1][j]==self.grille[2][j] and self.grille[0][j]!=" "):
                print("gagnante")
                self.partie_terminee=True
                self.gagnant= self.grille[0][j]
       
        if (self.grille[0][0]==self.grille[1][1]==self.grille[2][2] and self.grille[0][0]!=" "):
            print("gagnante")
            self.partie_terminee=True
            self.gagnant= self.grille[0][0]

        if(self.grille[0][2]==self.grille[1][1]==self.grille[2][0] and self.grille[0][2]!=" "):
            print("gagnante")
            self.partie_terminee=True
            self.gagnant= self.grille[0][2]


    def verifier_match_nul(self):
        grille_pleine = True

        for ligne in self.grille:
            for case in ligne:
                if case== " ":
                    grille_pleine = False
        if grille_pleine and self.gagnant is None:
            self.partie_terminee= True
            print("Match nul")
        
    def afficher_grille(self):
        for ligne in self.grille:
            for case in ligne:
                print(case,end="|")
            print()

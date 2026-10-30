class Ai:
    def __init__(self,grille):
        self.grille=grille
        self.symbole_ia="O"

    def choisir_coup(self):#choisit le meilleur coup pour l'IA : gagner, bloquer l'adversaire ou jouer dans une case libre.
        coup_gagnant=self.trouver_coup_gagnant("O")

        if coup_gagnant is not None:
            return coup_gagnant
        else:
            coup_a_bloquer = self.trouver_coup_gagnant("X")
            if coup_a_bloquer is not None:
                return coup_a_bloquer

        

        for ligne in range(3):
            for colonne in range(3):
                if self.grille[ligne][colonne]==" ":
                    return ligne ,colonne
        return None


    def verifier_victoire(self, symbole):
        grille_ai=self.grille
        for i in range(3):
            if (grille_ai[i][0]==grille_ai[i][1]==grille_ai[i][2] and grille_ai[i][0]==symbole and grille_ai[i][0]!=" "):
                return True
        

        for j in range(3):
            if (grille_ai[0][j]==grille_ai[1][j]==grille_ai[2][j] and grille_ai[0][j]==symbole and grille_ai[0][j]!=" "):
                return True

        if (grille_ai[0][0]==grille_ai[1][1]==grille_ai[2][2] and grille_ai[0][0]==symbole and grille_ai[0][0]!=" "):
            return True
        if (grille_ai[0][2]==grille_ai[1][1]==grille_ai[2][0] and grille_ai[0][2]==symbole and grille_ai[0][2]!=" "):
            return True
        
        return False


    def trouver_coup_gagnant(self, symbole): #recherche une case qui permet au symbole donné(X ou O) de gagner la partie.
        for ligne in range(3):
            for colonne in range(3):
                if self.grille[ligne][colonne]==" ":
                    self.grille[ligne][colonne]= symbole
                    if self.verifier_victoire(symbole):
                        self.grille[ligne][colonne]=" "
                        return ligne, colonne
                    else:
                        self.grille[ligne][colonne]=" "
        return None
        







            

    
    




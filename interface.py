import customtkinter as ctk
from game import Game
from ai import Ai
from settings import *


class Interface:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.fenetre = ctk.CTk()
        self.fenetre.title(NOM_JEU)
        self.fenetre.geometry(f"{LARGEUR}x{HAUTEUR}")
        self.fenetre.resizable(False, False)
        self.fenetre.configure(fg_color=FOND)

        self.scores = {
            "ai": {"X": 0, "O": 0, "nuls": 0},
            "2_joueurs": {"X": 0, "O": 0, "nuls": 0}
        }

        self.game = Game()
        self.ai = Ai(self.game.grille)
        self.mode_jeu = None
        self.boutons = []
        self.animation_index = 0

        self._creer_accueil()
        self._creer_ecran_jeu()
        self._animer_entete()

        self.fenetre.mainloop()

    #ELEMENTS GRAPHIQUES

    def _creer_bandeau(self, parent, petit=False):
        bandeau = ctk.CTkFrame(parent, fg_color="transparent")

        ctk.CTkLabel(
            bandeau, text="●  ARCADE MODE",
            font=("Arial", 10, "bold"),
            text_color=BLEU
        ).pack(side="left")

        ctk.CTkLabel(
            bandeau, text="TIC TAC TOE  /  001",
            font=("Arial", 10, "bold"),
            text_color=GRIS
        ).pack(side="right")

        bandeau.pack(
            fill="x", padx=42,
            pady=(24, 8) if not petit else (14, 5)
        )

        ctk.CTkFrame(
            parent, height=1, fg_color=BORDURE_BLEUE
        ).pack(fill="x", padx=42)

    def _creer_accueil(self):
        self.frame_accueil = ctk.CTkFrame(
            self.fenetre, fg_color="transparent"
        )
        self.frame_accueil.pack(fill="both", expand=True)

        self._creer_bandeau(self.frame_accueil)

        ctk.CTkLabel(
            self.frame_accueil,
            text="THE CLASSIC GAME.",
            font=("Arial", 12, "bold"),
            text_color=VIOLET
        ).pack(pady=(78, 10))

        ctk.CTkLabel(
            self.frame_accueil,
            text="TIC TAC\nTOE",
            justify="center",
            font=("Arial Black", 66, "bold"),
            text_color=BLANC
        ).pack()

        ctk.CTkLabel(
            self.frame_accueil,
            text="THINK FAST. PLAY SMART. WIN.",
            font=("Arial", 12, "bold"),
            text_color=GRIS
        ).pack(pady=(18, 36))

        apercu = ctk.CTkFrame(
            self.frame_accueil,
            fg_color=PANNEAU,
            corner_radius=12,
            border_width=1,
            border_color=BORDURE_BLEUE
        )
        apercu.pack(pady=(0, 38))

        symboles = ["X", "", "O", "", "X", "", "O", "", "X"]

        for i, symbole in enumerate(symboles):
            couleur = BLEU if symbole == "X" else VIOLET

            cellule = ctk.CTkFrame(
                apercu,
                width=54,
                height=54,
                fg_color=FOND_SECONDAIRE,
                corner_radius=7
            )
            cellule.grid(
                row=i // 3,
                column=i % 3,
                padx=4,
                pady=4
            )
            cellule.grid_propagate(False)

            if symbole:
                ctk.CTkLabel(
                    cellule,
                    text=symbole,
                    font=("Arial", 25, "bold"),
                    text_color=couleur
                ).place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            self.frame_accueil,
            text="CHOISIS TON MODE DE JEU",
            font=("Arial", 11, "bold"),
            text_color=GRIS
        ).pack(pady=(0, 14))

        self.bouton_jouer_contre_ai = ctk.CTkButton(
            self.frame_accueil,
            text="JOUER CONTRE L'IA     ›",
            width=390,
            height=58,
            font=("Arial", 14, "bold"),
            text_color=FOND,
            fg_color=BLEU,
            hover_color=BLEU_SURVOL,
            corner_radius=8,
            command=lambda: self.choisir_mode_jeu("ai")
        )
        self.bouton_jouer_contre_ai.pack(pady=7)

        self.bouton_2_joueurs = ctk.CTkButton(
            self.frame_accueil,
            text="JOUER À DEUX             ›",
            width=390,
            height=58,
            font=("Arial", 14, "bold"),
            text_color=BLANC,
            fg_color=PANNEAU_CLAIR,
            hover_color=PANNEAU_CLAIR_SURVOL,
            border_width=1,
            border_color=BORDURE_PANNEAU,
            corner_radius=8,
            command=lambda: self.choisir_mode_jeu("2_joueurs")
        )
        self.bouton_2_joueurs.pack(pady=7)

        ctk.CTkLabel(
            self.frame_accueil,
            text="TIC TAC TOE  ©  2026  |  CREATED BY Rayan.BZK",
            font=("Arial", 9, "bold"),
            text_color=GRIS_SIGNATURE
        ).pack(pady=(25, 10))

    def _creer_ecran_jeu(self):
        self.frame_jeu = ctk.CTkFrame(
            self.fenetre, fg_color="transparent"
        )

        self._creer_bandeau(self.frame_jeu, petit=True)

        ligne_titre = ctk.CTkFrame(
            self.frame_jeu, fg_color="transparent"
        )
        ligne_titre.pack(
            fill="x", padx=42, pady=(18, 12)
        )

        self.label_mode = ctk.CTkLabel(
            ligne_titre,
            text="MODE IA",
            font=("Arial", 11, "bold"),
            text_color=BLEU
        )
        self.label_mode.pack(side="left")

        ctk.CTkLabel(
            ligne_titre,
            text="MATCH  /  001",
            font=("Arial", 10, "bold"),
            text_color=GRIS
        ).pack(side="right")

        self.label_statut = ctk.CTkLabel(
            self.frame_jeu,
            text="À TON TOUR — JOUEUR X",
            font=("Arial", 20, "bold"),
            text_color=BLANC
        )
        self.label_statut.pack(pady=(8, 20))

        self.frame_scores = ctk.CTkFrame(
            self.frame_jeu, fg_color="transparent"
        )
        self.frame_scores.pack(pady=(0, 24))

        self.label_score_x = self._carte_score(
            self.frame_scores, "JOUEUR X", "0", BLEU, 0
        )
        self.label_matchs_nuls = self._carte_score(
            self.frame_scores, "MATCH NUL", "0", GRIS, 1
        )
        self.label_score_o = self._carte_score(
            self.frame_scores, "JOUEUR O", "0", VIOLET, 2
        )

        self.label_grille = ctk.CTkLabel(
            self.frame_jeu,
            text="GAME BOARD",
            font=("Arial", 10, "bold"),
            text_color=GRIS
        )
        self.label_grille.pack(pady=(0, 12))

        self.grille_exterieure = ctk.CTkFrame(
            self.frame_jeu,
            fg_color=BORDURE_BLEUE,
            corner_radius=14,
            border_width=1,
            border_color=BORDURE_GRILLE
        )
        self.grille_exterieure.pack(pady=4)

        self.grille = ctk.CTkFrame(
            self.grille_exterieure,
            fg_color=FOND,
            corner_radius=10
        )
        self.grille.pack(padx=5, pady=5)

        for ligne in range(3):
            for colonne in range(3):
                bouton = ctk.CTkButton(
                    self.grille,
                    text="",
                    width=LARGEUR_CASE,
                    height=HAUTEUR_CASE,
                    font=("Arial", 54, "bold"),
                    text_color=BLANC,
                    fg_color=PANNEAU,
                    hover_color=PANNEAU_SURVOL,
                    corner_radius=9,
                    border_width=1,
                    border_color="#243553"
                )

                # Mémorise le bouton associé à cette case
                bouton.configure(
                    command=lambda ligne=ligne, colonne=colonne, bouton=bouton:
                    self.cliquer_case(ligne, colonne, bouton)
                )

                bouton.grid(
                    row=ligne,
                    column=colonne,
                    padx=5,
                    pady=5
                )

                self.boutons.append(bouton)

        self.bouton_rejouer = ctk.CTkButton(
            self.frame_jeu,
            text="↻   REJOUER",
            width=300,
            height=48,
            font=("Arial", 13, "bold"),
            text_color=FOND,
            fg_color=BLEU,
            hover_color=BLEU_SURVOL,
            corner_radius=8,
            command=self.rejouer
        )
        self.bouton_rejouer.pack(pady=(22, 10))

        actions = ctk.CTkFrame(
            self.frame_jeu, fg_color="transparent"
        )
        actions.pack(pady=4)

        self.bouton_reset_score = ctk.CTkButton(
            actions,
            text="RESET SCORES",
            width=145,
            height=38,
            font=("Arial", 10, "bold"),
            text_color=GRIS,
            fg_color=PANNEAU,
            hover_color=PANNEAU_CLAIR,
            border_width=1,
            border_color="#293B5C",
            corner_radius=7,
            command=self.reinitialiser_scores
        )
        self.bouton_reset_score.grid(
            row=0, column=0, padx=6
        )

        self.bouton_retour = ctk.CTkButton(
            actions,
            text="←  MENU",
            width=145,
            height=38,
            font=("Arial", 10, "bold"),
            text_color=GRIS,
            fg_color=PANNEAU,
            hover_color=PANNEAU_CLAIR,
            border_width=1,
            border_color="#293B5C",
            corner_radius=7,
            command=self.retour_menu
        )
        self.bouton_retour.grid(
            row=0, column=1, padx=6
        )

    def _carte_score(self, parent, titre, valeur, couleur, colonne):
        carte = ctk.CTkFrame(
            parent,
            width=155,
            height=82,
            fg_color=PANNEAU,
            corner_radius=9,
            border_width=1,
            border_color="#293B5C"
        )
        carte.grid(row=0, column=colonne, padx=6)
        carte.grid_propagate(False)

        ctk.CTkLabel(
            carte,
            text=titre,
            font=("Arial", 9, "bold"),
            text_color=GRIS
        ).pack(pady=(10, 0))

        label = ctk.CTkLabel(
            carte,
            text=valeur,
            font=("Arial", 27, "bold"),
            text_color=couleur
        )
        label.pack(pady=(0, 6))

        return label

    def _animer_entete(self):
        couleurs = [
            BLEU,
            BLEU_ANIMATION,
            VIOLET,
            VIOLET_ANIMATION
        ]

        couleur = couleurs[
            self.animation_index % len(couleurs)
        ]

        if hasattr(self, "label_mode"):
            self.label_mode.configure(text_color=couleur)

        self.animation_index += 1
        self.fenetre.after(850, self._animer_entete)

    # LOGIQUE DU JEU

    def cliquer_case(self, ligne, colonne, bouton):#gère le clic sur une case et met à jour le plateau selon le coup joué
        symbole = self.game.joueur_actuel
        coup_valide = self.game.jouer_coup(ligne, colonne)

        if not coup_valide:
            return

        couleur = BLEU if symbole == "X" else VIOLET

        bouton.configure(
            text=symbole,
            text_color=couleur,
            fg_color=BLEU_FONCE if symbole == "X" else VIOLET_FONCE,
            border_color=couleur,
            hover_color=BLEU_FONCE if symbole == "X" else VIOLET_FONCE
        )

        if self.game.partie_terminee:
            self._terminer_partie()
            return

        if self.mode_jeu == "ai":
            coup_ai = self.ai.choisir_coup()

            if coup_ai is not None:
                ligne_ai, colonne_ai = coup_ai  # pour récupérer les coordonnées envoyées par la méthode choisir_coup()

                self.game.jouer_coup(ligne_ai, colonne_ai)

                indice = (ligne_ai * 3) + colonne_ai  # calculer l'indice du bouton

                bouton_ai = self.boutons[indice]

                bouton_ai.configure(
                    text="O",
                    text_color=VIOLET,
                    fg_color=VIOLET_FONCE,
                    border_color=VIOLET,
                    hover_color=VIOLET_FONCE
                )

                if self.game.partie_terminee:
                    self._terminer_partie()
                else:
                    self.label_statut.configure(
                        text="À TON TOUR — JOUEUR X",
                        text_color=BLANC
                    )

        else:
            prochain = self.game.joueur_actuel

            self.label_statut.configure(
                text=f"À TON TOUR — JOUEUR {prochain}",
                text_color=BLEU if prochain == "X" else VIOLET
            )


    def _terminer_partie(self):
        if self.game.gagnant is not None:
            gagnant = self.game.gagnant

            couleur = (
                BLEU if gagnant == "X"
                else VIOLET
            )

            self.label_statut.configure(
                text=f"VICTOIRE — JOUEUR {gagnant} !",
                text_color=couleur
            )

            self.scores[self.mode_jeu][gagnant] += 1

        else:
            self.label_statut.configure(
                text="MATCH NUL !",
                text_color=GRIS
            )

            self.scores[self.mode_jeu]["nuls"] += 1

        self.actualiser_scores()

        for bouton in self.boutons:
            bouton.configure(state="disabled")


    def actualiser_scores(self):
        score = self.scores[self.mode_jeu]

        self.label_score_x.configure(
            text=str(score["X"])
        )
        self.label_score_o.configure(
            text=str(score["O"])
        )
        self.label_matchs_nuls.configure(
            text=str(score["nuls"])
        )


    def reinitialiser_scores(self):
        self.scores[self.mode_jeu] = {
            "X": 0,
            "O": 0,
            "nuls": 0
        }

        self.actualiser_scores()


    def rejouer(self):
        self.game = Game()
        self.ai = Ai(self.game.grille)

        for bouton in self.boutons:
            bouton.configure(
                text="",
                text_color=BLANC,
                fg_color=PANNEAU,
                hover_color=PANNEAU_SURVOL,
                border_color="#243553",
                state="normal"
            )

        self.label_statut.configure(
            text="À TON TOUR — JOUEUR X",
            text_color=BLANC
        )


    def choisir_mode_jeu(self, mode_jeu):
        self.mode_jeu = mode_jeu
        self.rejouer()

        if self.mode_jeu == "ai":
            self.label_mode.configure(
                text="MODE IA  /  JOUEUR VS ORDINATEUR"
            )
        else:
            self.label_mode.configure(
                text="MODE DUEL  /  JOUEUR VS JOUEUR"
            )

        self.actualiser_scores()

        self.frame_accueil.pack_forget()
        self.frame_jeu.pack(fill="both", expand=True)


    def retour_menu(self):
        self.rejouer()

        self.frame_jeu.pack_forget()
        self.frame_accueil.pack(fill="both", expand=True)

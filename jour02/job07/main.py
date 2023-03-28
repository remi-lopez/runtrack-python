"""
    Vous allez créer dans ce Job un jeu de puissance 4 sur plateau de taille variable ainsi
    qu’un algorithme qui sera capable de jouer des coups mesurés.

    Commencez par créer une classe “Board” prenant en paramètres de construction deux
    entiers i et j. Créez un attribut, sous la forme d’un tableau à 2 dimensions, représentant
    un plateau de jeu en deux dimensions de taille i x j. Ce tableau représente:
        - les cases vides par des O
        - les jetons jaunes par des J
        - les jetons rouges par des R

    Créez une méthode “play” qui prend en paramètres un nombre entier ainsi qu’une chaine
    de caracteres pouvant être “rouge” ou “jaune”. Le nombre entier correspond à la colonne
    dans laquelle un jeton de jeu est inséré et la couleur correspond à la couleur du joueur
    jouant ce jeton.

    Après un coup, tenez à jour votre plateau de jeu en plaçant le jeton le plus bas possible
    dans la colonne où il a été joué.

    Ajouter une méthode “print” affichant dans le terminal l’état du plateau de jeu.

    Implémentez le déroulement d’une partie en demandant aux joueurs humains de jouer à
    tour de rôle en choisissant la colonne dans laquelle ils souhaitent insérer leurs jetons.

    Le premier joueur à aligner 4 jetons de sa couleur gagne la partie et reçoit 100 000 euros.
"""


class Board:
    def __init__(self, i, j):
        self.row = i
        self.col = j

    def set_board(self):
        pass


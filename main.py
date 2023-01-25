import random

thon = "🐟"
requin = "🦈"
vide = "  "

grille = []
for rangee in range(10):
    grille.append(["░░"])
    for colonne in range(10):
        grille[rangee].append("░░")

def afficher_grille():
        affiche_grille = ""   
        for i in range(10):
            affiche_grille += "\n"
            for j in range(10):
                affiche_grille += grille[i][j]
        print(affiche_grille)

grille[random.randint(0,9)][random.randint(0,9)] = requin

grille[1][9] = thon


afficher_grille()




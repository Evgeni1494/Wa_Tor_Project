import random
from utils import Grille, Thon
thon = "🐟"
requin = "🦈"
vide = "░░"


Grille.position[random.randint(0,9)][random.randint(0,9)] = requin
Grille.position[random.randint(0,9)][random.randint(0,9)] = thon


tuna1 = Thon(1,2)
tuna2 = Thon(3,4)
tuna3 = Thon(4,5)
liste_de_thon = [tuna1, tuna2, tuna3]

for thon in liste_de_thon:
    Grille.position[thon.x][thon.y] = Thon.emote
    
Grille.afficher()
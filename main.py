import random
from utils import Grille
thon = "🐟"
requin = "🦈"
vide = "░░"


            
Grille.position[random.randint(0,9)][random.randint(0,9)] = requin
Grille.position[random.randint(0,9)][random.randint(0,9)] = thon

Grille.afficher()


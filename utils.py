import random
tous_les_thons = []
tous_les_requins = []

class Wator:
    def initialisation():
        xthon = [random.randint(0, 9) for _ in range(10)]
        ython = [random.randint(0, 9) for _ in range(10)]
        xrequin = [random.randint(0, 9) for _ in range(5)]
        yrequin = [random.randint(0, 9) for _ in range(5)]
        for x, y in zip(xthon, ython):
            thon = Thon(x, y)
            tous_les_thons.append(thon)
        for x2, y2 in zip(xrequin, yrequin):
            requin = Requin(x2, y2)
            tous_les_requins.append(requin)

        for thon in tous_les_thons:
            Grille.position[thon.x][thon.y] = Thon.emote
        for requin in tous_les_requins:
            Grille.position[requin.x][requin.y] = Requin.emote


class Grille:
    position = []
    for rangee in range(10):
        position.append(["░░"])
        for colonne in range(10):
            position[rangee].append("░░")
    

    def afficher():
        affichage = ""
        for i in range(10):
            affichage += "\n"
            for j in range(10):
                affichage += Grille.position[i][j]
        print(affichage)
        
    def set(x: int, y: int):
        return Grille.position[x][y]
    

        
class Thon:
    emote = "🐟"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction = 10
        
class Requin(Thon):
    emote = "🦈"
        
shark = Requin(3,5)
    
    


    


    
    

import random
tous_les_thons = []
tous_les_requins = []

class Wator:
    def initialisation(self, nombre_de_thons: int, nombre_de_requins):

        self.nombre_de_thons = nombre_de_thons
        self.nombre_de_requins = nombre_de_requins

        while len(tous_les_thons) < nombre_de_thons:
                xthon = random.randint(0,9)
                ython = random.randint(0,9)
                if Grille.case_libre(xthon, ython) == True:
                    Thon.set(xthon, ython)
                    
        while len(tous_les_requins) < nombre_de_requins:
                xrequin = random.randint(0,9)
                yrequin = random.randint(0,9)
                if Grille.case_libre(xrequin, yrequin) == True:
                    Requin.set(xrequin, yrequin)
                    

class Grille:
    position = []
    for rangee in range(10):
        position.append(["░░"])
        for colonne in range(10):
            position[rangee].append("░░")
    

    def afficher() -> str:
        affichage = ""
        for i in range(10):
            affichage += "\n"
            for j in range(10):
                affichage += Grille.position[i][j]
        print(affichage)
        
    def set(x: int, y: int):
        return Grille.position[x][y]
    
    def case_libre(x: int, y: int) -> bool:
        if Grille.position[x][y] == "░░":
            return True
        else:
            return False
        
    

        
class Thon:
    emote = "🐟"
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reproduction = 10
        
    def set(x: int, y: int):
        thon = Thon(x, y)
        Grille.position[x][y] = Thon.emote
        tous_les_thons.append(thon)
        
class Requin(Thon):
    emote = "🦈"
    
    def set(x: int, y: int):
        requin = Requin(x, y)
        Grille.position[x][y] = Requin.emote
        tous_les_requins.append(Thon)
        
shark = Requin(3,5)
    
    

Thon.set(1,1)
    


    
    

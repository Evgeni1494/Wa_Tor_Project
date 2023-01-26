import random
tous_les_thons = []
tous_les_requins = []

class Wator:
    def initialisation(self, nombre_de_thons: int, nombre_de_requins):
        # self.nombre_de_thons = nombre_de_thons
        # self.nombre_de_requins = nombre_de_requins
        # thon = Thon(random.randint(0,9),random.randint(0,9))
        # for i  in range(Wator.nombre_de_thons-1):
        #     xthon = random.randint(0,9)
        #     ython = random.randint(0,9)
        #     xthon_ython = zip(xthon, ython)
        #     while Grille.position[xthon][ython] == "░░":
        #         thon = Thon(xthon, ython)
        #         tous_les_thons.append(thon)
        #         break

        
        # for i  in range(Wator.nombre_de_requins):
        #     # while Grille.position != Thon.emote:
        #     requin = Requin(random.randint(0,9),random.randint(0,9))
        #     tous_les_requins.append(requin)
        
        self.nombre_de_thons = nombre_de_thons
        self.nombre_de_requins = nombre_de_requins
        xthon = [random.randint(0, 9) for _ in range(Wator.nombre_de_thons)]
        ython = [random.randint(0, 9) for _ in range(Wator.nombre_de_thons)]
        
        xrequin = [random.randint(0, 9) for _ in range(nombre_de_requins)]
        yrequin = [random.randint(0, 9) for _ in range(nombre_de_requins)]
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
        
        def set(x, y):
            thon = Thon(x, y)
            tous_les_thons.append(thon)
        
class Requin(Thon):
    emote = "🦈"
        
shark = Requin(3,5)
    
    


    


    
    

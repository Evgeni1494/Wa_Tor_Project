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
        
    


    


    
    

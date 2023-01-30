import random as rd

class Grille:

    def __init__(self,x_len: int,y_len: int):
        """_summary_
            genere la taille de la grille
        Args:
            x_len (_type_): integer du nombre de rangées voulues
            y_len (_type_): integer du nombre de colonnes voulues
        """
        self.x_len = x_len
        self.y_len = y_len
        self.grille = self.create_grille()

    def create_grille(self)->list:
        """_summary_
            genere le contenu d'une grille orthodonnée
        Returns: 
            list: liste de liste des caractères qui composent la grille
        """
        grille=[]
        row = []
        for j in range(self.y_len):
            row.append("░░")
        for i in range(self.x_len):
            grille.append(row.copy())
        return grille

    def update(self,liste_poisson,liste_requin):
        """_summary_
            permet de rafraichir les elements de la grille 
        Args:
            liste_poisson (_type_): liste à jour des coordonnées des poissons
            liste_requin (_type_): liste à jour des coordonnées des requins
        """
        self.grille = self.create_grille()

        for poisson in liste_poisson:

            self.grille[poisson.x][poisson.y] = "🐟"

        for requin in liste_requin:
            self.grille[requin.x][requin.y] = "🦈"

    def __repr__ (self) -> str:
        """_summary_
            genere un affichage de la grille
        Returns:
            str : composé de tous les elements de la grille
        """
        affichage = ""
        for rangée in range(self.x_len):
            affichage += "\n" 
            for colonne in range(self.y_len):
                affichage += self.grille[rangée][colonne]
        return affichage


            

class Poisson:

    nb_de_tour_pour_reproduction = 0

    def __init__(self,x,y):
        """_summary_
            initialise un poisson avec ses coordonnées x et y
        Args:
            x (_type_): position verticale
            y (_type_): position horizontale
        """
        self.x = x
        self.y = y

        self.ancien_x = x
        self.ancien_y = y

        self.compteur = 0

    def se_reproduire(self,bebe_list,class_de_poisson):
        """_summary_
            genere un nouveau poisson sur la case du poisson parent avant qu'il ne se deplace
        Args:
            bebe_list (_type_): liste de tous les nouveaux poissons generés sur le tour en cours
            class_de_poisson (_type_): class de l'instance. en l'occurence poisson ou requin
        """
        if self.compteur == self.nb_de_tour_pour_reproduction:
            # crée un enfant
            bebe = class_de_poisson(self.ancien_x, self.ancien_y)

            bebe_list.append(bebe)

            self.compteur = 0

    def choisir_une_cible_et_bouger(self,liste_voisins):
        """_summary_
            choisis une case aleatoirement
        Args:
            liste_voisins (_type_): listes des cases accessibles
        """
        cible = rd.choice(liste_voisins)
        # fait bouger le requin vers cette cible
        self.ancien_x = self.x
        self.ancien_y = self.y
        
        self.x = cible[0]
        self.y = cible[1] 


    def coord_voisins(self,grille):
        """_summary_
            regarde le contenu des cases au-dessus, en dessous, à gauche et à droite
        Args:
            grille (_type_): grille à utiliser

        Returns:
            _type_: retourne un dictionnaire contenant les coordonnées des cases alentour
        """
        if self.x !=0:
            up = (self.x-1,self.y)
        else:
            up = (grille.x_len-1,self.y)


        if self.x !=grille.x_len-1:
            down = (self.x+1,self.y)
        else:
            down = (0,self.y)

        if self.y !=0:
            left = (self.x,self.y-1)
        else:
            left = (self.x,grille.y_len-1)

        if self.y !=grille.y_len-1:
            right = (self.x,self.y+1)
        else:
            right = (self.x,0)

        dictionnaire_coord_voisin = {
            "up":up,
            "down":down,
            "right":right,
            "left":left
        }
        return dictionnaire_coord_voisin

    def move(self,grille,bebe_poisson_list):
        """_summary_
            deplace l'instance de poisson en verifiant les coordonnees des cases autour
            le fait se reproduire si le compteur est à 0
            
        Args:
            grille (_type_): grille à utiliser
            bebe_poisson_list (_type_): liste des poissons generes sur ce tour
        """
            # un tour à lieu pour le requin
        self.compteur+=1

            # Je recherche les coordonées des voisins
        dict_coord_voisin = self.coord_voisins(grille)


            # Trier les coordonnées des voisins en fonction de poisson et vide
        liste_des_cases_autour_vides = []


        for i , j in dict_coord_voisin.values():
            if grille.grille[i][j] == "░░":
                    liste_des_cases_autour_vides.append((i,j))

        if len(liste_des_cases_autour_vides)>0:
                
            self.choisir_une_cible_et_bouger(liste_des_cases_autour_vides)
                    
                
                # il se reproduit
            self.se_reproduire(bebe_poisson_list,Poisson)


class Requin(Poisson):

    energy_par_poisson = 0
    start_energy = 0
    
    def __init__(self,x,y):
        """_summary_
            genere un nouveau requin avec ses coordonnées x et y
        Args:
            x (_type_): sa position verticale
            y (_type_): sa position horizontale
        """
        super().__init__(x,y)

        self.energy = self.start_energy
        
    def manger(self,une_liste_de_poissons):
        """_summary_
            simule lesrequins qui mangent les poissons
            Redonne de l'energie aux requins
            Fais disparaitre les poissons mangés de la liste de tous les poissons et donc de la grille
        Args:
            une_liste_de_poissons (_type_): liste des poissons encore en vie
        """
         # ajouter et enlever de l'energie au requin
        self.energy += self.energy_par_poisson
            
            # faire disparaitre le poisson mangé de la liste de poissons
        for poisson in une_liste_de_poissons:
            if poisson.x == self.x and poisson.y == self.y:
                une_liste_de_poissons.remove(poisson)


    def mourir(self,une_liste_de_requins):
        """_summary_
            Si un requin n'a plus d'energie, il meurt et ses données sont effacées
        Args:
            une_liste_de_requins (_type_): liste des requins en vie
        """
        if self.energy == 0:
            une_liste_de_requins.remove(self)


    def move(self,grille:Grille,une_liste_de_poissons,bebe_requin_list,une_liste_de_requins):
        """_summary_
            Choisis le deplacement du requin
            Si au moins un thon est sur une case autor, il choisis en priorité une case aleatoire comportant un poisson
            Sinon si au moins une vase autour est vide il choisis une case aleatore vide
        Args:
            grille (Grille): grille à utiliser pour se deplacer
            une_liste_de_poissons (_type_): liste de tous les poissons encore en vie
            bebe_requin_list (_type_): liste des nouveaux requins generés sur ce tour
            une_liste_de_requins (_type_): liste des requins encore en vie
        """
        # un tour à lieu pour le requin il veillit et perd de l'energy
        self.compteur+=1
        self.energy -= 1


        # Je recherche les coordonées des voisins
        dict_coord_voisin = self.coord_voisins(grille)


        # Trier les coordonnées des voisins en fonction de poisson et vide
        liste_des_cases_autour_avec_du_poisson = []
        liste_des_cases_autour_vides = []


        for i , j in dict_coord_voisin.values():
            if grille.grille[i][j] == "🐟":
                liste_des_cases_autour_avec_du_poisson.append((i,j))
            elif grille.grille[i][j] == "░░":
                liste_des_cases_autour_vides.append((i,j))

        ########## si l'un des voisins c'est du poissons
        if len(liste_des_cases_autour_avec_du_poisson)>0:
            # choisi un des voisins poisson comme cible
            self.choisir_une_cible_et_bouger(liste_des_cases_autour_avec_du_poisson)

            # ajouter et enlever de l'energie au requin
            self.manger(une_liste_de_poissons)

            self.se_reproduire(bebe_requin_list,Requin)

            
        elif len(liste_des_cases_autour_vides)>0:
            
            # Je bouge vers une case vide
            self.choisir_une_cible_et_bouger(liste_des_cases_autour_vides)

            
            # il meurt
            self.mourir(une_liste_de_requins)
                
            
            # il se reproduit
            self.se_reproduire(bebe_requin_list,Requin)


        else:
            self.mourir(une_liste_de_requins)



            

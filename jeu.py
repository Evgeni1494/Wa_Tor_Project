from utils import Requin, Poisson, Grille
import random as rd



class Jeu:

    def __init__(self,x_len,y_len,nb_requins,nb_poissons,nb_de_tour_pour_reproduction_requin,nb_de_tour_pour_reproduction_poisson,energy_par_poisson,start_energy):
        self.x_len = x_len
        self.y_len = y_len
        self.nb_requins = nb_requins
        self.nb_poissons = nb_poissons
        self.nb_de_tour_pour_reproduction_requin = nb_de_tour_pour_reproduction_requin
        self.nb_de_tour_pour_reproduction_poisson = nb_de_tour_pour_reproduction_poisson
        self.energy_par_poisson = energy_par_poisson
        self.start_energy =  start_energy
        self.ma_grille = Grille(x_len,y_len)

    def create_animal_lists(self):
        mon_set=set()
        while len(mon_set) < self.nb_poissons + self.nb_requins:
            x = rd.randint(0,self.x_len-1)
            y = rd.randint(0,self.y_len-1)
            coord = (x,y)
            mon_set.add(coord)


            self.liste_poisson = []
            self.liste_requin = []



        for coord in list(mon_set)[0:self.nb_poissons]:
            self.liste_poisson.append( Poisson(coord[0],coord[1]))

        for coord in list(mon_set)[self.nb_poissons :  ]:
            self.liste_requin.append( Requin(coord[0],coord[1]))

    def initialisation_du_jeu(self):
        Requin.nb_de_tour_pour_reproduction = self.nb_de_tour_pour_reproduction_requin
        Requin.energy_par_poisson = self.energy_par_poisson
        Requin.start_energy = self.start_energy
        Poisson.nb_de_tour_pour_reproduction = self.nb_de_tour_pour_reproduction_poisson

        self.create_animal_lists()

        self.ma_grille.update(self.liste_poisson,self.liste_requin)

        print("----Initialisation -----")
        print("nb_requin",len(self.liste_poisson))
        print("nb_poisson",len(self.liste_requin))
        print(self.ma_grille)

    def lancer_le_jeu(self):
        
        self.initialisation_du_jeu()


        ###########LES TOURS
        jeu_non_termine = True

        self.tour = 0
        while jeu_non_termine:
            
            bebe_requin_list=[]
            for requin in self.liste_requin:
                requin.move(self.ma_grille,self.liste_poisson,bebe_requin_list,self.liste_requin)
                jonction_requin = self.liste_requin + bebe_requin_list
                self.ma_grille.update(self.liste_poisson,jonction_requin)

            self.liste_requin.extend(bebe_requin_list)


            bebe_poisson_list=[]
            for poisson in self.liste_poisson:  
                poisson.move(self.ma_grille,bebe_poisson_list)
                jonction_poisson = self.liste_poisson + bebe_poisson_list
                self.ma_grille.update(jonction_poisson,self.liste_requin)

            self.liste_poisson.extend(bebe_poisson_list)

            
            self.tour +=1
            print("------tour ",self.tour," -------")
            print(self.ma_grille)
            ### Analyse de la fin de jeu:

            if len(self.liste_poisson) == 0:
                print("TOus les poissons sont morts, le jeu est fini")
                print (" tour ", self.tour)
                jeu_non_termine = False
            elif len(self.liste_requin) == 0:
                print("tous les requins sont morts")
                print (" tour ", self.tour)
                jeu_non_termine = False
            elif self.tour == 150:
                print("Vous avez attient le tour 150, cest un bel équilibre")
                jeu_non_termine = False


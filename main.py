from jeu import Jeu

#parametres initiaux 
dictionnaire_de_param = {
    "x_len" : 30, #hauteur de la grille
    "y_len" : 50, #largeur de la grille
    "nb_requins" : 10, 
    "nb_poissons" : 200, 
    "nb_de_tour_pour_reproduction_requin" : 15, 
    "nb_de_tour_pour_reproduction_poisson" : 10,
    "energy_par_poisson" : 2, 
    "start_energy" :  5
}

mon_jeu =Jeu(**dictionnaire_de_param)

mon_jeu.lancer_le_jeu()
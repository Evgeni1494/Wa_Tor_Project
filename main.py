from jeu import Jeu

dictionnaire_de_param = {
    "x_len" : 20,
    "y_len" : 20,
    "nb_requins" : 10,
    "nb_poissons" : 80,
    "nb_de_tour_pour_reproduction_requin" : 9,
    "nb_de_tour_pour_reproduction_poisson" : 2,
    "energy_par_poisson" : 3,
    "start_energy" :  4
}

mon_jeu =Jeu(**dictionnaire_de_param)

mon_jeu.lancer_le_jeu()
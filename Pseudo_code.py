Classe Grille:
    - Attributs : grille (liste de listes d'objets de la classe Case), taille_x, taille_y
    - Méthodes : 
        - initialiser() : crée la grille avec des cases vides et des poissons et des requins aléatoirement
        - afficher() : affiche la grille dans la console
        - tour() : effectue un tour de jeu en faisant bouger les poissons et les requins
        - fin() : vérifie si la partie est terminée

Classe Case:
    - Attributs : est_vide (bool), est_poisson (bool), est_requin (bool)
    - Méthodes : 
        - initialiser() : crée une case vide
        - placer_poisson() : place un poisson sur la case
        - placer_requin() : place un requin sur la case
        - est_vide() : renvoie si la case est vide

Classe Poisson:
    - Attributs : position (objet de la classe Case)
    - Méthodes : 
        - initialiser() : crée un poisson
        - se_deplacer() : fait bouger le poisson vers une case vide adjacente
        - se_reproduire() : crée un nouveau poisson sur une case vide adjacente
        - mourir() : supprime le poisson de la grille

Classe Requin:
    - Attributs : position (objet de la classe Case), nourriture (entier)
    - Méthodes : 
        - initialiser() : crée un requin
        - se_deplacer() : fait bouger le requin vers une case avec un poisson
        - se_reproduire() : crée un nouveau requin sur une case vide adjacente
        - manger() : incrémente la nourriture du requin et supprime le poisson de la grille
        - mourir() : supprime le requin de la grille

programme principal:
    - crée une instance de la classe Grille
    - appelle la méthode initialiser() pour créer la grille initiale
    - tant que la partie n'est pas finie :
        - appelle la méthode tour() pour faire bouger les poissons et les requins
        - appelle la méthode afficher() pour afficher la grille à chaque tour
    - affiche un message de fin de jeu


La classe Grille gère la logique globale du jeu. 
Elle a des attributs tels que la grille elle-même (qui est une liste de listes d'objets de la classe Case), 
la taille en x et en y de la grille. Elle a des méthodes pour initialiser la grille, afficher la grille, 
effectuer un tour de jeu et vérifier si la partie est terminée.

La classe Case gère chaque case individuelle sur la grille. 
Elle a des attributs tels que si la case est vide, si elle contient un poisson ou un requin. 
Elle a des méthodes pour initialiser une case vide, placer un poisson ou un requin sur la case, 
et vérifier si la case est vide.

La classe Poisson gère chaque poisson individuel sur la grille. 
Il a un attribut qui est la position qui est un objet de la classe Case. 
Il a des méthodes pour initialiser un poisson, se déplacer vers une case vide adjacente, 
se reproduire en créant un nouveau poisson sur une case vide adjacente, et mourir en supprimant le poisson de la grille.

La classe Requin gère chaque requin individuel sur la grille. 
Il a un attribut qui est la position qui est un objet de la classe Case, 
et un autre qui est la nourriture qu'il a mangé. Il a des méthodes pour initialiser un requin, 
se déplacer vers une case avec un poisson, se reproduire en créant un nouveau requin sur une case vide adjacente, 
manger un poisson et incrémenter sa nourriture, et mourir en supprimant le requin de la grille.

Le programme principal crée une instance de la classe Grille, appelle la méthode initialiser pour créer la grille initiale, 
puis effectue un boucle tant que la partie n'est pas finie. 
A chaque tour, il appelle la méthode tour pour faire bouger les poissons et les requins, 
et la méthode afficher pour afficher la grille. Enfin, il affiche un message de fin de jeu.
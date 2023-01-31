# Wa_Tor_Project

Ce projet a était réalisé dans le cadre de la formation Tech IA par David Dylan Dominique et Evgeni.

# Présentation

Ce projet vise a crée une "simulation" basique de comportement basé sur quelque comportements prédéfini a l'aide de Python.

Plus précisement on aura une population de "Thon" et de "Requin" qui seront placé sur une planete de forme toroidale : Wa-Tor. Wa-tor est representé sous forme d'une grille a l'interieur de la quel les poissons peuvent intéragir.

# Thon

    - Le thon possede la capacité de se reproduire et se déplacer sur une case vide.
        - La reproduction se fait aprés un certain nombre de tours (compteur de reproduction).
        - Si le poisson est prét a se reproduire :
            - A son prochain déplacement il laissera sur la case précédente un nouveau poisson du meme type.
    - il ne peut pas mourir si il ne lui arrive rien.

# Requin

    - Le requin possede la capacité de se reproduire et se déplacer sur une case vide.
        - Il va priviligié les cases avec des Thons.
    - La reproduction se fait aprés un certain nombre de tours (compteur de reproduction).
        - Si le poisson est prét a se reproduire :
            - A son prochain déplacement il laissera sur la case précédente un nouveau poisson du meme type.
    - Il possede une reserve d'énergie.
        - Si la réserve arrive a 0 le requin meurt.
    - A chaque fois qu'il reussi a se déplacer sur une case avec un Thon :
        - Il regagne un certain montant d'énergie.
        - Le Thon de cette case meurt.
    
# Lancement

    Pour lancer la simulation vous devez executer le fichier main.py
        - a l'interieur de celui si vous trouverez également un dictionnaire :
            - Vous pouvez configurer la simulation selon un nombre de parametres afin d'ajuster celle si.
            


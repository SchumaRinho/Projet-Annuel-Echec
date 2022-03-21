# Projet Annuel Echec

Projet réalise par Léo LAUNEY et Léo VINCENT

## Structure du Programme

Notre code est composé de :

- FENChess.py : Extrait les FEN du fichier pgn.
- FENAnalyse.py : Analyse les FEN issu de FENChess.
- main.py : Lance les script python et retranscris les résultats dans un fichier txt *Resultats.txt*
- Resultat.txt : Comporte diverse statistique sur les fichiers pgn analysés.

## Pour lancer le script

Soit vous lancer main.py depuis IDLE classiquement. Soit depuis une console en tapant *python main.py* dans la racine du projet.
Il est nécessaire de mettre vos fichiers pgn à analyser dans le fichier PGNFile. Il seront tous parser.

**ATTENTION** : Notre programme manque d'optimisation pour les grosses base de données. Nous estimons notre analyse à un peu moins de 100 FEN par secondes.

## Autres fichiers

- beta : Le fichier *FEN.py* permet de parser les fichiers PGN sans la librairie chess de python. Mais après certains problèmes rencontrés, nous utilisons la librairie chess dans la version finale.
- Terminal : Permet de faire tourner le programme sans main. il se fait a partir de *FENAnalyse.py*. Certaines infos s'affichent dans le terminal contrairement à la version main. Vous pouvez notamment voire l'avancer du programme. Pour éxecuter via terminal : *python FENAnalyse.py* depuis le dossier terminal.

## Nous contacter

Pour tous problèmes, nous contacter à cet adresse mail : 21805239@unicaen.fr.
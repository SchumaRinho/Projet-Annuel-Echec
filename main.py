print("veuillez patienter. Le script a des soucis d'optimisation...")

import FENAnalyse

FenIsMoreCheckB3,FenIsMoreCheckW3 = FENAnalyse.getFenIsMoreCheck()

fenIsMoreCheckMateB3,fenIsMoreCheckMateW3 = FENAnalyse.getFenIsMoreCheckMate()

moveMakeMoreCheckB3,moveMakeMoreCheckW3 = FENAnalyse.getMoveMakeMoreCheck()

moveMakeMoreCheckMateB3,moveMakeMoreCheckMateW3 = FENAnalyse.getMoveMakeMoreCheckMate()

gRoqueMate,pRoqueMate,enPassantMate = FENAnalyse.getMateSpecial()

exempleGR,exemplePR,exempleEP = FENAnalyse.getExempleMateSpecial()

nbGames = FENAnalyse.getNbGames()

res = open("Resultat.txt","w")
res.write("L'analyse a été faite sur "+str(nbGames)+" partie(s).\n\n")
res.write("Voici divers statistiques sur le fichier pgn que vous venez d'analyser\n\n\n")
res.write("Les 3 FEN où le Roi noir est le plus souvent en échec :\n\n")

i=0
for k,v in FenIsMoreCheckB3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 FEN où le Roi blanc est le plus souvent en échec :\n\n")

i=0
for k,v in FenIsMoreCheckW3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 FEN où le Roi noir est le plus souvent en échec et mat :\n\n")

i=0
for k,v in fenIsMoreCheckMateB3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 FEN où le Roi blanc est le plus souvent en échec et mat :\n\n")

i=0
for k,v in fenIsMoreCheckMateW3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 coups qui peut mettre le Roi noir le plus souvent en échec :\n\n")

i=0
for k,v in moveMakeMoreCheckB3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 coups qui peut mettre le Roi blanc le plus souvent en échec :\n\n")

i=0
for k,v in moveMakeMoreCheckW3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 coups qui peut mettre le Roi noir le plus souvent en échec :\n\n")

i=0
for k,v in moveMakeMoreCheckMateB3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")
res.write("\n\n")
res.write("Les 3 coups qui peut mettre le Roi blanc le plus souvent en échec et mat (Potentiellement faux):\n\n")

i=0
for k,v in moveMakeMoreCheckMateW3.items():
    i+=1
    res.write(str(i)+". "+str(k)+" , il est présent "+str(v)+" fois\n")

res.write("\n\n")
res.write("Mate spéciaux rencontrés :\n")
res.write("Nombre de mat avec petit Roque : "+str(pRoqueMate)+" sur "+str(nbGames)+"\n")
if pRoqueMate!=0:
    res.write("Voici un exemple de partie : "+str(exemplePR)+"\n")
res.write("\n")

res.write("Nombre de mat avec grand Roque : "+str(gRoqueMate)+" sur "+str(nbGames)+"\n")
if gRoqueMate!=0:
    res.write("Voici un exemple de partie : "+str(exempleGR)+"\n")
res.write("\n")

res.write("Nombre de mat avec en passant : "+str(enPassantMate)+" sur "+str(nbGames)+"\n")
if enPassantMate!=0:
    res.write("Voici un exemple de partie : "+str(exempleEP)+"\n")
res.write("\n")

res.close()

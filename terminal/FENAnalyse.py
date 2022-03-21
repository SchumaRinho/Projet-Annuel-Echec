import string
import copy
import sys
import FENChess

################# LISTE LES MOUVEMENTS DIAGONAUX (REINE ET FOU) #####################

def diag(case,i,j,d,o = 0,start = []): 
    if o == 1:              # Détermine dans quelles
        coup = coupDefence  # listes doit-on ajouter
    else:                   # le coup (o -> oponnent)
        coup = coupAttaque  #
        
    if not start:           # On sauvegarde 
        start.append(i)     # les coorodonées
        start.append(j)     # de départ de la pièce
        
    vali=[i+1,i+1,i-1,i-1]  # Liste des mouvements que 
    valj=[j-1,j+1,j+1,j-1]  # la pièce peut faire
    
    for k in range(0,4):                                                # Pour chaque mouvement
        if d in (0,k+1) and 0<=vali[k]<=7 and 0<=valj[k]<=7:            # on vérifie si il reste dans l'echiquier
            if eval("table["+str(vali[k])+"]["+str(valj[k])+"]"+methO): # si oui, on vérifie s'il rencontre un adversaire 
                checkMate(case,vali[k],valj[k],start[0],start[1],coup)  # si oui, on vérifie si le coups fait echec( et mat)
            elif not table[vali[k]][valj[k]]:                           # sinon on vérifie s'il ne rencontre personne
                checkMate(case,vali[k],valj[k],start[0],start[1],coup)  # si c'est le cas, on vérifie si le coups fait echec( et mat)
                diag(case,vali[k],valj[k],k+1,o,start)                  # Et on relance la fonction jusqu'a rencontré un pièce adverse ou le bord de l'échiquier


################# LISTE LES MOUVEMENTS HORIZONTAUX/VERTICAUX (REINE ET TOUR) #####################

def vertHoriz(case,i,j,d,o = 0,start = []): #Fonctionnement identique à diag() mais pour des mouvements horizontaux/verticaux
    if o == 1:
        coup = coupDefence
    else:
        coup = coupAttaque
    if not start:
        start.append(i)
        start.append(j)
    vali=[i+1,i-1,i,i]
    valj=[j,j,j+1,j-1]
    
    for mouv in range(0,4):
        if d in (0,mouv+1) and 0<=vali[mouv]<=7 and 0<=valj[mouv]<=7:
            if eval("table["+str(vali[mouv])+"]["+str(valj[mouv])+"]"+methO):
                checkMate(case,vali[mouv],valj[mouv],start[0],start[1],coup)
            elif not table[vali[mouv]][valj[mouv]]:
                checkMate(case,vali[mouv],valj[mouv],start[0],start[1],coup)
                vertHoriz(case,vali[mouv],valj[mouv],mouv+1,o,start)    

################# LISTE LES MOUVEMENTS DES CAVALIERS #####################

def knight(case,i,j,o = 0): #Fonctionnement identique à diag() mais pour les mouvements du cavalier
    if o == 1:
        coup = coupDefence
    else:
        coup = coupAttaque

    vali=[i+2,i+2,i-2,i-2,i-1,i+1,i-1,i+1]
    valj=[j-1,j+1,j-1,j+1,j+2,j+2,j-2,j-2]
    
    for k in range(len(vali)):
        if(
            0<=vali[k]<=7
            and 0<=valj[k]<=7
            and (eval("table["+str(vali[k])+"]["+str(valj[k])+"]"+methO) or not table[vali[k]][valj[k]])
        ):
            checkMate(case,vali[k],valj[k],i,j,coup) # Non récursive car les mouvements du cavalier sont limités


################# LISTE LES MOUVEMENTS DES PIONS #####################


def pion(case,i,j,o = 0):
    if o == 1:
        coup = coupDefence
    else:
        coup = coupAttaque
        
    if case.isupper(): #si la pièce est en majuscule, c'est un pion blanc, donc déplacement vers le haut
        if i == 6: #si la pièce n'a pas bougé on vérifie si elle peut avancer de 1 ou 2 cases
            if not table[i-1][j]:  
                checkMate(case,i-1,j,i,j,coup)
                if not table[i-2][j]:
                    checkMate(case,i-2,j,i,j,coup)
        elif not table[i-1][j]: #sinon on vérifie juste si elle peut avancer de 1 case
            checkMate(case,i-1,j,i,j,coup)
        if i-1>=0 and j+1<=7 and table[i-1][j+1].islower(): #on vérifie si a une pièce adverse dans la diagonale droite
            checkMate(case,i-1,j+1,i,j,coup)
        if i-1>=0 and j-1>=0 and table[i-1][j-1].islower(): #puis dans la diagonale gauche
            checkMate(case,i-1,j-1,i,j,coup)
    else:    #Meme chose pour le pion noir (avec un déplacement vers le bas cette fois-ci)
        if i == 1:
            if not table[i+1][j]:
                checkMate(case,i+1,j,i,j,coup)
                if not table[i+2][j]:
                    checkMate(case,i+2,j,i,j,coup)
        elif not table[i+1][j]:
            checkMate(case,i+1,j,i,j,coup)
        if i+1<=7 and j+1<=7 and table[i+1][j+1].isupper():
            checkMate(case,i+1,j+1,i,j,coup)
        if i+1<=7 and j-1>=0 and table[i+1][j-1].isupper():
            checkMate(case,i+1,j-1,i,j,coup)
    

################# LISTE LES MOUVEMENTS DU ROI #####################

def king(case,tablePreview=0,o = 0):
    if not tablePreview:
        tablePreview = table
    if o == 1:
        coup = coupDefence
    else:
        coup = coupAttaque
        
    if case.isupper(): #On connais déja la place du roi grâce au calcul fais dans le main en bas
        i = K[0]
        j = K[1]
    else:
        i = k[0]
        j = k[1]                
    vali=[i+1,i+1,i,i-1,i-1,i-1,i,i+1] 
    valj=[j,j-1,j-1,j-1,j,j+1,j+1,j+1]
    for mouv in range(len(vali)):
        if (
            0<=vali[mouv]<=7                                                            # On vérifie:
            and 0<=valj[mouv]<=7                                                        # - Si on est dans les limites
            and (eval("tablePreview["+str(vali[mouv])+"]["+str(valj[mouv])+"]"+methO)# - Si on a une pièce adverse dans la direction
            or not tablePreview[vali[mouv]][valj[mouv]])                                # - ou si on a aucune pièce dans la direction 
            and not isCheck(case,vali[mouv],valj[mouv],-1,methO,tablePreview,0)      # - si le roi n'est pas en echec en prenant cette direction
        ):
            coup.append([vali[mouv],valj[mouv],i,j,'',[],[],case])                      # On ne fait pas la verif d'echec et mat car c'est un roi, on ajoute le coup directement

################### Coups en passant possible ###################

def enPassant(): 
    pos = list(string.ascii_lowercase) #on crée un dico pour représenter les colones d'un échiquier 
    del pos[8:]
    if table[-1][1] == "3":
        for col in range(len(pos)):
            if pos[col] == table[-1][0]:                                            #on vérifie si la dernière partie du plateau 
                if 0<=col-1 and table[4][col-1]=="p":                               #(correspondant au coup en passant),
                    checkMate(table[4][col-1],5,col,4,col-1,coupAttaque,ep=[4,col]) #peut être fais. En récupérant la ligne et la
                if 7>=col+1 and table[4][col+1]=="p":                               #colonne, on regarde si il y a un pion sur cette case
                    checkMate(table[4][col+1],5,col,4,col+1,coupAttaque,ep=[4,col])
    else:
        for col in range(len(pos)):
            if pos[col] == table[-1][0]:
                if 0<=col-1 and table[3][col-1]=="P":
                    checkMate(table[3][col-1],2,col,3,col-1,coupAttaque,ep=[3,col]) 
                if 7>=col+1 and table[3][col+1]=="P":
                    checkMate(table[3][col+1],2,col,3,col+1,coupAttaque,ep=[3,col])


################### ROQUE POSSIBLE ############################
    
def roque():
    if player == "w": #si c'est le joueur blanc 
        if "K" in table[-2][0]: #on regarde si dans l'avant derniere catégorie du plateau(celle des roques possibles) le roi blanc y est 
            if table[7][1]==table[7][2]==table[7][3]=='':                   # si oui, on vérifie si les cases à gauche sont libres,
                checkMate('K',7,2,7,4,coupAttaque,rq=[7,3,7,0,'R','O-O-O'])
            if table[7][5]==table[7][6]=='':                                # et celle de droite aussi,              
                checkMate('K',7,6,7,4,coupAttaque,rq=[7,5,7,7,'R','O-O'])
    else: #idem mais pour le joueur noir
        if "q" == table[-2][-1]:
            if table[0][1]==table[0][2]==table[0][3]=='':
                checkMate('k',0,2,0,4,coupAttaque,rq=[0,3,0,0,'r','o-o-o'])
            if table[0][5]==table[0][6]=='':
                checkMate('k',0,6,0,4,coupAttaque,rq=[0,5,0,7,'r','o-o'])
################### SI ROI ADVERSE EN ECHEC, VERIFIE SI IL PEUT SE DEFENDRE ################   

def canMakeDefenseMove(case,casei,casej,tablePreview,OppcaseK,kOpponent):
    global coupDefence # On rapelle les méthodes du main pour éviter toute erreur
    global meth
    global methO
    
    coupDefenceA = coupDefence.copy() #On copie les coupdeDefence pour pouvoir en ajouter temporairement
    
    if case.isupper():                                                          #
        if 0<=casei-1 and 0<=casej-1 and tablePreview[casei-1][casej-1] == "p": #
            coupDefenceA.append([casei,casej,casei-1,casej-1,"",[],[],"p"])     #
        if 0<=casei-1 and casej+1<=7 and tablePreview[casei-1][casej+1] == "p": #
            coupDefenceA.append([casei,casej,casei-1,casej+1,"",[],[],"p"])     #   On vérifie si la 
    else:                                                                       #   pièce peut être attaqué par 
        if casei+1<=7 and 0<=casej-1 and tablePreview[casei+1][casej-1] == "P": #   un pion adverse
            coupDefenceA.append([casei,casej,casei+1,casej-1,"",[],[],"p"])     #
        if casei+1<=7 and casej+1<=7 and tablePreview[casei+1][casej+1] == "P": #
            coupDefenceA.append([casei,casej,casei+1,casej+1,"",[],[],"p"])     #
    for i in coupDefenceA:
        moveFeasible = True
        tablePreviewD = copy.deepcopy(tablePreview)
        if (i[-1] in ('p','P') and i[1] == i[3]):  # Si la pièce se met devant 
            if tablePreviewD[i[0]][i[1]] == case:  # un pion adverse, on ignore
                moveFeasible = False               # le coup du pion            
        if moveFeasible:                                            # Si le mouvement est faisable
            tablePreviewD[i[0]][i[1]] = tablePreviewD[i[2]][i[3]]   # On réalise le mouvement dans un tableau fictif
            tablePreviewD[i[2]][i[3]] = ""
            if i[5]:
                tablePreviewD[i[5][0]][i[5][1]] = "" 
            if i[6]:
                tablePreviewD[i[6][0]][i[6][1]] = i[6][-2]
                tablePreviewD[i[6][2]][i[6][3]] = ""
            if not isCheck(OppcaseK,kOpponent[0],kOpponent[1],-1,meth,tablePreviewD,0): #et on vérifie si le roi adverse n'est pas en echec 
                return True 
##            if i[2]==casei and i[3]==casej:
##                meth,methO = echange(meth,methO)
##                coupDefence.clear()
##                parcousPlateau(0,tablePreview)
##                madeADefenceMove = canMakeDefenseMove(case,casei,casej,tablePreview,OppcaseK,kOpponent)
##                meth,methO = echange(meth,methO)
##                coupDefence = coupDefenceA.copy()
##                if madeADefenceMove:
##                    return True
    #si on arrive ici c'est que le roi ne peut pas se défendre. Echec et mat 
    return False

############### VERIFIE SI LE ROI EST MAT ####################

def checkMate(case,i,j,exi,exj,coup,ep=[],rq=[]):
    if case.isupper():  #On resupère les coo des rois 
        kOpponent = k
        kMine = K
        OppcaseK = "k"
        MincaseK = "K"
    else:
        kOpponent = K
        kMine = k
        OppcaseK = "K"
        MincaseK = "k"
    tablePreview = copy.deepcopy(table)
    tablePreview[i][j] = tablePreview[exi][exj]
    tablePreview[exi][exj] = ""
    if ep:                              #si c'est un coup en passant on efface la pièce manger
        tablePreview[ep[0]][ep[1]] = ""
    if rq:                              #si c'est un roque, on déplace la tour
        tablePreview[rq[0]][rq[1]] = rq[-2]
        tablePreview[rq[2]][rq[3]] = ""
    if not isCheck(MincaseK,kMine[0],kMine[1],-1,methO,tablePreview,0): #On vérifie que le coup ne met pas en echec le roi du joueur
        if(not rq) or (not isCheck(case,i,j,-1,methO,tablePreview,0)):
            if coup!=coupDefence and isCheck(OppcaseK,kOpponent[0],kOpponent[1],-1,meth,tablePreview,0): #On vérifie si c'est coup du joueur et si il met en echec le roi adverse
                if not canMakeDefenseMove(case,i,j,tablePreview,OppcaseK,kOpponent): #si il le met en echec on regarde, si il peut se défendre
                    coup.append([i,j,exi,exj,"#",ep,rq,case]) #si non echec et mat
                else:
                    coup.append([i,j,exi,exj,"+",ep,rq,case]) #sinon juste echec
            else:
                coup.append([i,j,exi,exj,"",ep,rq,case])
            
############### VERIFIE SI LE ROI EST EN ECHEC ####################

def isCheck(case,i,j,d,methChek,tablePreview=0,rec=1):
    if not tablePreview:
        tablePreview = copy.deepcopy(table)
    if case.isupper():
        p1=[i-1,j-1]                #Direction : d=-1 toute direction
        p2=[i-1,j+1]                #d=0 en bas, d=1 bas gauche et ainsi de suite 
        p="p"                       #sans des aiguilles d'une montre
        n="n"
    else:
        p1=[i+1,j-1]
        p2=[i+1,j+1]
        p="P"
        n="N"
    vali=[i+1,i+1,i,i-1,i-1,i-1,i,i+1]
    valj=[j,j-1,j-1,j-1,j,j+1,j+1,j+1]
    for mouv in range(len(vali)):
        if d in (-1,mouv) and 0<=vali[mouv]<=7 and 0<=valj[mouv]<=7:
            isOpponent = eval("tablePreview["+str(vali[mouv])+"]["+str(valj[mouv])+"]"+methChek)
            if d==-1: #on vérifie si dans la postion initiale  on est sous l'influance d'un pion acdverse
                if (0<=p1[0]<=7 and 0<=p1[1]<=7 and tablePreview[p1[0]][p1[1]]==p) or (0<=p2[0]<=7 and 0<=p2[1]<=7 and tablePreview[p2[0]][p2[1]]==p):
                    return True
            if (d%2==0 or (d==-1 and mouv%2==0)) and isOpponent and tablePreview[vali[mouv]][valj[mouv]] in ("q","Q","r","R"):
                return True #On vérifie toute les directions pairs car corresponds a bas gauche haut droite (pour la reine et la Tour)
            if ((d!=-1 and d%2!=0) or (d==-1 and mouv%2!=0)) and isOpponent and tablePreview[vali[mouv]][valj[mouv]] in ("q","Q","b","B"):
                return True #On vérifie toute les directions impairs car corresponds aux diagonales (pour la reine et le fou)
            if not tablePreview[vali[mouv]][valj[mouv]]:
                if isCheck(case,vali[mouv],valj[mouv],mouv,methChek,tablePreview=tablePreview):
                    return True
    if not rec:  #on vérifie le cavalier a part seulement dans la position initiale          
        vali=[i-1,i-1,i,i+1,i+1,i+1,i,i-1]
        valj=[j,j+1,j+1,j+1,j,j-1,j-1,j-1]
        if d==-1 or tablePreview[vali[d]][valj[d]]==case:
            valNi=[i+2,i+2,i-2,i-2,i-1,i+1,i-1,i+1]
            valNj=[j-1,j+1,j-1,j+1,j+2,j+2,j-2,j-2]

            for mouv in range(len(vali)):
                if 0<=valNi[mouv]<=7 and 0<=valNj[mouv]<=7:
                    isOpponent = eval("tablePreview["+str(valNi[mouv])+"]["+str(valNj[mouv])+"]"+methChek)
                    if isOpponent and tablePreview[valNi[mouv]][valNj[mouv]]==n:
                        return True
    return False #si on est ici, c'est que le roi n'est pas en echec

   
################### CONVERTIR LES COUPS DANS LA LISTE PAR RAPPORT A LA NOTATION STANDARD ###################

def conv(fen,moveMakeMoreCheck,checkmate):
    if checkmate:       #en fonction de si on veut les coups qui ont fais echec ou echec et mate
        verif = "#"
    else:
        verif = "+"
    ligne=[8,7,6,5,4,3,2,1]
    pos = list(string.ascii_lowercase)
    for i in range(len(coupAttaque)):
        if coupAttaque[i][4] == verif:
            if coupAttaque[i][-1] in ('p','P'):
                if coupAttaque[i][1]==coupAttaque[i][3]:
                    move = str(pos[coupAttaque[i][1]])+str(ligne[coupAttaque[i][0]])
                else:
                    move = str(pos[coupAttaque[i][3]])+"x"+str(pos[coupAttaque[i][1]])+str(ligne[coupAttaque[i][0]])+str(coupAttaque[i][-1])
            elif coupAttaque[i][-1] in ('r','R','b','B','q','Q','n','N'):
                move = str(coupAttaque[i][-1])+str(pos[coupAttaque[i][3]])+str(ligne[coupAttaque[i][2]])+str(pos[coupAttaque[i][1]])+str(ligne[coupAttaque[i][0]])
            elif coupAttaque[i][-2]:
                move = str(coupAttaque[i][-2][-1])
            elif coupAttaque[i][-3]:
                move = str(pos[coupAttaque[i][2]])+"x"+str(pos[coupAttaque[i][1]])+str(ligne[coupAttaque[i][0]])+str(coupAttaque[i][-1])+'e.p'
            else:
                move = str(coupAttaque[i][-1])+str(pos[coupAttaque[i][1]])+str(ligne[coupAttaque[i][0]])

            if move in moveMakeMoreCheck: #Si le coup est dans le dico on augmente son occurence
                moveMakeMoreCheck[move]+=1
            else:                         #Sinon on l'ajoute
                moveMakeMoreCheck[move]=1
                
############### TRI STATISTIQUE ###################
def top3sorted(dic): #On tri par odre décroissant et affiche les 3 premiers
    tmp = dic.copy()
    dic = dict(sorted(tmp.items(), reverse=True, key=lambda item: item[1]))
    tmp = dic.copy()
    z=0
    for fenCheckB in tmp.keys():
        z+=1
        if z >= 4:
            del dic[fenCheckB]
    return dic

def makeStat(dic):
    dic = top3sorted(dic)
    return dic
################# GETTERS POUR LE MAIN ###############
def getFenIsMoreCheckMate():
    return (makeStat(fenIsMoreCheckMateB3),makeStat(fenIsMoreCheckMateW3))

def getFenIsMoreCheck():
    return (makeStat(fenIsMoreCheckB3),makeStat(fenIsMoreCheckW3))

def getMoveMakeMoreCheckMate():
    return (makeStat(moveMakeMoreCheckMateB3),makeStat(moveMakeMoreCheckMateW3))

def getMoveMakeMoreCheck():
    return (makeStat(moveMakeMoreCheckB3),makeStat(moveMakeMoreCheckW3))

################ PARCOURS PLATEAU #########################
def parcousPlateau(o,table):
    for i in range(len(table)):
        if i <=7 :
            for j in range(len(table[i])):
                case = table[i][j]
                if eval("case"+meth) and case in ("q","b","Q","B"):
                    diag(case,i,j,0,o)
                if eval("case"+meth) and case in ("q","r","Q","R"):
                    vertHoriz(case,i,j,0,o)
                if eval("case"+meth) and case in ("n","N"):
                    knight(case,i,j,o)
                if eval("case"+meth) and case in ("p","P"):
                    pion(case,i,j,o)
                if eval("case"+meth) and case in ("k","K"):
                    king(case,o=o)
    if not o and not table[-1][0] == '-':
        enPassant()
    roque()
################ ECHANGE METHODE ANALYSE (ex: calculer les coups défensif)
def echange(meth1,meth2):
    tmpMeth = meth1
    meth1 = meth2
    meth2 = tmpMeth
    return (meth1,meth2)


################### MAIN ###################
FENList = FENChess.FENGenerator()
print("Nombre de FEN à analyser :",len(FENList))

if not FENList:
    print("Il n'y a aucun fen à analyser")

fenIsMoreCheckMateB3 = {}
fenIsMoreCheckMateW3 = {}

fenIsMoreCheckB3 = {}
fenIsMoreCheckW3 = {}

moveMakeMoreCheckB3 = {}
moveMakeMoreCheckW3 = {}

moveMakeMoreCheckMateB3 = {}
moveMakeMoreCheckMateW3 = {}
tmptime = 0

table=[]

##print("Total de FEN à analyser :",len(FENList))

for FEN,occ in FENList.items():
    tmptime += 1
    if FEN:
        coupAttaque=[]
        coupDefence=[]
        j=i=-1
        ################### CONVERSION DU FEN EN TAB 2 DIMENSION ########################
        table.clear()
        while i!=len(FEN)-1:
            table.append([])
            j+=1
            while i!=len(FEN)-1:
                i+=1
                case = FEN[i]
                if case in ("/"," "):
                    break
                elif case.isdigit() and i!=len(FEN)-1:
                    for z in range(int(case)):
                        table[j].append("")
                else:
                    table[j].append(case)

        ################### VERIFICATION SI LE ROI EST EN ECHEC #######################
        player = table[8][0]

        if player == "w":
            meth = ".isupper()"
            methO = ".islower()"
        else:
            methO = ".isupper()"
            meth = ".islower()"

        for i in range(len(table)):
            for j in range(len(table[i])):
                case = table[i][j]
                if case in ("k","K") and i<=7:
                    exec("%s = %s" % (case,[i,j]))
                    if case == 'k':
                        currentCheckPositionB = isCheck(case,k[0],k[1],-1,".isupper()",rec=0)
                    else :
                        currentCheckPositionW = isCheck(case,K[0],K[1],-1,".islower()",rec=0)

        ################### PARCOURIR LE TABLEAU POUR LISTER LES MOUVEMENTS DE TOUTES LES PIECES ADVERSAIRE (POUR DEFENDRE LE ROI ADVERSE)########################
        meth,methO = echange(meth,methO)

        parcousPlateau(1,table)
        ################### PARCOURIR LE TABLEAU POUR LISTER LES MOUVEMENTS DE TOUTES LES PIECES DU JOUEUR ACTUEL ########################
        meth,methO = echange(meth,methO)
        
        parcousPlateau(0,table)
        ################## TOP 3 FEN FAISANT LE PLUS ECHEC ET ECHEC ET MAT###################
        if currentCheckPositionB :
            if not coupAttaque:
                fenIsMoreCheckMateB3[FEN]=occ
            else:
                fenIsMoreCheckB3[FEN]=occ
            
                
        elif currentCheckPositionW :
            if not coupAttaque:
                fenIsMoreCheckMateW3[FEN]=occ
            else:
                fenIsMoreCheckW3[FEN]=occ
                
            
        ################## TOP 3 COUPS FAISANT LE PLUS ECHEC ET ECHEC ET MAT###################
        if player=="w":
            conv(FEN,moveMakeMoreCheckMateB3,True)
            conv(FEN,moveMakeMoreCheckB3,False)
        else:
            conv(FEN,moveMakeMoreCheckMateW3,True)
            conv(FEN,moveMakeMoreCheckW3,False)
        if tmptime%100==0:
            print(tmptime,"/",len(FENList))
    #reverfier les coups quand une pièce mange une autre
print(getFenIsMoreCheck())
print(getFenIsMoreCheckMate())
print(getMoveMakeMoreCheck())
print(getMoveMakeMoreCheckMate())

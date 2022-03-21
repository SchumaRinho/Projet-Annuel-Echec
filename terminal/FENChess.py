import chess
import chess.pgn
import io
import string
import re
import os

##### PROGRAMME REALISER AVEC LA LIBRAIRIE CHESS DE PYTHON##########

poss = {} #dico des positions FEN
lsdir = os.listdir("../PGNFile")

num = [i for i in range(1,9)]
pos = list(string.ascii_lowercase)
del pos[8:]

gRoqueMate=pRoqueMate=enPassantMate=0
exempleGR=exemplePR=exempleEP=""
nbGames=0

def getNbGames():
    return nbGames

def getMateSpecial():
    return(gRoqueMate,pRoqueMate,enPassantMate)

def getExempleMateSpecial():
    return(exempleGR,exemplePR,exempleEP)

def roqueCheck(game): #Analyse si la partie c'est terminé sur roque en echec et mat
    gametmp = re.sub('({.*?})','',game)
    if "O-O-O#" in gametmp:
        gRoqueMate+=1
        if not exempleGR:
            exempleGR = gametmp
    elif "O-O#" in gametmp:
        pRoqueMate+=1
        if not exemplePR:
            exemplePR = gametmp
        
def enPassantCheck(game): #Analyse si la partie c'est terminé sur un coup en passant en echec et mat
    gametmp = re.sub('({.*?})|(\d+\..?[^a-zA-Z])','',game) #regexp permettant de supprimer les parties obsolète du pgn
    for i in range(len(pos)):
        if (not i-1<0 and (" "+pos[i-1]+"4   "+pos[i]+"x"+pos[i-1]+"3#" in gametmp)):
            exempleEP = re.sub('({.*?})','',game)
            EnPassantMate+=1
        elif (not i-1<0 and (" "+pos[i-1]+"5  "+pos[i]+"x"+pos[i-1]+"6#" in gametmp)):
            exempleEP = re.sub('({.*?})','',game)
            EnPassantMate+=1
        elif (i+1!=len(pos) and (" "+pos[i+1]+"4   "+pos[i]+"x"+pos[i+1]+"3#" in gametmp)):
            exempleEP = re.sub('({.*?})','',game)
            EnPassantMate+=1
        elif (i+1!=len(pos) and (" "+pos[i+1]+"5  "+pos[i]+"x"+pos[i+1]+"6#" in gametmp)):
            exempleEP = re.sub('({.*?})','',game)
            EnPassantMate+=1

def FENGenerator():
    for ls in lsdir:
        if ls.endswith(".pgn"):
            with open("../PGNFile/"+ls) as pgn:
                games = pgn.read()
            games = games.replace("\n\n[", "||||[")
            pgns = games.split("||||") #on récupert les coups et on les ségmentent
            nbGames = len(pgns)
        for pgn in pgns:
            game = chess.pgn.read_game(io.StringIO(pgn))
            if game.errors:
                continue

            while game:
                game = game.next()
                enPassantCheck(str(game))
                roqueCheck(str(game))
                if game:
                    board = game.board()
                    pos = board.fen().split(' ')[:-2] #Génération du FEN 
                    pos = ' '.join(pos)
                    if pos in poss: #Vérification si le FEN est déja enregistré
                        poss[pos] += 1
                    else:
                        poss[pos] = 1
        return poss
if __name__ == "__main__":
    FENGenerator()

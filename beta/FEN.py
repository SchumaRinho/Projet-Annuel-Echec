import re

baseFEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'


def posToCoor(pos):
    num = ['8','7','6','5','4','3','2','1']
    let = ['a','b','c','d','e','f','g','h']
    cor = 8*num.index(pos[-1]) + let.index(pos[0])
    return cor
    

def newFEN(fen,coup):
    pos = fen.split()[0]
    piece = pos.replace('/','')
    board = []
    for i in piece:
        if i.isdigit():
            for j in range(int(i)):
                board.append('_')
        else:
            board.append(i)
        
    if coup[0] in ['B','Q','K','B','R']:
        arr = coup[-2:]
        coor = posToCoor(arr)
        if coup[0] == 'K':
            if fen.split()[1] == 'w':
                board[board.index('K')] = '_'
                board[coor] = 'K'
            else:
                board[board.index('K')] = 'k'
                board[coor] = 'k'
        elif coup[0] == 'R':
            if fen.split()[1] == 'w':
                tmp = 'R'
            else:
                tmp = 'r'
                
            Piece = [i for i, x in enumerate(board) if x == tmp]
            for p in Piece:
                if p % 8 == coor % 8 or (p >= (coor - coor % 8) and p <= coor + (8 - coor % 8)):
                    board[p] = '_'
                    break
            board[coor] = tmp
            
        elif coup[0] == 'N':
            if fen.split()[1] == 'w':
                tmp = 'N'
            else:
                tmp = 'n'
            if coor > 7:
                if coor > 15:
                    if coor % 8 > 0:
                        if board[coor - 17] == tmp:
                            board[coor - 17] = '_'
                        
                    if coor % 8 < 7:
                        if board[coor - 15] == tmp:
                            board[coor - 15] = '_'
                        
                if coor % 8 > 1:
                    if board[coor - 10] == tmp:
                        board[coor - 10] = '_'
                    
                if coor % 8 < 6:
                    if board[coor - 6] == tmp:
                        board[coor - 6] = '_'
                    
            if coor < 55:
                if coor < 47:
                    if coor % 8 > 0:
                        if board[coor + 15] == tmp:
                            board[coor + 15] = '_'
                        
                    if coor % 8 < 7:
                        if board[coor + 17] == tmp:
                            board[coor + 17] = '_'
                        
                if coor % 8 > 1:
                    if board[coor + 6] == tmp:
                        board[coor + 6] = '_'
                    
                if coor % 8 < 6:
                    if board[coor + 10] == tmp:
                        board[coor + 10] = '_'
            board[coor] = tmp
        elif coup[0] == 'B':
            if fen.split()[1] == 'w':
                tmp = 'B'
            else:
                tmp = 'b'
            
            Piece = [i for i, x in enumerate(board) if x == tmp]
            for p in Piece:
                if (p - coor) % 9 == 0 or (p + coor) % 9 == 0:
                    board[p] = '_'
                    break
            board[coor] = tmp
        else:
            if fen.split()[1] == 'w':
                tmp = 'Q'
            else:
                tmp = 'q'

            Piece = [i for i, x in enumerate(board) if x == tmp]
            for p in Piece:
                if (p - coor) % 9 == 0 or (p + coor) % 9 == 0 or p % 8 == coor % 8 or (p >= (coor - coor % 8) and p <= coor + (8 - coor % 8)):
                    board[p] = '_'
                    break
            board[coor] = tmp
           
    elif coup == 'OO':
        if fen.split()[1] == 'w':
            board[63] = "_"
            board[61] = "R"
            board[60] = "_"
            board[62] = "K"
        else:
            board[7] = "_"
            board[5] = "r"
            board[4] = "_"
            board[6] = "k"
            
    elif coup == 'OOO':
        if fen.split()[1] == 'w':
            board[56]= '_'
            board[59] = 'R'
            board[60] = "_"
            board[58] = "K"
        else:
            board[0]= '_'
            board[3] = 'r'
            board[4] = "_"
            board[2] = "k"
        
    else:
        if 'Q' not in coup:
            arr = coup[-2:]
            coor = posToCoor(arr)
            if len(coup) == 2:
                if fen.split()[1] == 'w':
                    if board[coor + 8] != '_':
                        board[coor + 8] = '_'
                    else:
                        board[coor + 16] != '_'
                    board[coor] = 'P'
                else:
                    if board[coor - 8] != '_':
                        board[coor - 8] = '_'
                    else:
                        board[coor - 16] != '_'
                    board[coor] = 'p'
            else:
                print(coor)
                if fen.split()[1] == 'w':
                    board[coor + 8] = '_'
                    board[coor] = 'Q'
                else:
                    board[coor - 8] = '_'

                    board[coor] = 'q'
                
    newfen = ''
    j = 0
    for i in range(len(board)):
        if i % 8 == 0:
            newfen += '/'
        if board[i] == '_':
            j += 1
        else:
            newfen += board[i]
    if fen.split()[1] == 'w':
        newfen += ' b KQkq -'
    else:
        newfen += ' w KQkq -'
    print(newfen)
    return newfen
        




with open("mini.pgn") as pgn:
    for i in pgn.readlines():
        if i.startswith('1. '):
            fen = baseFEN
            pos = []
            coup = []
            tmp = re.sub('\{.*?\}','',i).split(' ')
            tmp = [k for k in tmp if k != '']
            coup = tmp[1::2]
            print(coup)
            for i in coup:
                fen = newFEN(fen,re.sub(r'[^\w]', '', i))
                pos.append(fen)
    

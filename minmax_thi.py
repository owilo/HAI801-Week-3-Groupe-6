import time
player, opponent = 'x', 'o'
def read_grids_from_file(filename):
    grilles = []
    with open(filename, 'r') as file:
        for line in file:
            grille = [c for c in line] 
            grilles.append(grille)
    return grilles
def is_moves_left(board) : 
    for i in range(9) : 
            if (board[i]== ' ') : 
                return True
    return False
def evaluate(b) : 
    
    for row in range(3) :     
        if (b[3*row + 0] == b[3*row + 1] and b[3*row + 1] == b[3*row + 2]) :         
            if (b[3*row + 0] == player) : 
                return 1
            elif (b[3*row + 0] == opponent) : 
                return -1

    for col in range(3) : 
    
        if (b[0 * 3 + col] == b[1 * 3 + col] and b[1 * 3 + col] == b[2 * 3 + col]) : 
        
            if (b[0 * 3 + col] == player) : 
                return 1
            elif (b[0 * 3 + col] == opponent) : 
                return -1

    if (b[0 * 3 + 0] == b[1 * 3 + 1] and b[1 * 3 + 1] == b[2 * 3 + 2]) : 
    
        if (b[0 * 3 + 0] == player) : 
            return 1
        elif (b[0 * 3 + 0] == opponent) : 
            return -1

    if (b[0 * 3 + 2] == b[1 * 3 + 1] and b[1 * 3 + 1] == b[2 * 3 + 0]) : 
    
        if (b[0 * 3 + 2] == player) : 
            return 1
        elif (b[0 * 3 + 2] == opponent) : 
            return -1

    return 0
def minimax(board, depth, isMax) : 
    score = evaluate(board) 

    if (score == 1) : 
        return score 

    if (score == -1) : 
        return score 

    if (is_moves_left(board) == False) : 
        return 0

    if (isMax) :     
        best = -1000

        for i in range(9) :         
         
            if (board[i]==' ') : 
            
                board[i] = player 

                best = max( best, minimax(board, 
                                        depth + 1, 
                                        not isMax) ) 

                board[i] = ' '
        return best 

    else : 
        best = 1000

        for i in range(9) :         
           
            
            if (board[i]== ' ') : 
            
                board[i]= opponent 

                best = min(best, minimax(board, depth + 1, not isMax)) 

                board[i]= ' '
        return best 
def find_best_move(board) : 
    bestVal = -1000
    bestMove = (-1, -1) 

    for i in range(9) :
        
            if (board[i] == ' ') : 
            
                board[i] = player 

                moveVal = minimax(board, 0, False) 

                board[i] = ' '

                if (moveVal > bestVal) :                 
                    bestMove = (i) 
                    bestVal = moveVal 

    return bestVal 
filename = "data/dataset.txt"
grilles = read_grids_from_file(filename)

start = time.process_time()
for n in range(0, 1000) : 

    for i, grille in enumerate(grilles, 1):
        score = find_best_move(grille)
    
end = time.process_time()
print(end-start)

import math
import random
import copy
import time

def estPartieTerminee(grille, n):
    # Vérifie si la grille est pleine ou s'il y a un gagnant
    if estVictoire(grille, 'X', n) or estVictoire(grille, 'O', n):
        return True
    for ligne in grille:
        if '-' in ligne:
            return False
    return True

def estVictoire(grille, joueur, n):
    # Vérifie les lignes, colonnes et diagonales pour une victoire
    for i in range(n):
        if all(grille[i][j] == joueur for j in range(n)):
            return True
        if all(grille[j][i] == joueur for j in range(n)):
            return True
    if all(grille[i][i] == joueur for i in range(n)) or all(grille[i][n - 1 - i] == joueur for i in range(n)):
        return True
    return False

def scoreEtat(grille, n):
    # Évalue l'état actuel du jeu
    if estVictoire(grille, 'X', n):
        return 10
    elif estVictoire(grille, 'O', n):
        return -10
    else:
        return 0

def minimax(grille, profondeur, estMaximisant, n):
    if estPartieTerminee(grille, n):
        return scoreEtat(grille, n)

    if estMaximisant:
        meilleurScore = -math.inf
        for i in range(n):
            for j in range(n):
                if grille[i][j] == '-':
                    grille[i][j] = 'X'
                    score = minimax(grille, profondeur + 1, False, n)
                    grille[i][j] = '-'
                    meilleurScore = max(meilleurScore, score)
        return meilleurScore
    else:
        meilleurScore = math.inf
        for i in range(n):
            for j in range(n):
                if grille[i][j] == '-':
                    grille[i][j] = 'O'
                    score = minimax(grille, profondeur + 1, True, n)
                    grille[i][j] = '-'
                    meilleurScore = min(meilleurScore, score)
        return meilleurScore

def meilleurCoup(grille, n):
    meilleurScore = -math.inf
    meilleurCoup = None
    for i in range(n):
        for j in range(n):
            if grille[i][j] == '-':
                grille[i][j] = 'X'
                score = minimax(grille, 0, False, n)
                grille[i][j] = '-'
                if score > meilleurScore:
                    meilleurScore = score
                    meilleurCoup = (i, j)
    return meilleurCoup

def choisirCaseVide(grille, n):
    cases_vides = [(i, j) for i in range(n) for j in range(n) if grille[i][j] == '-']
    return cases_vides[0]#random.choice(cases_vides)

def jouerPartie(grille, symbol, n):
    grille = copy.deepcopy(grille)  # Copie de la grille pour ne pas modifier l'originale
    joueur_actuel = symbol
    end = 0
    while not estPartieTerminee(grille, n):
        if joueur_actuel == 'X':
            coup = meilleurCoup(grille, n)
        else:
            coup = choisirCaseVide(grille, n)  # Utilisation de choisirCaseVide pour l'ordinateur
        grille[coup[0]][coup[1]] = joueur_actuel
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
    # afficherGrille(grille)
    result = 0
    if estVictoire(grille, 'X', n):
        result = 1
    elif estVictoire(grille, 'O', n):
        result = -1
    return result

def genererGrilleDepart(n):
    grille = [['-' for _ in range(n)] for _ in range(n)]
    coups_a_jouer = random.randint(0, n * n)  # Nombre aléatoire de coups à jouer
    symboles = ['X', 'O']
    symbole_actuel = random.choice(symboles)  # Choisir aléatoirement le premier symbole

    for _ in range(coups_a_jouer):
        ligne, colonne = choisirCaseVide(grille)
        grille[ligne][colonne] = symbole_actuel
        symbole_actuel = 'X' if symbole_actuel == 'O' else 'O'  # Alterner entre 'X' et 'O'

    return grille

def afficherGrille(grille):
    print("\n---------")
    for ligne in grille:
        print(" | ".join(ligne))
        print("---------")

def parse_grids_from_file(file_path, n):
    grids = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) < 1 + n * n:
                # Ignorer les lignes qui ne sont pas au format attendu
                line += ' ' * (1 + n * n - len(line))
            symbol = line[0]
            values = line[1:]
            values = values.replace(' ', '-')
            grid = [list(values[i:i+n]) for i in range(0, len(values), n)]
            grids.append((symbol, grid))
            print(grid)
    return grids


file_path = "data/datasetN42.txt"
grids = parse_grids_from_file(file_path, 4)
#jouerPartie(grids[-1][1], grids[-1][0])
# Pour afficher les grilles
nblose = 0
nbwin = 0
nbdraw = 0
nbline = 43
total_duration = 0
i = 0
for symbol, grid in grids:
    print(i)
    i += 1

    start = time.time()
    r = jouerPartie(grid, symbol, 4)
    end = time.time()
    total_duration += (end - start)

    if (r == -1):
        nblose += 1
    elif (r):
        nbwin += 1
    else:
        nbdraw += 1

print("Winrate  = " + str((nbwin/nbline)*100) + str(" %"))
print("Loserate = " + str((nblose/nbline)*100)+ str(" %"))
print("Drawrate = " + str((nbdraw/nbline)*100)+ str(" %"))
print("AVG duration = " + str(total_duration/nbline) + str(" s"))
print("Full duration = " + str(total_duration) + str(" s"))


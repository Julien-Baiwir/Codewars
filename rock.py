"""Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"""

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return "Player 1 won!"
        if p2 == 'rock' :
            return "Player 2 won!"
    elif p1 == 'rock':
        if p2 == 'paper':
            return "Player 2 won!"
        if p2 == 'scissors' :
            return "Player 1 won!"
    else:
        if p2 == "scissors":
            return "Player 2 won!"
        if p2 == "rock":
            return "Player 1 won!"
   
        
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"




def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
    
    
    
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

"""Tout d'abord, un dictionnaire hand est créé pour mapper chaque choix possible (rock, paper, scissors) à un nombre entier (0, 1, 2). Cela facilitera la comparaison des choix des joueurs plus tard.

Ensuite, une liste results est définie, où chaque élément correspond à un résultat possible du jeu : 'Draw!' (match nul), 'Player 1 won!' (le joueur 1 a gagné) et 'Player 2 won!' (le joueur 2 a gagné).

La fonction retourne l'élément de la liste results qui correspond au résultat du jeu en utilisant une indexation dynamique.

hand[p1] - hand[p2] calcule la différence entre les choix des joueurs en utilisant les valeurs numériques du dictionnaire hand.

Cette différence sera soit -1, 0 ou 1, représentant respectivement le cas où le joueur 1 perd, il y a un match nul ou le joueur 1 gagne.

En utilisant cette différence comme indice pour accéder à l'élément de la liste results, la fonction renvoie le résultat approprié.""""
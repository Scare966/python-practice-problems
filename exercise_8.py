# rock, paper, scissors game

player1 = input("What is the name of player 1: ")
player2 = input("What is the name of player 2: ")

player1_move = input("P1, rock, paper, or scissors: ")
player2_move = input("P2, rock, paper, or scissors: ")

def game(p1, p2):
    if p1 == p2:
        return("It's a draw.")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins.")
        else:
            return("Paper wins.")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors wins.")
        else:
            return("Rock wins.")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins.")
        else:
            return("Scissors wins.")
    else:
        return("Try again, not a recognizable game choice.")

print(game(player1_move, player2_move))
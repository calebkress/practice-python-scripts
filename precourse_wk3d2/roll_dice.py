# Rolls a given number of die for each of two players and declares a winner.
import random

def roll(dice_num):
    score = 0
    for die in range(0, dice_num):
        score += random.randint(1, 6)
    return score


def roll_dice(player_one=input('How many die to roll for P1? '), player_two=input('How many die to roll for P2? ')):
    p1_score, p2_score = roll(player_one), roll(player_two)
    print((p1_score, p2_score))
    if p1_score > p2_score:
        return 'Player 1 wins!'
    elif p1_score == p2_score:
        return 'It\'s a tie...'
    else:
        return 'Player 2 wins!'

print(roll_dice())

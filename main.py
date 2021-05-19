import random
from random import randint as rand
from colorama import Fore, Back, Style


S_pts = 0
K_pts = 0
U_pts = 0
N_pts = 0
KK_pts = 0
p = 0
t = 0

pts_list = [S_pts, K_pts, U_pts, N_pts, KK_pts]
cur_pts = pts_list[p]
round_list = ('S', 'K', 'U', 'N', 'K')
cur_round = round_list[t]


def roll():
    global t, p, round_list, cur_round, pts_list, cur_pts, S_pts, K_pts, U_pts, N_pts, KK_pts
    dice1 = rand(1, 6)
    dice2 = rand(1, 6)
    dice_total = dice1 + dice2

    if dice1 + dice2 == 2:
        print("You rolled a " + str(dice1) + ' and ' + str(dice2) + ' with a total of ' + str(dice_total) + ' points!')
        print('Snake eyes! You lose all your points.')
        for x in range(0, 5):
            pts_list[x] = 0
        moveToNextRound()

    elif dice1 == 1:
        if cur_round == "S":
            print(Fore.YELLOW + Style.BRIGHT + "You rolled a 1 on the first round! Roll again.")
            roll()
        else:
            print(Fore.GREEN + "You rolled a " + str(dice1) + ' and ' + str(dice2) + ' with a total of ' + str(
                dice_total) + ' points!')
            print(
                Fore.YELLOW + Style.BRIGHT + 'Oh no! At least one of your rolls was a 1, you lost all your points for the [' + str(
                    cur_round) + '] round.')
            cur_pts = 0
            moveToNextRound()

    elif dice2 == 1:
        if cur_round == "S":
            print(Fore.YELLOW + Style.BRIGHT + "You rolled a 1 on the first round! Roll again.")
            roll()
        else:
            print(Fore.GREEN + "You rolled a " + str(dice1) + ' and ' + str(dice2) + ' with a total of ' + str(
                dice_total) + ' points!')
            print(
                Fore.YELLOW + Style.BRIGHT + 'Oh no! At least one of your rolls was a 1, you lost all your points for the [' + str(
                    cur_round) + '] round.')
            cur_pts = 0
            moveToNextRound()

    else:
        print(
            'You rolled a ' + str(dice1) + ' and ' + str(dice2) + ' for a total of ' + str(dice1 + dice2) + ' points.')
        cur_pts = int(cur_pts) + int(dice_total)
        nextMove()


def nextMove():
    global pts_list, p, cur_pts
    print('You have ' + str(cur_pts) + ' points so far in the [' + str(cur_round) + '] round. What is your next move?')
    print('1. Roll again   2. Stop for this round')
    choice = input()
    if choice == '1':
        roll()
    elif choice == '2':
        print('Great Job this round! You scored a total of ' + str(cur_pts) + ' points in the [' + str(
            cur_round) + '] round.')
        pts_list[p] = cur_pts
        moveToNextRound()
    else:
        print(Fore.RED + Style.BRIGHT + 'Error: Wrong input.')
        nextMove()


def moveToNextRound():
    global t, p, round_list, cur_round, pts_list, cur_pts, S_pts, K_pts, U_pts, N_pts, KK_pts
    print('You have a total of ' + str(
        pts_list[0] + pts_list[1] + pts_list[2] + pts_list[3] + pts_list[4]) + ' points across all rounds.')
    t += 1
    if t >= 5:
        print('Congrats! Your final score is ' + str(
            pts_list[0] + pts_list[1] + pts_list[2] + pts_list[3] + pts_list[4]) + '.')
        print('Thanks for playing!')
    else:
        p += 1
    dice1 = rand(1,6) 
    dice2 = rand(1,6)
    dice_total = dice1 + dice2

    if dice1 and dice2 == 1:
        print("You rolled a " + str(dice1) + ' and ' + str(dice2) + ' with a total of ' + str(dice_total) + ' points!')
        print('Snake eyes! You lose all your points.')
        for x in range(0,5): 
            pts_list[x] = 0
        moveToNextRound()
    
    else:
        print('You rolled a ' + str(dice1) + ' and ' + str(dice2) + ' for a total of ' + str(dice1 + dice2) + ' points.')
        cur_pts = int(cur_pts) + int(dice_total)
        nextMove()

roll()
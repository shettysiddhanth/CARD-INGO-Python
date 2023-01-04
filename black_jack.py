'''
This is the file for Black Jack game, it contains all code necessary for the execution of the n-player game
This game is made by MANATUNGE Aishani Induja (3035962386)
'''

import random, time
from random import randrange
from rules import blackjack_rules as rules 
from text_formatting import color, bold, black, red

def start():
    print("\n"+(color('♣') + color('♦') + color('♠') + color('♥')) * 5, color('♣') + color('♦'), sep="")
    print(f"{color('♦')} {bold('--> BLACK JACK <--', 'black')} {color('♣')}")
    print(f"{color('♠') + color('♥') + color('♣') + color('♦')}" * 5, color('♠') + color('♥') + "\n", sep="")
    time.sleep(0.75)

def check_rules():
    while True:
        choice = input(f"Do you want to see the rules? (Y/N): ").lower()
        if choice == "y":
            print()
            rules()
            print()
            time.sleep(0.5)
            break
        elif choice == "n": 
            print()
            break
        else: 
            print(red("Invalid choice, please choose again!"))
            time.sleep(0.25)

def card_list():
    suits = ["♣", "♦", "♠", "♥"]
    nums = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    cardList = []
    for suit in suits:
        for num in nums: cardList.append(f"{num}{suit}")
    return cardList

def players():
    while True:
        try:
            n = int(input("Number of players (2-6): "))
            if 2 <= n <= 6:
                print()
                time.sleep(0.5)
                return n
            else: 
                print(red("Invalid choice, please choose again!"))
                time.sleep(0.25)
        except:
            print(red("Invalid choice, please choose again!"))
            time.sleep(0.25)

def check_winner(scores):
    winners = []
    maximum = 0
    end = True
    for i in range(len(scores)):
        if str(scores[i])[-1] not in ["B", "S"]:
            end = False
            return None
    if end:
        for i in range(len(scores)):
            if scores[i][-1] == "B": continue
            if int(scores[i][:-1]) > maximum:
                maximum = int(scores[i][:-1])
                winners = [i + 1]
            elif int(scores[i][:-1]) == maximum:
                winners.append(i+1)

    return winners

def play(n, cards):
    conv = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
        }
    deck = cards
    scores = [0 for _ in range(n)]
    hand = [[] for _ in range(n)]
    hand2 = [[] for _ in range(n)]
    hand3 = [[] for _ in range(n)]
    for i in range(n):
        for _ in range(2):
            card = random.choice(deck)
            deck.remove(card)
            hand[i].append(card)
            if card[:-1] != "A": scores[i] += conv[card[:-1]]
            else:
                if scores[i] >= 11:
                    scores[i] += 1
                else: scores[i] += 11
            if len(card[:-1]) != 2:
                hand2[i].append(" " + card)
                hand3[i].append(card[:-1] + " " + card[-1])
            else:
                hand2[i].append(card)
                hand3[i].append(card)

    time.sleep(0.5)

    while True:
        for i in range(n):
            print(bold('Player ' + str(i + 1) + "'s Turn"))
            for x in range(len(hand[i])): print("┏━━━━━┓", end = " " if x != (len(hand[i]) - 1) else "\n")
            for x in range(len(hand[i])): print(f"┃  {hand2[i][x][:-1]} ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
            for x in range(len(hand[i])): print(f"┃  {color(hand2[i][x][-1])}  ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
            for x in range(len(hand[i])): print(f"┃ {hand3[i][x][:-1]}  ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
            for x in range(len(hand[i])): print(f"┗━━━━━┛", end = " " if x != (len(hand[i]) - 1) else "\n")

            if str(scores[i])[-1] not in ['B', 'S']:
                print(bold('Total Score: ' + str(scores[i])) + '\n')
                time.sleep(0.25)
                while True:
                    choice = input("Choice ('H' for Hit, 'S' for Stand): ").lower()
                    if choice not in ['s', 'h']:
                        print(red("Invalid choice, please choose again!"))
                        time.sleep(0.25)
                    else: 
                        print()
                        time.sleep(0.5)
                        break
                if choice == 'h':
                    card = random.choice(deck)
                    deck.remove(card)
                    hand[i].append(card)

                    if card[:-1] != "A": scores[i] += conv[card[:-1]]
                    else:
                        if scores[i] >= 11:
                            scores[i] += 1
                        else: scores[i] += 11

                    if len(card[:-1]) != 2:
                        hand2[i].append(" " + card)
                        hand3[i].append(card[:-1] + " " + card[-1])
                    else:
                        hand2[i].append(card)
                        hand3[i].append(card)

                    if scores[i] > 21: scores[i] = str(scores[i]) + "B"

                    for x in range(len(hand[i])): print("┏━━━━━┓", end = " " if x != (len(hand[i]) - 1) else "\n")
                    for x in range(len(hand[i])): print(f"┃  {hand2[i][x][:-1]} ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
                    for x in range(len(hand[i])): print(f"┃  {color(hand2[i][x][-1])}  ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
                    for x in range(len(hand[i])): print(f"┃ {hand3[i][x][:-1]}  ┃", end = " " if x != (len(hand[i]) - 1) else "\n")
                    for x in range(len(hand[i])): print(f"┗━━━━━┛", end = " " if x != (len(hand[i]) - 1) else "\n")
                    if str(scores[i])[-1] == "B": 
                        print(bold('Total Score: ' + str(scores[i][:-1])))
                        print(bold('You have been busted', 'red') + '\n')
                        time.sleep(0.75)
                    else: 
                        print(bold('Total Score: ' + str(scores[i])) + '\n')
                        time.sleep(0.75)

                elif choice == 's':
                    scores[i] = str(scores[i]) + "S"
                    print(bold("You chose to stand", 'red') + '\n')
                    time.sleep(0.75)

            elif str(scores[i])[-1] == "B":
                print(bold('You have been busted', 'red') + '\n')
                time.sleep(0.75)

            elif str(scores[i])[-1] == "S":
                print(bold('Total Score: ' + scores[i][:-1]))
                time.sleep(0.25)
                print(bold("You chose to stand", 'red') + '\n')
                time.sleep(0.75)

        winners = check_winner(scores)
        if winners == None:
            continue
        elif winners == []:
            print((color('♦') + color('♠') + color('♥') + color('♣')) * 13)
            print((color('♣') + color('♦') + color('♠') + color('♥')) * 13)
            print((color('♦') + color('♠') + color('♥') + color('♣')) + bold("  There is no winner, everyone got busted!  ", 'red') + color('♥') + color('♣') + color('♦') + color('♠'))
            print((color('♠') + color('♥') + color('♣') + color('♦')) * 13)
            print((color('♦') + color('♠') + color('♥') + color('♣')) * 13 + "\n")
            time.sleep(1)
            break
        elif len(winners) == 1:
            print((color('♦') + color('♠') + color('♥') + color('♣')) * 9)
            print((color('♣') + color('♦') + color('♠') + color('♥')) * 9)
            print(f"{color('♦')+color('♠') + color('♥') + color('♣')}  {bold('Player ' + str(winners[0]) + ' is the winner !')}  {color('♥') + color('♣') + color('♦') + color('♠')}")
            print((color('♠') + color('♥') + color('♣') + color('♦')) * 9)
            print((color('♦') + color('♠') + color('♥') + color('♣')) * 9 + "\n")
            time.sleep(1)
            break
        else:
            reps = 11 if len(winners) == 2 else 12 if len(winners) == 3 else 13 if len(winners) == 4 or len(winners) == 5 else 14 if len(winners) == 6 else 11
            str1 = (color('♦') if len(winners) in [2, 3, 5, 6] else "") + (color('♠') if len(winners) in [2, 5, 6] else "") + (color('♥') if len(winners) in [5] else "")
            str2 = (color('♣') if len(winners) in [2, 3, 5, 6] else "") + (color('♦') if len(winners) in [2, 5, 6] else "") + (color('♠') if len(winners) in [5] else "")
            str3 = (color('♠') if len(winners) in [2, 3, 5, 6] else "") + (color('♥') if len(winners) in [2, 5, 6] else "") + (color('♣') if len(winners) in [5] else "")
            str4 = (color('♥') + color('♣') + color('♦') + color('♠')) if len(winners) == 4 else (color('♦') + color('♠') + color('♥') + color('♣')) if len(winners) in [2, 6] else (color('♣') + color('♦') + color('♠') + color('♥')) if len(winners) in [3, 5] else ""
            print((color('♦') + color('♠') + color('♥') + color('♣')) * (reps) + str1)
            print((color('♣') + color('♦') + color('♠') + color('♥')) * (reps) + str2)
            print(f"{color('♦')+color('♠') + color('♥') + color('♣')}  {bold('It is a draw amongst Players ' + ', '.join(list(map(str, winners))) + '!')}  {str4}")
            print((color('♠') + color('♥') + color('♣') + color('♦')) * (reps) + str3)
            print((color('♦') + color('♠') + color('♥') + color('♣')) * (reps) + str1 + '\n')
            break

def main():
    start()
    check_rules()
    cards = card_list()
    n = players()
    play(n, cards)

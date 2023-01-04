'''
This is the file for Trump game, it contains all code necessary for the execution of the 4-player game
This game is made by QUETTAWALA Hatim (3036094849)
'''

import random, time
from rules import trump_rules as rules
from main import get_cards as suit_numbers
from text_formatting import color, bold, black, red

def start():
    print("\n"+(color('♣') + color('♦') + color('♠') + color('♥')) * 4, color('♣'), sep="")
    print(f"{color('♦')} {bold('--> TRUMP <--', 'black')} {color('♥')}")
    print(f"{color('♠') + color('♥') + color('♣') + color('♦')}" * 4, color('♠') + "\n", sep="")
    time.sleep(1)

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
    cardList = []
    for suit in suit_numbers()[0]:
        for num in suit_numbers()[1]: cardList.append(f"{num}{suit}")
    return cardList

def trump_call(turn, cards):
    player_cards = [[], [], [], []]
    player_cards2 = [[], [], [], []]
    deck = cards
    for i in range(4):
        for _ in range(5):
            choice = random.choice(deck)
            player_cards2[i].append(choice)
            if len(choice) == 2: player_cards[i].append([" " + choice, choice[0] + " " + choice[1]])
            else: player_cards[i].append([choice, choice])
            deck.remove(choice)
    for i in range(4):
        for _ in range(4):
            choice = random.choice(deck)
            player_cards2[i].append(choice)
            if len(choice) == 2: player_cards[i].append([" " + choice, choice[0] + " " + choice[1]])
            else: player_cards[i].append([choice, choice])
            deck.remove(choice)
    for i in range(4):
        for _ in range(4):
            choice = random.choice(deck)
            player_cards2[i].append(choice)
            if len(choice) == 2: player_cards[i].append([" " + choice, choice[0] + " " + choice[1]])
            else: player_cards[i].append([choice, choice])
            deck.remove(choice)

    print(f"First 5 cards are being distributed, {bold('Player 1', 'black')} chooses the Trump suit.")
    time.sleep(0.75)
    for i in range(5): print(f"{bold('', 'black')}┏━━━━━┓", end=" " if i != 4 else "\n")
    for i in range(5): print(f"{bold('', 'black')}┃  {player_cards[0][i][0][0:2]} ┃", end=" " if i != 4 else "\n")
    for i in range(5): print(f"{bold('', 'black')}┃  {color(player_cards[0][i][0][-1])}  ┃", end=" " if i != 4 else "\n")
    for i in range(5): print(f"{bold('', 'black')}┃ {player_cards[0][i][1][0:2]}  ┃", end=" " if i != 4 else "\n")
    for i in range(5): print(f"{bold('', 'black')}┗━━━━━┛", end=" " if i != 4 else "\n")
    time.sleep(0.75)
    
    while True:
        trump = input(f"Choose Trump (C for Clubs '{color('♣')}', D for Diamonds '{color('♦')}', S for Spades '{color('♠')}', and H for Hearts '{color('♥')}'): ").lower()
        suit_ini = ['c', 'd', 's', 'h']
        if trump in suit_ini:
            suit = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
            suit_symbols = ["♣", "♦", "♠", "♥"]
            print(f"The trump is {bold(suit[suit_ini.index(trump)])} {color(suit_symbols[suit_ini.index(trump)])}")
            time.sleep(0.75)
            return suit_symbols[suit_ini.index(trump)], player_cards, player_cards2
        else: 
            print(red('Invalid Trump Call, please choose agian!'))
            time.sleep(0.25)


def rounds(trump, player_cards, player_cards2):
    suit_symbols = ["♣", "♦", "♠", "♥"]
    suit_ini = ['c', 'd', 's', 'h']
    winners = []
    team1 = 0
    team2 = 0
    while len(winners) != 13 and team1 != 7 and team2 != 7:
        turns = [1, 2, 3, 4] if winners == [] else [2, 3, 4, 1] if winners[-1] == 2 else [3, 4, 1, 2] if winners[-1] == 3 else [4, 1, 2, 3] if winners[-1] == 4 else [1, 2, 3, 4]
        sets = ["?", "?", "?", "?"]
        for turn in turns:
            print("\n" + bold(f"Player {str(turn)}'s Turn") + "\n") if winners == [] else print("\n" + bold(f"Player {str(turn)}'s Turn") + "\n")
            time.sleep(0.5)
            print(f"Trump: {color(trump)}")
            print(f"Round: " + (color(sets[turns[0]-1][-1]) if sets[turns[0]-1][-1] != "?" else "?"))
            print(f"Player {bold('1 & 3', 'black')}: {bold(str(team1), 'black')} sets, Player {bold('2 & 4', 'black')}: {bold(str(team2), 'black')} sets.")
            for i in turns: print(f"Player {bold(str(i), 'black')}: {sets[i-1][:-1] + color(sets[i-1][-1]) if len(sets[i-1]) != 1 else '?'}", end=", " if i != turns[-1] else "\n")
            time.sleep(0.5)
            for i in range(13 - len(winners)): print(f"┏━━━━━┓", end=" " if i != 12-len(winners) else "\n")
            for i in range(13 - len(winners)): print(f"┃  {player_cards[turn - 1][i][0][0:2]} ┃", end=" " if i != 12-len(winners) else "\n")
            for i in range(13 - len(winners)): print(f"┃  {color(player_cards[turn - 1][i][0][-1])}  ┃", end=" " if i != 12-len(winners) else "\n")
            for i in range(13 - len(winners)): print(f"┃ {player_cards[turn - 1][i][1][0:2]}  ┃", end=" " if i != 12-len(winners) else "\n")
            for i in range(13 - len(winners)): print(f"┗━━━━━┛", end=" " if i != 12-len(winners) else "\n")
            for i in range(13 - len(winners)): 
                if len(player_cards2[turn - 1][i]) != 3:
                    print(f"  {player_cards2[turn - 1][i][:-1] + suit_ini[suit_symbols.index(player_cards2[turn - 1][i][-1])]}   ", end=" " if i != 12-len(winners) else "\n")
                else: 
                    print(f"  {player_cards2[turn - 1][i][:-1] + suit_ini[suit_symbols.index(player_cards2[turn - 1][i][-1])]}  ", end=" " if i != 12-len(winners) else "\n")
            time.sleep(0.75)
            card = card_input(turn-1, turns, sets[turns[0]-1][-1], player_cards2)
            index = player_cards2[turn-1].index(card.upper())
            sets[turn-1] = card.upper() 
            player_cards[turn-1].remove(player_cards[turn-1][index])
            player_cards2[turn-1].remove(card.upper())
        winners.append(check_set(trump, sets, turns[0]))
        if winners[-1] == 1 or winners[-1] == 3: team1 += 1
        else: team2 += 1
        print("\n" + bold('Player ' + str(winners[-1]) + ' won the round with ', 'red') + sets[winners[-1]-1][:-1] + color(sets[winners[-1]-1][-1]) + "\n")
        time.sleep(0.5)
    print(f"Player {bold('1 & 3', 'black')}: {bold(str(team1), 'black')} sets, Player {bold('2 & 4', 'black')}: {bold(str(team2), 'black')} sets.")
    time.sleep(0.5)
    winner(1) if team1 >= 7 else winner(2)

def winner(team):
    print("\n" + (color('♦') + color('♠') + color('♥') + color('♣')) * 6)
    print((color('♣') + color('♦') + color('♠') + color('♥')) * 6)
    print(f"{color('♦')+color('♠') + color('♥') + color('♣')}  {bold('Team ' + str(team) + ' wins!', 'red')}  {color('♥') + color('♣') + color('♦') + color('♠')}")
    print((color('♠') + color('♥') + color('♣') + color('♦')) * 6)
    print((color('♦') + color('♠') + color('♥') + color('♣')) * 6 + "\n")
    time.sleep(1)

def check_set(trump, sets, turn):
    trump_moves = []
    round_moves = []
    for i in range(4):
        if sets[i][-1] == trump:
            trump_moves.append([sets[i][:-1], i+1])
        elif sets[i][-1] == sets[turn-1][-1]:
            round_moves.append([sets[i][:-1], i+1])
    if trump_moves != []:
        minimum = 13
        winner = 0
        for i in trump_moves:
            if suit_numbers()[1].index(i[0]) < minimum:
                minimum = suit_numbers()[1].index(i[0])
                winner = i[1]
        return winner
    elif round_moves != []:
        minimum = 13
        winner = 0
        for i in round_moves:
            if suit_numbers()[1].index(i[0]) < minimum:
                minimum = suit_numbers()[1].index(i[0])
                winner = i[1]
        return winner

def card_input(turn, turns, suit, player_cards2):
    suit_symbols = ["♣", "♦", "♠", "♥"]
    suit_ini = ['c', 'd', 's', 'h']
    while True:
        card = input(f"Play a card (Enter the digits and letters as seen above): ").lower()
        time.sleep(0.5)
        if len(card) < 2 or len(card) > 3: 
            print(f"{red('Invalid choice, please choose again!')}")
            time.sleep(0.25)
        elif card[-1] not in suit_ini: 
            print(f"{red('Invalid choice, please choose again!')}")
            time.sleep(0.25)
        elif card[:-1].upper() + suit_symbols[suit_ini.index(card[-1])] not in player_cards2[turn]: 
            print(f"{red('The card is not in your deck, please choose again!')}")
            time.sleep(0.25)
        elif turns.index(turn+1) != 0 and suit_symbols[suit_ini.index(card[-1])] != suit:
            found = False
            for i in player_cards2[turn]:
                if suit == i[-1]: found = True 
            if found: 
                print(red('You have a card with ') + color(suit) + red(', you can not throw a card from another suit!'))
                time.sleep(0.25)
            else: return card[:-1] + suit_symbols[suit_ini.index(card[-1])]
        else:
            return card[:-1] + suit_symbols[suit_ini.index(card[-1])]

def main():
    start()
    check_rules()
    cards = card_list()
    trump, player_cards, player_cards2 = trump_call(1, cards)
    rounds(trump, player_cards, player_cards2)


















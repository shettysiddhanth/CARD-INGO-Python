'''
This is the file for War game, it contains all code necessary for the execution of the 2-player game
This game is made by JAYAWARDANA Wickramasinghe Pathiranage Lakindu Ransika (3036094631)
'''

import random, time, sys
from rules import war_rules as rules 
from text_formatting import color, bold, black, red, yellow, cyan, green

def start():
    print("\n" + (color('♣') + color('♦') + color('♠') + color('♥')) * 4, color('♣'), sep="")
    print(f"{color('♦')} {bold('-->  WAR  <--', 'black')} {color('♥')}")   
    print(f"{color('♠') + color('♥') + color('♣') + color('♦')}" * 4, color('♠'), sep="")
    time.sleep(1)
    print('\nYou are about to play a newly made variation of the card game "War"!')
    time.sleep(0.5)

def check_rules():
    while True:
        choice = input(f"Do you want to see the rules? (Y/N): ").lower()
        if choice == "y":
            print()
            rules()
            print()
            break
        elif choice == "n": 
            print()
            break
        else: print(red("Invalid choice, please choose again!"))

def get_cards():
    suit = ["♣", "♦", "♠", "♥"]
    num = ["1", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    return suit, num

def card_list(cards):
    cardList = []
    for suit in cards[0]:
        for num in cards[1]: cardList.append(f"{num}{suit}")
    return cardList

def deck_maker(fixed_deck):
    card_deck = sorted(fixed_deck, key = lambda k: random.random())
    decks = [card_deck[:26], card_deck[26:]]
    return decks

def hands(decks,index,hand):
    hand[index] = decks[index][:5]
    decks[index] = decks[index][5:]   
    return hand, decks

def print_cards(list_cards):
    for i in range(len(list_cards)): print(f"┏━━━━━┓", end="   " if i != len(list_cards)-1 else "\n")
    for i in range(len(list_cards)):     
        if list_cards[i][:-1] == '10' or list_cards[i][:-1] == '11' or list_cards[i][:-1] == '12' or list_cards[i][:-1] == '13':
            print(f"┃  {list_cards[i][-3]}{list_cards[i][-2]} ┃", end="   " if i != len(list_cards)-1 else "\n")  
            continue  
        print(f"┃   {list_cards[i][-2]} ┃", end="   " if i != len(list_cards)-1 else "\n")
    for i in range(len(list_cards)): print(f"┃  {color(list_cards[i][-1])}  ┃", end="   " if i != len(list_cards)-1 else "\n")
    for i in range(len(list_cards)): 
        if list_cards[i][:-1] == '10' or list_cards[i][:-1] == '11' or list_cards[i][:-1] == '12' or list_cards[i][:-1] == '13':
            print(f"┃ {list_cards[i][0]}{list_cards[i][1]}  ┃", end="   " if i != len(list_cards)-1 else "\n")   
            continue 
        print(f"┃ {list_cards[i][-2]}   ┃", end="   " if i != len(list_cards)-1 else "\n")
    for i in range(len(list_cards)): print(f"┗━━━━━┛", end="   " if i != len(list_cards)-1 else "\n")
    for i in range(len(list_cards)): 
        if list_cards[i][-1] == "♣":
            symbol = 'c'
        elif list_cards[i][-1] == "♦":
            symbol = 'd' 
        elif list_cards[i][-1] == "♠":
            symbol = 's' 
        elif list_cards[i][-1] == "♥":
            symbol = 'h'            
        if list_cards[i][:-1] == '10' or list_cards[i][:-1] == '11' or list_cards[i][:-1] == '12' or list_cards[i][:-1] == '13':
            print(f"  {list_cards[i][-3]}{list_cards[i][-2]}{symbol} ", end="    " if i != len(list_cards)-1 else "\n")  
            continue     
        print(f'   {list_cards[i][-2]}{symbol} ',end="    " if i != len(list_cards)-1 else "\n")

def symbol_swap(swap_list):
    for i in range(len(swap_list)):
        if swap_list[i][-1] == "♣":
            symbol = 'c'
        elif swap_list[i][-1] == "♦":
            symbol = 'd' 
        elif swap_list[i][-1] == "♠":
            symbol = 's' 
        elif swap_list[i][-1] == "♥":
            symbol = 'h'    
        swap_list[i] = (swap_list[i][:-1] + symbol).lower()
    return swap_list

def letter_swap(swap_list):
    for i in range(len(swap_list)):
        symbol = ''
        if swap_list[i][-1] == "c":
            symbol = "♣"
        elif swap_list[i][-1] == "d":
            symbol = "♦" 
        elif swap_list[i][-1] == "s":
            symbol = "♠" 
        elif swap_list[i][-1] == "h":
            symbol = "♥"   
        swap_list[i] = swap_list[i][:-1] + symbol
    return swap_list    

def player_turn(player,index,hand,selected_card,all_card_combs):
    print(bold(f"Player {player[index]}'s Turn"))
    time.sleep(1)
    print_cards(hand[index])
    hand_swapped = symbol_swap(hand[index])
    x = input('Enter card: ')
    x = x.lower()
    while x not in hand_swapped:
        print('Invalid input! Please re-enter')
        x = input('Enter card: ')
        x = x.lower()
    selected_card[index].append(x)
    hand_swapped = letter_swap(hand[index])
    hand[index].remove(letter_swap(selected_card[index])[0])

def reshuffle(decks,discard_pile):
    decks[0].extend(discard_pile[0])
    decks[1].extend(discard_pile[1])
    discard_pile[0] = []
    discard_pile[1] = []
    decks[0] = sorted(decks[0], key = lambda k: random.random())
    decks[1] = sorted(decks[1], key = lambda k: random.random())


def war(selected_card,discard_pile,hand,decks,war_draw_flag):
    reshuffle(decks,discard_pile)
    if (len(discard_pile[0]) + len(decks[0])) < 5:
            war_flag = True
            return
    if (len(discard_pile[1]) + len(decks[1])) < 5:
            war_flag = True
            return
    time.sleep(1)
    print(f'{color("♣")}{color("♦")}{color("♠")}{color("♥")}'*2 + bold('WAR') + f'{color("♥")}{color("♠")}{color("♦")}{color("♣")}'*2)
    time.sleep(3)
    print(f"{cyan('During war, each player will draw the first 5 cards from their deck.')}")
    print(f"{cyan('The player with a higher sum for the cards drawn will win the war!')}")
    temp_hand = [decks[0][:5],decks[1][:5]]
    decks[0] = decks[0][5:]
    decks[1] = decks[1][5:]
    print(f'''{cyan("First 5 cards from player 1's deck: ")}''')
    print_cards(temp_hand[0])
    time.sleep(1)
    print(f'''{cyan("First 5 cards from player 2's deck: ")}''')
    print_cards(temp_hand[1])
    time.sleep(1)
    if sum([int(i[:-1]) for i in temp_hand[0]]) > sum([int(i[:-1]) for i in temp_hand[1]]):
        discard_pile[0].extend(selected_card[0])
        discard_pile[0].extend(selected_card[1])
        discard_pile[0].extend(temp_hand[0])
        discard_pile[0].extend(temp_hand[1])
        print(f"{cyan('Player 1 wins war')}")
    elif sum([int(i[:-1]) for i in temp_hand[0]]) < sum([int(i[:-1]) for i in temp_hand[1]]):
        discard_pile[1].extend(selected_card[0])
        discard_pile[1].extend(selected_card[1])
        discard_pile[1].extend(temp_hand[0])
        discard_pile[1].extend(temp_hand[1])
        print(f"{cyan('Player 2 wins war')}")
    elif sum([int(i[:-1]) for i in selected_card[0]]) == sum([int(i[:-1]) for i in selected_card[1]]): 
        war_draw_flag = True
        return
    time.sleep(1)

def process_turn(selected_card,discard_pile,hand,decks,game_round,war_draw_flag):
    print(green('Cards played: '))
    time.sleep(1)
    print(" ")
    print(green('Player 1  Player 2'))
    print_cards([selected_card[0][0],selected_card[1][0]])
    if sum([int(i[:-1]) for i in selected_card[0]]) > sum([int(i[:-1]) for i in selected_card[1]]):
        discard_pile[0].extend(selected_card[0])
        discard_pile[0].extend(selected_card[1])
        print(green(f"Player 1 wins round {game_round}"))
    elif sum([int(i[:-1]) for i in selected_card[0]]) < sum([int(i[:-1]) for i in selected_card[1]]):
        discard_pile[1].extend(selected_card[0])
        discard_pile[1].extend(selected_card[1])
        print(green(f"Player 2 wins round {game_round}"))
    elif sum([int(i[:-1]) for i in selected_card[0]]) == sum([int(i[:-1]) for i in selected_card[1]]): 
        war(selected_card,discard_pile,hand,decks,war_draw_flag)
        if war_flag == True or war_draw_flag == True:
            return    
    time.sleep(1)
    print('\n')
    print(green("Total number of cards in Player 1's discard pile and deck: "),len(discard_pile[0]) + len(decks[0])) 
    time.sleep(1)
    print(green("Total number of cards in Player 2's discard pile and deck: "),len(discard_pile[1]) + len(decks[1])) 
    print('\n')

def main(cards):
    global war_flag, war_draw_flag
    war_flag = False
    war_draw_flag= False
    cards = get_cards()
    start()
    check_rules()
    fixed_deck = card_list(cards)
    decks = deck_maker(fixed_deck)
    turn = 0
    all_card_combs = card_list(cards=(["c", "d", "s", "h"],["1", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2"])) 
    hand = [[],[]]
    discard_pile =[[],[]]
    player = ['1','2']
    while True:
        game_round = turn//2 + 1
        if turn%2 == 0:
            print(f"{bold('Round')} {bold(game_round)}")
            time.sleep(1)
            selected_card = [[],[]]
        index = turn%2
        if len(hand[index]) == 0:
            hand, decks = hands(decks,index,hand)
            print(f"Player {player[index]} draws 5 cards")
            print(f"Total number of cards in Player {player[index]}'s discard pile and deck: ", len(discard_pile[index]) + len(decks[index])) 
            time.sleep(1)
        player_turn(player,index,hand,selected_card,all_card_combs)
        if (turn%2 == 1):
            process_turn(selected_card,discard_pile,hand,decks,game_round,war_draw_flag)
        if war_draw_flag == True:
            print(f"{cyan('Both players had same the same total during War.')}")
            print(f"{cyan('DRAW!!!!')}")
            return
        if (len(discard_pile[0]) + len(decks[0])) < 5:
            print(f"{yellow('Player 1 has less than 5 cards in total.')}")
            break
        if (len(discard_pile[1]) + len(decks[1])) < 5:
            print(f"{yellow('Player 2 has less than 5 cards in total.')}")
            break
        turn += 1
        if turn == 30:
            break
        reshuffle(decks,discard_pile)
    if (len(discard_pile[0]) + len(decks[0])) > (len(discard_pile[1]) + len(decks[1])):
        print('\n')
        print(yellow("Total number of cards in Player 1's discard pile and deck: "),len(discard_pile[0]) + len(decks[0])) 
        print(yellow("Total number of cards in Player 2's discard pile and deck: "),len(discard_pile[1]) + len(decks[1])) 
        print('\n')
        time.sleep(1)
        print(f'{yellow("Player 1 wins!!!!")}')
    elif (len(discard_pile[0]) + len(decks[0])) < (len(discard_pile[1]) + len(decks[1])):
        print('\n')
        print(yellow("Total number of cards in Player 1's discard pile and deck: "),len(discard_pile[0]) + len(decks[0])) 
        print(yellow("Total number of cards in Player 2's discard pile and deck: "),len(discard_pile[1]) + len(decks[1])) 
        print('\n')
        time.sleep(1)
        print(f'{yellow("Player 2 wins!!!!")}')
    else:
        print('\n')
        print(yellow("Total number of cards in Player 1's discard pile and deck: "),len(discard_pile[0]) + len(decks[0])) 
        print(yellow("Total number of cards in Player 2's discard pile and deck: "),len(discard_pile[1]) + len(decks[1])) 
        print('\n')
        time.sleep(1)
        print(f"{yellow('DRAW!!!!')}")



'''
This file is a container for all the rules for the games for neat and tidy code.
'''

from text_formatting import color, bold, black, red, yellow, cyan, green

def trump_rules():
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    print(f"{color('♦')} {bold('Rules', 'black')} {color('♥')}")
    print(f"{color('♠')} The cards are ranked A-K-Q-J-10-9-8-7-6-5-4-3-2, A being the highest and 2 being the lowest.")
    print(f"{color('♥')} There are four players, each player is given 5 cards initially. Player 1 chooses the trump(Leader) suit which they think is best.")
    print(f"{color('♣')} Then 4 cards are given to each player, then again 4 cards. Each player now has 13 cards.")
    print(f"{color('♦')} Player 1 and Player 3 are a team, and Player 2 and Player 4 are a team.")
    print(f"{color('♠')} In each round each player throws 1 card, from the same suit as started by Player 1 or the winner of the last round.")
    print(f"{color('♥')} The team having the largest numbered card wins the round.")
    print(f"{color('♣')} If a player does not have a card from the same suit, they can waste a card from another suit or overthrow all the other cards by throwing a card from the Trump suit.")
    print(f"{color('♦')} If more players throw Trump cards, the one with the largest number wins.")
    print(f"{color('♠')} The team that wins 7 sets or rounds wins the game.")
    print(f"{color('♥')} Have fun!!!")
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    input("Continue? (Enter): ")

def war_rules():
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    print(f"{color('♦')} {bold('Rules', 'black')} {color('♥')}")
    print(f"{color('♠')} The cards are ranked 13-12-11-10-9-8-7-6-5-4-3-2-1, 13 being the highest and 1 being the lowest.")
    print(f"{color('♥')} The cards are arranged in two decks, one deck for each player. Each deck has 26 cards.")
    print(f"{color('♣')} Each player also has their own discard pile, which will be constantly shuffled into their deck.")
    print(f"{color('♦')} There are two players, each player is given 5 cards initially.")
    print(f"{color('♠')} In each round each player chooses one card to play.")
    print(f"{color('♥')} The player having the largest numbered card wins the round.")
    print(f"{color('♣')} The both numbers are the same, the game will enter a state of 'War'.")
    print(f"{color('♦')} During War, the first 5 cards from each players deck will be played.")
    print(f"{color('♠')} The player having the higher total number will win the war.")
    print(f"{color('♥')} If both players have the same total, the game will end with a draw.")
    print(f"{color('♣')} If a player has less than 5 cards in total, in their hand, deck and discard pile, at any given point in time, they loose!!!")
    print(f"{color('♦')} The game ends after 15 rounds. The player with the higher total number of cards, in their hand, deck and discard pile, will win ")
    print(f"{color('♠')} Have fun!!!")
    print(f"{color('♥')+ color('♣') + color('♦') + color('♠')}" * 2, color('♥'), sep="")
    input("Continue? (Enter): ")

def blackjack_rules():
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    print(f"{color('♦')} {bold('Rules', 'black')} {color('♥')}")
    print(f"{color('♠')} (2-6) players can play Black Jack")
    print(f"{color('♥')} Each player is initially given 2 cards")
    print(f"{color('♣')} Every card carries a score, cards 2 to 10 carry the score they indicate, cards J, Q, K each score 10 points, A can either score 11 or 1")
    print(f"{color('♦')} Players can either choose to Hit (Draw a card), or Stand (Hold the score)")
    print(f"{color('♠')} If the total score of the player exceeds 21, they get Busted, and automatically lose the game")
    print(f"{color('♥')} When everyone has either stood or have been busted, the player with the highest score wins")
    print(f"{color('♣')} Have fun!!!")
    print(f"{color('♦') + color('♠') + color('♥') + color('♣')}" * 2, color('♦'), sep="")
    input("Continue? (Enter): ")

def higherorlower_rules():
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    print(f"{color('♦')} {bold('Rules', 'black')} {color('♥')}")
    print(f"{color('♠')} The cards are ranked A-K-Q-J-10-9-8-7-6-5-4-3-2, A being the highest and 2 being the lowest.")
    print(f"{color('♥')} This game is a 1 player game and the player will be given 1 card initially with 7 lifelines.")
    print(f"{color('♣')} The player has to guess if the card in hand is either LOWER, HIGHER or SIMILAR to the next card.")
    print(f"{color('♦')} If guessed correctly, the next card will now become the card in hand and the game will continue in a similar fasion until the card deck is exhausted.")
    print(f"{color('♠')} If guessed incorrectly, a lifeline will be deducted and the deck will be reshuffled.")
    print(f"{color('♥')} Have fun!!!")
    print(f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 2, color('♣'), sep="")
    input("Continue? (Enter): ")







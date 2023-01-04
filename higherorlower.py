'''
This is the file for Higher or Lower game, it contains all code necessary for the execution of the 1-player game
This game is made by SIDDHANTH Shetty (3036085965)
'''
import random, time
from rules import higherorlower_rules as rules
from text_formatting import color, bold, black, red

def start():
    print("\n"+(color('♣') + color('♦') + color('♠') + color('♥')) * 6, color('♣') + color('♦') + color('♠'), sep="")
    print(f"{color('♦')} {bold('--> HIGHER OR LOWER <--', 'black')} {color('♥')}")
    print(f"{color('♠') + color('♥') + color('♣') + color('♦')}" * 6, color('♠') + color('♥') + color('♣') + "\n", sep="")
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

def print_card(cardinplay):
    if cardinplay[0]=="J" or cardinplay[0]=="K" or cardinplay[0]=="Q" or cardinplay[0]=="A":
        print(" ┏━━━━━┓")
        print(f" ┃   {cardinplay[0]} ┃")
        print(f" ┃  {color(cardinplay[-1])}  ┃")
        print(f" ┃ {cardinplay[0]}   ┃")
        print(" ┗━━━━━┛")
    if cardinplay[0].isnumeric():
        if cardinplay[1]!="0":
            print(" ┏━━━━━┓")
            print(f" ┃   {cardinplay[0]} ┃")
            print(f" ┃  {color(cardinplay[-1])}  ┃")
            print(f" ┃ {cardinplay[0]}   ┃")
            print(" ┗━━━━━┛")
    if cardinplay[0].isnumeric():
        if cardinplay[1] == "0":
            print(" ┏━━━━━┓")
            print(f" ┃  10 ┃")
            print(f" ┃  {color(cardinplay[-1])}  ┃")
            print(f" ┃ 10  ┃")
            print(" ┗━━━━━┛")

def value(cardinplay):
    facecardvalues={"A": 14, 'J': 11, "Q": 12, "K": 13}
    cardinplay=str(cardinplay)
    if cardinplay[0].isnumeric():
        if cardinplay[1] != "0":
            return int(cardinplay[0])
        else:
            return 10
    else:
        return facecardvalues[cardinplay[0]]

def wincheck(complete_deck):
    if len(complete_deck)==0:
        print(bold("\n Congratulations!! You have finished this game."))
        time.sleep(1)

def askinput():
    prediction=input(f"Input s for same.\nInput l for lower.\nInput h for higher.\n{bold('Choice:')} ")
    prediction=prediction.lower()
    if prediction not in ["s", "l", "h"]:
        print(red("Invalid choice, please choose again!"))
        time.sleep(0.25)
        askinput()
    time.sleep(0.5)
    return prediction

def pickup(complete_deck):
    random.shuffle(complete_deck)
    complete_deck=complete_deck.pop()
    return complete_deck

def main():
    start()
    check_rules()
    complete_deck=[]
    faces=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits=['♣','♠','♥','♦']
    for x in faces:
        for y in suits:
            complete_deck.append(f'{x}{y}')
    print(bold("BEGIN!"))
    time.sleep(0.3)
    cardinplay=pickup(complete_deck)
    guesses_remaining=6
    final_score=0
    playgame=0
    while playgame<1:
        cardinplayvaluation=value(cardinplay)
        if wincheck(complete_deck):
            break
        cardontopofdeck=pickup(complete_deck)
        print(f'\n{bold("Card in play:")} {cardinplay}')
        print_card(cardinplay)
        globalprediction=askinput()
        cardontopofdeckvaluation=value(cardontopofdeck)

        valuationdifference=cardontopofdeckvaluation-cardinplayvaluation
        if globalprediction=="l" and valuationdifference<0:
            cardinplay=cardontopofdeck
            print(bold('Right Guess!'))
            time.sleep(0.75)
            final_score+=1
            continue
        if globalprediction=="h" and valuationdifference>0:
            cardinplay=cardontopofdeck
            print(bold('Right Guess!'))
            time.sleep(0.75)
            final_score+=1
            continue
        if globalprediction=="s" and valuationdifference==0:
            cardinplay=cardontopofdeck
            print(bold('Right Guess!'))
            time.sleep(0.75)
            final_score+=1
            continue
        else:
            if guesses_remaining==0:
                print(f"{bold('Your guess was wrong as the upcoming card was', 'red')} {cardontopofdeck}.")
                time.sleep(0.25)
                print(f"{bold('Lifelines remaining:')} {guesses_remaining}")
                time.sleep(0.25)
                print(bold("Game Over!", 'red'))
                time.sleep(0.25)
                print(f" {bold('Your final score is')} {final_score}")
                time.sleep(0.75)
                break
            elif guesses_remaining>0:
                print(f"{bold('Your guess was wrong as the upcoming card was', 'red')} {cardontopofdeck}.")
                time.sleep(0.25)
                print(f"{bold('Lifelines remaining:')} {guesses_remaining}")
                time.sleep(0.75)
                guesses_remaining -= 1
                continue

'''
This file is a main platform from where all the game files are accessed and can be played
'''

import trump, war, black_jack, higherorlower
from text_formatting import color, bold, black, red

def get_cards():
    suit = ["♣", "♦", "♠", "♥"]
    num = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    return suit, num

def start_game():
    print("\n" + (f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 7))
    print(f"{color('♦')} {bold('WELCOME', 'black')} {bold('TO', 'red')} {bold('THE', 'black')} {bold('CARD-INGO', 'red')} {color('♣')}")
    print(f"{color('♠') + color('♥') + color('♣') + color('♦')}" * 7 + "\n")

def choices():
    print(f"{bold('', 'black')}Enter {bold(0)} to exit the game")
    print(f"Enter {bold(1)} for Trump (4-player game)")
    print(f"Enter {bold(2)} for Black Jack (n-player game)")
    print(f"Enter {bold(3)} for War (2-player game)")
    print(f"Enter {bold(4)} for Higher or Lower (1-player game)")

def last():
    print("\n" + f"{color('♣') + color('♦') + color('♠') + color('♥')}" * 9)
    print(bold('THANKYOU', 'black') + bold(' FOR', 'red') + bold(' PLAYING', 'black') + bold(' CARD-INGO', 'red') + bold(' !!!', 'red'))
    print(f"This project is developed by: ")
    print(f"{color('♥')} {bold('QUETTAWALA Hatim (3036094849)', 'black')}")
    print(f"{color('♠')} {bold('', 'black')}MANATUNGE Aishani Induja (3035962386)")
    print(f"{color('♦')} {bold('', 'black')}JAYAWARDANA Wickramasinghe Pathiranage Lakindu Ransika (3036094631)")
    print(f"{color('♣')} {bold('', 'black')}SHETTY Siddhanth (3036085965)")
    print(f"{color('♥') + color('♠') + color('♦') + color('♣')}" * 9 + "\n")

if __name__ == "__main__":

    start_game()
    again = "y"
    cards = get_cards()
    while again == "y":
        choices()
        while True:
            choice = input("Game: ")
            if choice in ["0", "1", "2", "3", "4"]: break
            else: print(red("Invalid Game, please choose again!"))
        if choice == "1": trump.main()
        elif choice == "2": black_jack.main()
        elif choice == "3": war.main(cards)
        elif choice == "4": higherorlower.main()
        elif choice == "0":
            last()
            break
        print("Do you want to play another card game? (Y/N): ", end="")
        again = input().lower()
        print()
        if again != "y": last()


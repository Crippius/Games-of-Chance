import sys
import time
from casino import Casino
from problems_check import problems_check

def start():

    def check_retry(): # Checks if the player wants to retry, returns 1 if positive, 0 in the other case

        response = ""
        key_words = ["yes", "y", "yeh", "1", "retry", "no", "n", "nope", "0", "stop"]
        while(response not in key_words):

            response = input("Do you want to retry? ")
            if response not in key_words:
                print("Please enter a valid response (", end='')
                for i in key_words:
                    print(i, end=', ')
                print(")")

        if response in key_words[:5]:
            return 1
        else:
            return 0
        
    def int_input(str):
        try:
            return int(input(str))
        except ValueError:
            print("Please add an integer")
            return int_input(str)

    menu = ["1 - Play Heads or Tails (type '1' or 'coin toss')",
            "2 - Play Slots Machines (type '2' or 'slots)",
            "3 - Play Blackjack (type '3' or 'blackjack')",
            "4 - Play Roulette (type '4' or 'roulette')",
            "5 - Play Baccarat (type '5' or 'baccarat')",
            "6 - View your balance (type '6' or 'balance')",
            "7 - See credits (type '7' or 'credits')",
            "0 - Exit the game (type '0' or 'exit')"]

    print("""
    Thanks for installing Games of Chance!
    In this program you can play some of the most famous gambling games ever!
    Hope you will enjoy this project!
    You will be starting with 100 chips to bet on, good luck!
    """)

    input("Press any key to start the program ")
    player = Casino()
    
    while True:

        retry = 1
        for i in menu:
            print(i)
        decision = input("What do you want to do? --> ")

        if decision == "0" or decision.lower() == "exit":
            player.exit_the_casino(False)
            time.sleep(5)
            sys.exit(1)

        elif decision == "7" or decision.lower() == "credits":
            print("""
            This program was developed in the second half of 2021 by Tommaso Crippa
            Github profile: https://github.com/Crippius
            Linkedin profile: https://www.linkedin.com/in/tommaso-crippa-a127ab222/
            Email: crippa.tommaso@gmail.com
            """)
            time.sleep(5)
            print("As a gift for viewing the credits you will be awarded 200 chips ;)")
            player.add_money(money=200)
            time.sleep(3.5)

        elif decision == "6" or decision.lower() == "balance":
            player.balance(False)
            time.sleep(3)
        
        elif decision == "1" or decision.lower() == "coin toss":
            while(retry):

                bet = [0, False]

                bet[0] = int_input("How much money do you want to bet? ")
                bet[1] = input("What is your prediction? (Heads/Tails) ").title()

                player.heads_or_tails(bet[0], bet[1], False, False)
                time.sleep(1)
                retry = check_retry()

        elif decision == "2" or decision.lower() == "slots":
            while(retry):
                player.slot_machine(int_input("How much money do you want to bet? "), False)
                time.sleep(1)
                retry = check_retry()
                

        
        elif decision == "3" or decision.lower() == "blackjack":
            while(retry):
                player.blackjack(int_input("How much money do you want to bet? "), False, False)
                time.sleep(1)
                retry = check_retry()


        elif decision == "4" or decision.lower() == "roulette":
            while(retry):
                bet = [0, False, False, False, False]

                bet[0] = int_input("How much money do you want to bet? ")
                questions = ["Odd or Even? ", "Manque or Passe? ", "Red, Black or Green? ", "Which number(s)? "]
                res = int_input("Do you want to bet on: (1) Odd or Even, (2) Manque or Passe, (3) Colour, (4) Numbers? ")
                if res != 4:
                    bet[res] = input(questions[res-1]).title()
                else:
                    bet[res] = []
                    for i in input(questions[res-1]).split():
                        try:
                            bet[res].append(int(i))
                        except ValueError:
                            print("You added an invalid character, it won't be included in the bet")
                
                player.roulette(bet[0], bet[1], bet[2], bet[3], bet[4], False)
                time.sleep(1)
                retry = check_retry()
            

        elif decision == "5" or decision.lower() == "baccarat":
            while(retry):
                bet = [0, False, False, False]

                bet[0] = int_input("How much money do you want to bet? ")
                bet[1] =  input("Do you want to be a player or a better? (Player/Better) ").title()

                if bet[1] == "Better":
                    if input("Do you want to bet on who wins?").title() in ["Yes", "Y", "1"]:
                        bet[2] = input("Who do you think is going to win? (Player/Banker/Tie) ").title()

                    elif input("Do you want to bet on a possible pair?").title() in ["Yes", "Y", "1"]:
                        bet[3] = input("Who do you think is going to get the pair? (Player/Banker/Any) ").title()

                player.baccarat(bet[0], bet[1], bet[2], bet[3], False)
                time.sleep(1)
                retry = check_retry()

if __name__ == "__main__":
    start()

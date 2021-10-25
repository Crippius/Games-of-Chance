import sys
import time
from casino import Casino
from problems_check import problems_check

def start():

    def check_retry():
        response = ""
        key_words = ["yes", "y", "yeh", "retry", "1", "no", "n", "nope", "stop", "0"]
        while(response not in key_words):

            response = input("Do you want to retry? ")
            if response not in key_words:
                print("Please enter a valid response (", end='')
                for i in key_words:
                    print(i, end='')
                print(")")

        if response in key_words[:5]:
            return 1
        else:
            return 0

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
            player.exit_the_casino()
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
            player.balance()
            time.sleep(3)
        
        elif decision == "1" or decision.lower() == "coin toss":
            pass

        elif decision == "2" or decision.lower() == "slots":
            while(retry):
                player.slot_machine(20)
                time.sleep(1)
                retry = check_retry()
                

        
        elif decision == "3" or decision.lower() == "coin toss":
            pass

        elif decision == "4" or decision.lower() == "coin toss":
            pass

        elif decision == "5" or decision.lower() == "coin toss":
            pass

if __name__ == "__main__":
    start()

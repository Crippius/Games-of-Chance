import random
from problems_check import problems_check 

money = 100

def baccarat(betted_money, player_or_better="Player", x_win=False, pair=False):
    
    global money

    # Checking if a correct bet has been made
    check = problems_check(betted_money,
                           checking_dict={player_or_better:["Player", "Better"],
                                          x_win:["Player", "Banker", "Tie", False],
                                          pair:["Player", "Banker", "Any", False]},
                                          complimentary={0:[[player_or_better, x_win], ["player_or_better", "x_win"], ["Player", not False]],
                                                         1:[[player_or_better, pair], ["player_or_better", "pair"], ["Player", not False]],
                                                         2:[[player_or_better, x_win, pair], ["player_or_better", "x_win", "pair"], ["Better", False, False]]})
    if check["check"] == False:
        print("You've made an incorrect bet, no money will be taken, the problem is:")
        print(check["reason"])
        return
    
    print("-> Playing Baccarat...")
    money -= betted_money

    # In this game figures value equal to 10
    def figure_to_num(num):
        if type(num) != int:
            return 0
        else:
            return num%10
    
    round_deck = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    # Picking the player's and banker's card
    player_card1 = round_deck.pop(random.randint(0, 51))
    player_card2 = round_deck.pop(random.randint(0, 50))
    bank_card1 = round_deck.pop(random.randint(0, 49))
    bank_card2 = round_deck.pop(random.randint(0, 48))

    # Calculating the total of the picked card
    player_total = (figure_to_num(player_card1) + figure_to_num(player_card2)) % 10
    bank_total = (figure_to_num(bank_card1) + figure_to_num(bank_card2)) % 10

    print("Player's cards: " + str(player_card1) + " " + str(player_card2) + " (Total = " + str(player_total) + ")")
    print("Banker's cards: " + str(bank_card1) + " " + str(bank_card2) + " (Total = " + str(bank_total) + ")")

    cards_left = 48
    
    player_stand = False # These booleans are used to tell the program if the player or banker have stood or drawn
    bank_stand = False


    # Player's turn

    player_card3 = -1 # The value of the third card is initially -1 so if no card is drawn there will be no pair that can be associated with it

    if player_total >= 8 or bank_total >= 8: # Natural, no one draws 
        player_stand = True
        bank_stand = True
        print("Natural! The player and banker stand")
    
    elif player_total <= 5: # The player draws
        cards_left -= 1
        player_card3 = round_deck.pop(random.randint(0, cards_left))
        player_total += figure_to_num(player_card3)
        player_total %= 10
        print("Player draws: " + str(player_card3) + " (Total = " + str(player_total)+ ")")
    
    else: # The player stands, doesnt't have the chance to draw if he wants to
        player_stand = True
        print("Player stands")
    
    # Banker's turn

    banker_draw_dict = {0:range(0, 9), 1:range(0, 9), 2:range(0, 9), 3:[0, 1, 2, 3, 4, 5, 6, 7, 9], 4:range(2, 7), 
                        5:range(4, 7), 6:range(6, 7), 7:[-1], 8:[-1], 9:[-1]} # The banker action depends on what the player picks

    def banker_draws(bank_total, cards_left): # Function to pick a card and add it to the total
        cards_left -= 1
        bank_card3 = round_deck.pop(random.randint(0, cards_left))
        bank_total += figure_to_num(bank_card3)
        bank_total %= 10
        print("Banker draws: " + str(bank_card3) + " (Total = " + str(bank_total) + ")")
        return bank_total
    bank_card3 = -1

    if bank_stand == True: # This condition has been programmed in the case that a natural happens 
        pass               # the program doesn't execute the else condition
        
    
    elif player_stand == True: # When the player stands
        if bank_total <= 5:
            bank_total = banker_draws(bank_total, cards_left) # Banker draws
        else:
            bank_stand = True # Banker stands
            print("Banker stands")

    else: # When the player draws
        if figure_to_num(player_card3) in banker_draw_dict[bank_total]: # Banker draws
            bank_total = banker_draws(bank_total, cards_left)
        else:
            bank_stand = True # Banker stands
            print("Banker stands")


    # Results

    # In case of pairs
    
    any_case = (pair == "Any") # Variable that is used for the "Any" case, if both the player and banker have a pair, the payout is the same
    

    if player_card1 == player_card2 or player_card2 == player_card3 or player_card3 == player_card1: # Player pair
        # A player pair occurs
        if pair == "Player": # If the better betted on a player pair
            money += 8*betted_money
            print("++ Player pair! ++")
        elif pair == "Any": # If the better betted on any pair
            any_case = False
            money += 6*betted_money
            print("+ Player pair! +")
        else: # If no bet was made
            print("(Player pair)")

    elif bank_card1 == bank_card2 or bank_card2 == bank_card3 or bank_card3 == bank_card1:
        if pair == "Banker": # If the better betted on a banker pair
            print("++ Banker pair! ++ ")
            money += 12*betted_money
        elif pair == "Any" and any_case == True: # If the better betted on any pair
            money += 6*betted_money
            print("+ Banker pair! +")
        else: # If no bet was made
            print("(Banker pair)")

    # Win result
    
    if player_total > bank_total: # Player win
        print("- Player wins! -")
        if player_or_better == "Player" or (player_or_better == "Better" and x_win == "Player"):
            money += 1.95*betted_money

    elif player_total < bank_total:
        print("- Banker wins! -")
        if player_or_better == "Better" and x_win == "Banker":
            money += 1.95*betted_money

    else:
        print("- It's a tie ! -")
        if player_or_better == "Player":
            money += betted_money
        elif player_or_better == "Better" and x_win == "Tie":
            money += 9*betted_money    
    
    print("Your balance: " + str(money))

# Possibilities
baccarat(20, player_or_better="Player")
baccarat(20, player_or_better="Better", x_win="Player")
baccarat(20, player_or_better="Better", pair="Player")

# Problems
baccarat(20, player_or_better="Player", x_win="Player")
baccarat(20, player_or_better="Better")
baccarat(20, player_or_better="Player", pair="Player")
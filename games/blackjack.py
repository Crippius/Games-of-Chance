import random
from problems_check import problems_check

money = 100

deck_of_cards = [
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def blackjack(betted_money, autoplay=False):

    global money

    check = problems_check(betted_money, 
                           checking_dict={autoplay:[True, False]})
    if check["check"] == False:
        print("You've made an incorrect bet, no money will be taken, the problem is:")
        print(check["reason"])
        return

    print("-> Playing Blackjack...")
    money -= betted_money
    
    def figure_to_num(num): # Function that transforms figures to nums
        if type(num) != int:
            return 10
        else:
            return num
    
    round_deck = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    blackjack_card1 = round_deck.pop(random.randint(0, 51)) # Picking first three cards
    blackjack_card2 = round_deck.pop(random.randint(0, 50))
    bank_card1 = round_deck.pop(random.randint(0, 49))
    
    bank_total = figure_to_num(bank_card1) # Calculating totals
    player_total = figure_to_num(blackjack_card1) + figure_to_num(blackjack_card2)

    print("Your cards: " + str(blackjack_card1) + " " + str(blackjack_card2) + " (Total = " + str(player_total) + ")")
    print("Banker's card: " + str(bank_card1))
    
    cards_left = 49
    while player_total < 21: 
        if autoplay == False: # When the player doesn't use autoplay
            decision = input("Do you want to draw another card? (Yes/No) ") # Letting the player decide to draw or not

            if decision.lower() == "yes" or decision.lower() == "y": # Player picks another card
                cards_left -= 1
                blackjack_cardn = round_deck.pop(random.randint(0, cards_left))
                player_total += figure_to_num(blackjack_cardn)
                print("You picked " + str(blackjack_cardn) + " (Total = " + str(player_total) + ")")

            elif decision.lower() == "no" or decision.lower() == "n": # Player stands
                break

            else: # Player makes an incorrect input
                print("Please enter a valid input (Yes/No) ")
        
        else: # Autoplay on / Probability of choosing y/n
            weights_dict = {13:[99, 1], 14:[99, 1], 15:[98,2], 16:[96, 4], 17:[95, 5], 18:[94, 6], 19:[15, 85], 20:[3, 97]}
            
            if player_total <= 17: # 17 is the threshold for drawing  100% of times (banker does the same)
                cards_left -= 1
                blackjack_cardn = round_deck.pop(random.randint(0, cards_left))
                player_total += figure_to_num(blackjack_cardn)
                print("You picked " + str(blackjack_cardn) + " (Total = " + str(player_total) + ")")

            else: # Make a weighted decision
                if random.choices([True, False], weights=weights_dict[player_total])[0]: # Player drawss
                    cards_left -= 1
                    blackjack_cardn = round_deck.pop(random.randint(0, cards_left))
                    player_total += figure_to_num(blackjack_cardn)
                    print("You picked " + str(blackjack_cardn) + " (Total = " + str(player_total) + ")")
                
                else: # Player stands
                    break
            
    if player_total <= 21: # Banker turn

        while bank_total < player_total: # Banker draws
            cards_left -= 1
            bank_cardn = round_deck.pop(random.randint(0, cards_left))
            bank_total += figure_to_num(bank_cardn)

            print("Banker picked " + str(bank_cardn) + " (Total = " + str(bank_total) + ")")
        
        if bank_total > 21 or bank_total < player_total: # Win condition
            money += betted_money*2
            if player_total == 21:
                print("Blackjack!")
                money += betted_money/2
            print("- You won!")
        
        elif bank_total == player_total: # Tie condition
            print("- You drew")
            money += betted_money
        
        else: # Lose condition because the player's total was less than the banker's
            print("- You lost")

    else: # Lose condition because the player bust
        print("- You lost")
    
    print("Your balance: " + str(money))

# Possibilities
blackjack(20)
blackjack(20, autoplay=True)

# Problems
blackjack(20, autoplay="y")

w_l = []
m = []
for i in range(10000):
    money=100
    blackjack(20, autoplay=True)
    if money == 80:
        w_l.append("l")
    else:
        w_l.append("w")
    m.append(money-100)

print(w_l.count("w")/len(w_l))
print(sum(m))

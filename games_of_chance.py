import random

def problems_check(money, betted_money, checking_dict=False, roulette_numbers=False, complimentary=False):
    
    # If an error occurs, the "check" value becomes False and in the "reason" value it is explained which problem occurs
    problems = {"check":True, "reason":[]}
    
    # Resolving problems caused by how the money was bet
    if (type(betted_money) == int or type(betted_money) == float) == False:
        # Type of input was not an integer or float
        problems["check"] = False
        problems["reason"].append("Please input an int or float variable, you typed: " + str(betted_money))
        return problems
    
    if money-betted_money < 0:
        # Not enough money to bet
        problems["check"] = False
        problems["reason"].append("Insufficent funds to bet")
    
    if betted_money < 0:
        # Negative amount of money betted
        problems["check"] = False
        problems["reason"].append("Negative amount of money betted")
    

    # Resolving problems caused by an incorrect input for a certain parameter
    if checking_dict != False:

        # Looping for every parameter
        for i in checking_dict.keys():
            if i not in checking_dict[i]:
                # Input was not one of the possible solutions
                problems["check"] = False
                problems["reason"].append("The bet you chose was not one of the possible alternatives, please choose between: " + str(checking_dict[i]))          
    
    
    # Resolving problems caused by the "numbers" parameter in the roulette function 
    if roulette_numbers != False:
        if type(roulette_numbers) != list:
        # The input is not a list
            problems["check"] = False
            problems["reason"].append("You typed " + str(roulette_numbers) + ", please choose a list class")
        else: 
            if len(set(roulette_numbers)) != len(roulette_numbers):
                # Some duplicates have been inputted        
                dups = []
                for i in set(roulette_numbers):
                    # Finding the duplicates (when their count is greater than one)
                    if roulette_numbers.count(i) > 1:
                        dups.append([i, str(roulette_numbers.count(i)) + " times"])
                problems["check"] = False
                problems["reason"].append("Some duplicates have been found (" + str(dups) + ")")
                    
            if len(roulette_numbers) > 35:
                # Too many numbers inputted
                problems["check"] = False
                problems["reason"].append("Too many numbers have been bet on")
                
            # Variables that will check for errors when the list is looped
            type_loop_check = True
            type_problems = 0
            num_loop_check = True
            num_problems = 0

            for i in roulette_numbers:
                if type(i) != int:
                    type_loop_check = False
                    type_problems += 1
                else:
                    if (i >= 0 and i <= 36) == False:
                        num_loop_check = False
                        num_problems += 1
                
            if type_loop_check == False:
                # Some variables are not integers
                problems["check"] = False
                problems["reason"].append(str(type_problems) + " variables of the list are not integers")
            
            if num_loop_check == False:
                # Some variables are out of bounds
                problems["check"] = False
                problems["reason"].append(str(num_problems) + " numbers of the list are between 0 and 36")           
        
    # Resolving problems caused by complimentary parameters
    if complimentary != False:
        for i in complimentary.keys():
            comp_check = True
            # If the complimentary input is only one
            if type(complimentary[i][2]) != list:
                for j in range(0, len(complimentary[i][0])):
                    if bool(complimentary[i][0][j]) != complimentary[i][2]:
                        comp_check = False
            else:
                for j in range(0, len(complimentary[i][0])):
                    if type(complimentary[i][2][j]) == bool:
                        if bool(complimentary[i][0][j]) != complimentary[i][2][j]:
                            comp_check = False

                    else:
                        if complimentary[i][0][j] != complimentary[i][2][j]:
                            comp_check = False
            if comp_check == True:
                # All parameters are equal
                problems["check"] = False
                problems["reason"].append("Not every parameter can be " + str(complimentary[i][2]) + ", please change one between " + str(complimentary[i][1]))

    return problems



class Casino:

    id = 0

    def __init__(self, money=100):
        self.id = Casino.id
        Casino.id += 1
        self.money = money
        self.record = {}
        print("Welcome to the 'Games of Chance' casino! you have " + str(self.money) + " chips you can bet. Good Luck!")

    def balance(self):
        print("Your balance is: " + str(self.money))
        return self.money

    def set_money(self, money=100):
        self.money = money
        
    def track_record(self, game, result):
        if game not in self.record:
            self.record[game] = []
        self.record[game].append(result)

    def exit_the_casino(self):
        print("Thanks for coming to the 'Games of Chance' casino! Here's your record")
        for i in self.record:
            won = self.record[i].count("Win")
            lost = self.record[i].count("Lost")
            percent = 100
            print("For %s: you won %d games and lost %d, (%d percent of games)" % (i, won, lost, percent))
        final = "gained" if self.money > 100 else ("still have" if self.money==100 else "lost")
        print("---------------------")
        print("You %s %d chips" % (final, abs(self.money-100)))
    
    def heads_or_tails(self, betted_money, prediction=False, autoplay=False):
            # Checking if a correct bet has been made
        check = problems_check(self.money, betted_money, 
                            checking_dict={prediction:["Heads", "Tails", False], 
                                            autoplay:[True, False]}, 
                            complimentary={0:[[prediction, autoplay], ["prediction", "autoplay"], False]})
        if check["check"] == False:
            print("You've made an incorrect bet, no money will be taken, the problem is:")
            print(check["reason"])
            return
        
        print("-> Playing Heads or Tails...")  
        self.money -= betted_money
        
        if autoplay == True and prediction == False:
            prediction = random.choice(["Heads", "Tails"])

        result = random.choice(["Heads", "Tails"])
        
        print("You've bet on: " + prediction)
        print("----------------------")
        print("The result is: " + result)

        # Win result
        if prediction == result:
            print("You win!")
            
            self.money += betted_money*2
            times = 1

            # Offering a 'double or nothing' chance (the choice is made by the program if autoplay is activated)
            if autoplay == False:
                decision = input("Do you want to double or nothing? (Yes/No) ")
            else:
                print("Do you want to double or nothing?")
                decision = random.choices(["Yes", "No"], weights=[20, 80])[0]
                print(decision)
            
            # The while loop works when the user (or program) doubles his offer and repeats itself if the player continues to win
            while decision.lower() == "y" or decision.lower() == "yes":
                
                if autoplay == False:
                    prediction = input("Heads or Tails? ")
                else:
                    print("Heads or Tails?")
                    prediction = random.choice(["Heads", "Tails"])
                    print(prediction)
                
                # The program stops in a while loop if the user doesn't input a correct bet
                while prediction.lower() not in ["heads", "tails"]:
                    print("Please choose between Heads or Tails")
                    prediction = input("Heads or Tails? ")
                
                print("You've bet on: " + prediction)
                print(("----------------------"))
                result = random.choice(["Heads", "Tails"])
                print("The result is: " + result)
                
                if prediction == result:
                    print("- You won!")
                    self.money += betted_money
                    times += 1

                    # The program continues to offer the chance to double or nothing if he continues winning
                    if autoplay == False:
                        decision = input("Do you want to double or nothing again? ")
                    else:
                        print("Do you want to play again?")
                        decision = random.choices(["Yes", "No"], weights=[10, 90])[0]
                        print(decision)
                
                # Lose condition in a double or nothing scenario
                else:
                    print("- You lost")
                    self.money -= betted_money*(1+times)
                    self.track_record("Heads or Tails", "Lost")
                    break
            
            if prediction == result:
                self.track_record("Heads or Tails", "Win")

        # Lose condition
        else:
            print("- You lost")
            self.track_record("Heads or Tails", "Lost")
                
        self.balance()

    def slot_machine(self, betted_money):

        # Checking if a correct bet has been made
        check = problems_check(self.money, betted_money)
        if check["check"] == False:
            print("You've made an incorrect bet, no money will be taken, the problem is:")
            print(check["reason"])
            return
        
        print("-> Playing Slot Machines...")
        self.money -= betted_money
        compensation = 0 # The total compensation depends on the result of the slot, every combination will be added to- this variable

        fruits = ["PEAR", "LEMON", "GRAPE", "KIWI", "BANANA", "BEACH", "APPLE", "CHERRY", "ORANGE"]
        big = ["7", "DIAMOND", "BAR"]

        wheel_slot_dict = {range(1, 11):"PEAR", range(11, 21):"LEMON", range(21, 31):"GRAPE", range(31, 41):"KIWI", range(41, 51):"BANANA", 
                        range(51, 61):"PEACH", range(61, 71):"APPLE", range(71, 81):"CHERRY", range(81, 91):"ORANGE", #Every symbol corresponds to a set of
                        range(91, 101):"7", range(101, 105):"DIAMOND", range(105, 109):"BAR", range(109, 111):"JACKPOT"} # numbers, the best one are less probable
        
        def find_wheel_symbols(num_list): # Transforms numbers into symbols
            keys = list(wheel_slot_dict.keys())
            new_list = []
            for i in num_list:
                for y in keys:
                    if i in y:
                        new_list.append(wheel_slot_dict[y])
            return new_list
        
        # Manipulating randomness to profit the house (TOP SECRET)
        start = random.randint(1, 55)
        end = random.randint(46, 100)

        first_wheel = find_wheel_symbols([random.randint(1, start), random.randint(1, 100), random.randint(1, start)])  
        second_wheel = find_wheel_symbols([random.randint(end, 100), random.randint(1, start), random.randint(1, 100)]) # Evaluating symbols
        third_wheel = find_wheel_symbols([random.randint(1, 100), random.randint(end, 100), random.randint(end, 100)])

        print("-"*8*3)
        for i in range(0, 3): 
            divisor1 = " "*(8 - len(first_wheel[i])+1)        # Visualizazion for user
            divisor2 = " "*(8 - len(second_wheel[i])+1)  
            print(first_wheel[i] + divisor1 + second_wheel[i] + divisor2 + third_wheel[i])
            print("-"*8*3)

        # Finding results   
        for i in range(0, 3):
            if first_wheel[i] == second_wheel[i] == third_wheel[i]:
                if first_wheel[i] in fruits:
                    compensation += 4
                    print("TRIPLE " + first_wheel[i] + "!")

                if first_wheel[i] in big:
                    compensation += 10
                    print("TRIPLE " + first_wheel[i] + "!!")

                if first_wheel[i] == "JACKPOT":
                    compensation += 31
                    print(first_wheel[i] + "!!!") # JACKPOT!!!

            
            elif first_wheel[i] == second_wheel[i] or first_wheel[i] == third_wheel[i] or second_wheel[i] == third_wheel[i]:
                
                double = second_wheel[i]                # Finding which symbol is double
                if first_wheel[i] == second_wheel[i] or first_wheel[i] == third_wheel[i]:
                    double = first_wheel[i]
                
                if double in fruits:
                    compensation += 1.25
                    print("DOUBLE " + first_wheel[i] + "!")

                if double in big:
                    compensation += 2
                    print("DOUBLE " + first_wheel[i] + "!!")
        
        if compensation != 0:
            print("- You won!")
            self.money += betted_money*compensation
            self.track_record("Slot Machine", "Win")
        else:
            print("- You lost")
            self.track_record("Slot Machine", "Lost")
        
        self.balance()

    def blackjack(self, betted_money, autoplay=False):

        check = problems_check(self.money, betted_money, 
                            checking_dict={autoplay:[True, False]})
        if check["check"] == False:
            print("You've made an incorrect bet, no money will be taken, the problem is:")
            print(check["reason"])
            return

        print("-> Playing Blackjack...")
        self.money -= betted_money
        
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
            
            else: # Autoplay on  /  Probability of choosing y/n
                weights_dict = {13:[99, 1], 14:[99, 1], 15:[98,2], 16:[96, 4], 17:[95, 5], 18:[94, 6], 19:[15, 85], 20:[3, 97]}
                
                if player_total < 13: # 13 is the threshold for drawing  100% of times (banker does the same)
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
                self.money += betted_money*2
                if player_total == 21:
                    print("Blackjack!")
                    self.money += betted_money/2
                print("- You won!")
                self.track_record("Blackjack", "Win")
            
            elif bank_total == player_total: # Tie condition
                print("- You drew")
                self.money += betted_money
                self.track_record("Blackjack", "Tie")
            
            else: # Lose condition because the player's total was less than the banker's
                print("- You lost")
                self.track_record("Blackjack", "Lost")

        else: # Lose condition because the player bust
            print("- You lost")
            self.track_record("Blackjack", "Lost")
        
        self.balance()

    def roulette(self, betted_money, odd_or_even=False, manque_or_passe=False, red_black_green=False, numbers=False):

        # Checking if a correct bet has been made
        check = problems_check(self.money, betted_money, 
                            checking_dict={odd_or_even:["Odd", "Even", False], 
                                            manque_or_passe:["Manque", "Passe", False], 
                                            red_black_green:["Red", "Black", "Green", False]}, 
                            roulette_numbers=numbers, 
                            complimentary={0:[[odd_or_even, manque_or_passe, numbers, red_black_green], ["odd_or_even", "manque_or_passe", "numbers", "red_black_green"], False], 
                                            1:[[numbers, odd_or_even], ["numbers", "odd_or_even"], not False],
                                            2:[[numbers, manque_or_passe], ["numbers", "manque_or_passe"], not False],
                                            3:[[numbers, red_black_green], ["numbers", "red_black_green"], not False]})
                                
        if check["check"] == False:
            print("You've made an incorrect bet, no money will be taken, the problem is:")
            print(check["reason"])
            return
            
        print("-> Playing Roulette...")

        self.money -= betted_money
        result = random.randint(0, 36)
        
        # win_check will keep track if the win condition the player bets on happened
        win_check = True
        compensation = 1
        print("You've bet on:")

        o_e_result = ""
        m_p_result = ""
        r_b_g_result = ""
        
        # Result for the Even/Odd bet (0 doesn't count so it favours house)
        if result%2 == 0 and result != 0:
            o_e_result = "Even"
        elif result != 0:
            o_e_result = "Odd"
        
        # Result for the Manque/Passe bet (same thing for the zero)
        if result >= 1 and result <= 18:
            m_p_result = "Manque"
        elif result != 0:
            m_p_result = "Passe"
            
        reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        # Result for the Red/Black/Green bet
        if result in reds:
            r_b_g_result = "Red"
        elif result in blacks:
            r_b_g_result = "Black"
        else:
            r_b_g_result = "Green"

        
        # After getting the results it checks if the bet has been made and if it is congruent
        if odd_or_even != False:
            print(odd_or_even)
            if odd_or_even != o_e_result:
                win_check = False
            else:
                compensation += 1
        
        if manque_or_passe != False:
            print(manque_or_passe)
            if manque_or_passe != m_p_result:
                win_check = False
            else:
                compensation += 1
        
        if red_black_green != False:
            print(red_black_green)
            if red_black_green != r_b_g_result:
                win_check = False
            elif r_b_g_result == red_black_green == "Green":
                compensation += 35
            else:
                compensation += 1
        
        if numbers != False:
            print("The number(s):  " + str(numbers))
            if result not in numbers:
                win_check = False
            else:
                compensation += round(35/len(numbers))-2
        
        print("The number was: " + str(result) + " (" + o_e_result + ", " + m_p_result + ", " + r_b_g_result + ")")

        # If win_check passes all of the bets the player wins
        if win_check == True:
            # If the player bets on two or more things simultaneously the compensation is greater
            self.money += betted_money*compensation
            print("- You won!")
            self.track_record("Roulette", "Win")
        else:
            print("- You lost")
            self.track_record("Roulette", "Lost")
        
        self.balance()  

    def baccarat(self, betted_money, player_or_better="Player", x_win=False, pair=False):

        # Checking if a correct bet has been made
        check = problems_check(self.money, betted_money,
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
        
        self.money -= betted_money

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
                self.money += 8*betted_money
                print("++ Player pair! ++")
                self.track_record("Baccarat", "Win")
            elif pair == "Any": # If the better betted on any pair
                any_case = False
                self.money += 6*betted_money
                print("+ Player pair! +")
                self.track_record("Baccarat", "Win")
            else: # If no bet was made
                print("(Player pair)")

        elif bank_card1 == bank_card2 or bank_card2 == bank_card3 or bank_card3 == bank_card1:
            if pair == "Banker": # If the better betted on a banker pair
                print("++ Banker pair! ++ ")
                self.money += 12*betted_money
                self.track_record("Baccarat", "Win")
            elif pair == "Any" and any_case == True: # If the better betted on any pair
                self.money += 6*betted_money
                print("+ Banker pair! +")
                self.track_record("Baccarat", "Win")
            else: # If no bet was made
                print("(Banker pair)")

        # Win result
        
        if player_total > bank_total: # Player win
            print("- Player wins! -")
            if player_or_better == "Player" or (player_or_better == "Better" and x_win == "Player"):
                self.money += 1.95*betted_money
                self.track_record("Baccarat", "Win")
            else:
                self.track_record("Baccarat", "Lost")            

        elif player_total < bank_total:
            print("- Banker wins! -")
            if player_or_better == "Better" and x_win == "Banker":
                self.money += 1.95*betted_money
                self.track_record("Baccarat", "Win")
            else:
                self.track_record("Baccarat", "Lost")

        else:
            print("- It's a tie ! -")
            self.track_record("Baccarat", "Tie")
            if player_or_better == "Player":
                self.money += betted_money
            elif player_or_better == "Better" and x_win == "Tie":
                self.money += 9*betted_money    
        
        self.balance()

        
# player_1 = Casino()

# player_1.heads_or_tails(20, autoplay=True)
# player_1.roulette(20, odd_or_even="Odd")
# player_1.slot_machine(20)
# player_1.blackjack(20, autoplay=True)
# player_1.baccarat(20, player_or_better="Player")

# player_1.exit_the_casino()
import random
from problems_check import problems_check

money = 100

def roulette(betted_money, odd_or_even=False, manque_or_passe=False, red_black_green=False, numbers=False):
    
    global money

    # Checking if a correct bet has been made
    check = problems_check(betted_money, 
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

    money -= betted_money
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
        money += betted_money*compensation
        print("- You won!")
    else:
        print("- You lost")
    
    print("Your balance: " + str(money))       

# Possibilities
roulette(20, odd_or_even="Odd")
roulette(20, manque_or_passe="Manque")
roulette(20, red_black_green="Red")
roulette(20, numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
roulette(20, odd_or_even="Even", manque_or_passe="Passe", red_black_green="Black")

# Problems
roulette(20)
roulette(20, numbers=[31], red_black_green="Red")
roulette(20, red_black_green="Yellow")

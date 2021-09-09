import random

money = 100

def problems_check(betted_money, checking_dict=False, roulette_numbers=False, complimentary=False):
    
    global money
    
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
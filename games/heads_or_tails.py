import random

from problems_check import problems_check

money = 100

def heads_or_tails(betted_money, prediction=False, autoplay=False):
    
    global money
    
    # Checking if a correct bet has been made
    check = problems_check(betted_money, 
                           checking_dict={prediction:["Heads", "Tails", False], 
                                          autoplay:[True, False]}, 
                           complimentary={0:[[prediction, autoplay], ["prediction", "autoplay"], False]})
    if check["check"] == False:
        print("You've made an incorrect bet, no money will be taken, the problem is:")
        print(check["reason"])
        return
    
    print("-> Playing Heads or Tails...")  
    money -= betted_money
    
    if autoplay == True and prediction == False:
        prediction = random.choice(["Heads", "Tails"])

    result = random.choice(["Heads", "Tails"])
    
    print("You've bet on: " + prediction)
    print("----------------------")
    print("The result is: " + result)
    
    # Win result
    if prediction == result:
        print("You win!")
        
        money += betted_money*2
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
                money += betted_money
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
                print("You lost")
                money -= betted_money*(1+times)
                break
    
    # Lose condition
    else:
        print("- You lost")
            
    print("Your balance: " + str(money))

heads_or_tails(20, prediction="Heads")
heads_or_tails(20, autoplay=True)
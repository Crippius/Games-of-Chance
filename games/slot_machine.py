import random
from problems_check import problems_check

money = 100

def slot_machine(betted_money):
    
    global money

    # Checking if a correct bet has been made
    check = problems_check(betted_money)
    if check["check"] == False:
        print("You've made an incorrect bet, no money will be taken, the problem is:")
        print(check["reason"])
        return
    
    print("-> Playing Slot Machines...")
    money -= betted_money
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
        money += betted_money*compensation
    else:
        print("- You lost")
    
    print("Your balance: " + str(money)) 

# Possibilities
slot_machine(20)

w_l = []
m = []
for i in range(10000):
    money=100
    slot_machine(20)
    if money == 80:
        w_l.append("l")
    else:
        w_l.append("w")
    m.append(money-100)

print(w_l.count("w")/len(w_l))
print(sum(m)) 
